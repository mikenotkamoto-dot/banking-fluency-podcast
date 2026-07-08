# Banking Fluency Podcast Feed

Unlisted podcast feed for `Banking Fluency for Bitcoin-Age Operators`.

## Current state

- Source library: `/Users/emilealbert/FRIDAY/walkcasts/banking-fluency`
- Built feed path: `docs/feed-f3204d3f5ca71c56/feed.xml`
- Public/unlisted feed URL:
  `https://mikenotkamoto-dot.github.io/banking-fluency-podcast/feed-f3204d3f5ca71c56/feed.xml`

## Privacy truth

GitHub Pages serves a publicly reachable RSS feed. This is **unlisted**, not truly private:

- obscure feed path
- `robots.txt` disallow
- `noindex,nofollow` landing page
- no directory submission unless Leo explicitly requests it

## Update

```bash
cd /Users/emilealbert/FRIDAY/projects/banking-fluency-podcast
python3 update_feed.py
git add update_feed.py docs README.md
git commit -m "chore: update banking fluency podcast feed"
git push
```
