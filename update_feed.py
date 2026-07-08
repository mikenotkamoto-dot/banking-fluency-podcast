#!/usr/bin/env python3
"""Build the static Banking Fluency podcast feed from the local course audio library."""
from __future__ import annotations

from email.utils import formatdate
from pathlib import Path
import hashlib
import html
import json
import re
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont

SRC = Path('/Users/emilealbert/FRIDAY/walkcasts/banking-fluency')
PUBLIC = Path(__file__).resolve().parent / 'docs'
SECRET_PATH = 'feed-f3204d3f5ca71c56'
BASE_URL = 'https://mikenotkamoto-dot.github.io/banking-fluency-podcast'


def ffprobe_duration(path: Path) -> str:
    candidates = ['/opt/homebrew/bin/ffprobe', 'ffprobe']
    for ffprobe in candidates:
        try:
            res = subprocess.run(
                [ffprobe, '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=nk=1:nw=1', str(path)],
                text=True,
                capture_output=True,
                timeout=20,
            )
            if res.returncode == 0 and res.stdout.strip():
                secs = int(float(res.stdout.strip()))
                return f'{secs // 3600:02d}:{(secs % 3600) // 60:02d}:{secs % 60:02d}'
        except Exception:
            continue
    return ''


def build_cover() -> None:
    cover_img = Image.new('RGB', (1400, 1400), '#07111f')
    draw = ImageDraw.Draw(cover_img)
    draw.rectangle((0, 0, 1400, 1400), fill='#07111f')
    draw.ellipse((850, -120, 1530, 560), fill='#102a43')
    draw.ellipse((-180, 920, 560, 1620), fill='#3a2414')
    draw.rectangle((110, 1010, 1290, 1030), fill='#f59e0b')
    try:
        title_font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 112)
        sub_font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 48)
        small_font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 36)
    except Exception:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    draw.text((110, 430), 'Banking', fill='#f8fafc', font=title_font)
    draw.text((110, 560), 'Fluency', fill='#f8fafc', font=title_font)
    draw.text((115, 730), 'for Bitcoin-Age Operators', fill='#cbd5e1', font=sub_font)
    draw.text((115, 1085), 'Banks • Credit Unions • Regulation • Galoy Lens', fill='#94a3b8', font=small_font)
    cover_img.save(PUBLIC / 'cover.png', 'PNG')


def parse_episode_dir(day_dir: Path) -> dict | None:
    match = re.match(r'(\d{4}-\d{2}-\d{2})-day-(\d{3})-(.+)', day_dir.name)
    if not match:
        return None
    date, day, slug = match.groups()
    mp3s = sorted(day_dir.glob('*.mp3'))
    if not mp3s:
        return None
    return {'date': date, 'day': day, 'slug': slug, 'src_mp3': mp3s[0]}


def build() -> dict:
    (PUBLIC / 'episodes').mkdir(parents=True, exist_ok=True)
    feed_dir = PUBLIC / SECRET_PATH
    feed_dir.mkdir(parents=True, exist_ok=True)

    items: list[dict] = []
    for day_dir in sorted((SRC / 'episodes').glob('*-day-*')):
        if not day_dir.is_dir():
            continue
        parsed = parse_episode_dir(day_dir)
        if not parsed:
            continue
        date, day, slug, src_mp3 = parsed['date'], parsed['day'], parsed['slug'], parsed['src_mp3']
        dest_dir = PUBLIC / 'episodes' / day_dir.name
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_mp3 = dest_dir / src_mp3.name
        if not dest_mp3.exists() or dest_mp3.stat().st_size != src_mp3.stat().st_size:
            shutil.copy2(src_mp3, dest_mp3)
        for sidecar in day_dir.glob('*.md'):
            dest_sidecar = dest_dir / sidecar.name
            if not dest_sidecar.exists() or dest_sidecar.stat().st_size != sidecar.stat().st_size:
                shutil.copy2(sidecar, dest_sidecar)
        title = ' '.join(word.capitalize() for word in slug.split('-'))
        items.append({
            'date': date,
            'day': day,
            'title': title,
            'mp3_rel': f'episodes/{day_dir.name}/{src_mp3.name}',
            'size': dest_mp3.stat().st_size,
            'mtime': dest_mp3.stat().st_mtime,
            'duration': ffprobe_duration(src_mp3),
        })

    build_cover()
    (PUBLIC / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
    (PUBLIC / '.nojekyll').write_text('', encoding='utf-8')

    feed = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:podcast="https://podcastindex.org/namespace/1.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">',
        '<channel>',
        '<title>Banking Fluency for Bitcoin-Age Operators</title>',
        f'<link>{BASE_URL}/</link>',
        '<language>en-ca</language>',
        '<itunes:author>FRIDAY</itunes:author>',
        '<description>A structured daily course for understanding banks, credit unions, regulation, payments, lending, custody, and the institutional context for Bitcoin-age financial infrastructure.</description>',
        '<itunes:summary>A structured daily course for understanding banks, credit unions, regulation, payments, lending, custody, and the institutional context for Bitcoin-age financial infrastructure.</itunes:summary>',
        '<itunes:explicit>false</itunes:explicit>',
        '<itunes:type>episodic</itunes:type>',
        '<itunes:category text="Education"/>',
        f'<itunes:image href="{BASE_URL}/cover.png"/>',
        f'<lastBuildDate>{formatdate(time.time(), usegmt=True)}</lastBuildDate>',
    ]

    for item in reversed(items):
        episode_url = f"{BASE_URL}/{item['mp3_rel']}"
        desc = f"Banking Fluency Day {item['day']}: {item['title']}. A regulated-financial-institution fluency lesson for Bitcoin-age operators."
        guid = f"banking-fluency-{item['day']}-{hashlib.sha256(item['mp3_rel'].encode()).hexdigest()[:12]}"
        feed.extend([
            '<item>',
            f'<title>Day {item["day"]}: {html.escape(item["title"])}</title>',
            f'<description>{html.escape(desc)}</description>',
            f'<itunes:summary>{html.escape(desc)}</itunes:summary>',
            f'<pubDate>{formatdate(item["mtime"], usegmt=True)}</pubDate>',
            f'<guid isPermaLink="false">{guid}</guid>',
            f'<enclosure url="{episode_url}" length="{item["size"]}" type="audio/mpeg"/>',
            f'<itunes:episode>{int(item["day"])}</itunes:episode>',
        ])
        if item['duration']:
            feed.append(f'<itunes:duration>{item["duration"]}</itunes:duration>')
        feed.append('</item>')
    feed.extend(['</channel>', '</rss>'])
    feed_path = feed_dir / 'feed.xml'
    feed_path.write_text('\n'.join(feed), encoding='utf-8')
    ET.parse(feed_path)

    index = f'''<!doctype html><html><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Banking Fluency</title><style>body{{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;background:#07111f;color:#f8fafc;max-width:760px;margin:6rem auto;padding:0 1.5rem;line-height:1.55}}a{{color:#60a5fa}}code{{background:#111827;padding:.2rem .35rem;border-radius:.25rem}}</style></head><body><h1>Banking Fluency</h1><p>Unlisted podcast feed for Banking Fluency for Bitcoin-Age Operators.</p><p><strong>RSS feed:</strong><br><a href="/{SECRET_PATH}/feed.xml">/{SECRET_PATH}/feed.xml</a></p><p>Latest day: {items[-1]['day'] if items else 'n/a'} · Episodes in feed: {len(items)}</p><p>Add the RSS URL manually in Apple Podcasts or another podcast app.</p></body></html>'''
    (PUBLIC / 'index.html').write_text(index, encoding='utf-8')
    return {
        'episodes': len(items),
        'latest_day': items[-1]['day'] if items else None,
        'feed_path': str(feed_path),
        'intended_feed_url': f'{BASE_URL}/{SECRET_PATH}/feed.xml',
    }


if __name__ == '__main__':
    print(json.dumps(build(), indent=2))
