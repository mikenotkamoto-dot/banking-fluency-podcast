# Banking Fluency — Day 007

## Title

Credit II: Collateral, Reserves, and Loss Severity

## Place in the course

Day 006 treated underwriting as a forward-looking judgment about expected repayment. This lesson begins where that repayment thesis weakens: collateral may improve recovery, the allowance recognizes estimated credit losses before final collection outcomes are known, and a charge-off removes amounts deemed uncollectible.

Keep this bridge brief. Do not reteach borrower capacity, willingness, loan purpose, debt-service coverage, or loan structuring.

## Learning objective

Explain how collateral can reduce loss without creating ordinary-course repayment capacity; distinguish probability of default from loss severity; evaluate whether collateral is legally available and economically realizable; and trace the distinct roles of the allowance for credit losses, provision expense, charge-offs, and recoveries.

## The coherent layer: from missed repayment to realized loss

A borrower’s failure to make contractual payments does not by itself reveal how much the lender will ultimately lose. The economic path is:

> Repayment weakens → the institution reassesses collectibility → collateral and other recoveries affect the expected shortfall → the allowance is updated → confirmed uncollectible amounts are charged off → later collections are recoveries

Four questions keep this path coherent:

1. **Will default occur?** This concerns the likelihood that the borrower will fail to perform as agreed.
2. **What exposure will exist then?** The balance at risk may include funded principal and, depending on the product and accounting framework, other amounts or future drawings.
3. **What can actually be recovered?** Recovery can come from borrower cash, collateral, guarantees, insurance, restructuring, or collection—but only to the extent those sources are legally enforceable and economically realizable.
4. **When should the expected or confirmed loss enter the accounts?** The allowance, provision, charge-off, and recovery answer different parts of this accounting question.

**Simplification label:** This pack uses a U.S. bank and U.S. GAAP/CECL frame. It is educational, not a complete statement of Accounting Standards Codification Topic 326, Call Report instructions, tax rules, regulatory capital, appraisal law, bankruptcy priorities, consumer collection law, or product-specific charge-off policy. Credit unions and institutions in other jurisdictions may use different reporting language and requirements.

## Default frequency and loss severity are different dimensions

Two portfolios can produce the same number of defaults and very different losses.

- **Probability of default (PD)** is the likelihood that a borrower or exposure defaults over a defined period under a defined default standard.
- **Exposure at default (EAD)** is the amount exposed when default occurs.
- **Loss given default (LGD), or loss severity,** is the portion of exposure not recovered after considering recoveries and relevant costs.

A simplified economic relationship is:

> Expected credit loss ≈ PD × EAD × LGD

Suppose two $1 million loans both default. Loan A produces $900,000 of net recoveries; its simplified loss severity is 10 percent. Loan B produces $400,000 of net recoveries; its simplified loss severity is 60 percent. The default event is the same category of event, but the loss is not.

This is why “secured” is not a binary synonym for “safe.” Collateral generally acts most directly on recovery and loss severity. It may also affect borrower behavior or default likelihood, but valuable collateral cannot automatically cure weak cash flow, an incoherent loan structure, or a borrower unable to pay.

**Simplification label:** CECL does not require every institution to use a PD × EAD × LGD model, and those terms can have model-specific definitions. U.S. GAAP permits various appropriate methods. The formula is a conceptual decomposition, not an instruction for calculating an allowance.

## What collateral actually does

**Collateral** is property or another asset in which the lender has legally effective rights intended to support repayment or recovery. Examples include real estate, equipment, vehicles, inventory, receivables, securities, cash, deposit accounts, or other eligible assets.

Collateral can serve different functions:

- provide a secondary recovery source if ordinary repayment fails;
- form part of the intended cash-conversion mechanism in a properly controlled asset-based facility;
- limit the lender’s advance relative to a borrowing base or loan-to-value measure;
- create monitoring signals when collateral quantity, quality, or value deteriorates; and
- influence pricing, structure, approval authority, and expected loss severity.

The phrase **secondary source of repayment** is useful but not universal. In many conventional commercial loans, recurring operating cash flow is expected to pay the debt and collateral is a fallback. In some asset-based lending, orderly conversion of controlled receivables or inventory into cash is the intended primary mechanism. The lender must describe the actual transaction rather than rely on a slogan.

The FDIC’s examination manual warns that undue reliance on appraised real-estate value instead of repayment ability is dangerous. It also notes that the current potential sale price or liquidating value can differ from appraised value because demand may be weak and a distressed sale may require a sacrifice price.

## A collateral checklist is not a recovery analysis

An appraisal or asset list is only an input. A credible recovery estimate tests at least six layers.

### 1. Existence and identity

Does the asset exist, and is it the asset described in the credit file? Inventory can be obsolete or missing. Receivables can be disputed, aged, already paid, owed by affiliates, or subject to offsets. Equipment can be highly specialized. Real estate can have environmental, zoning, title, condition, or occupancy problems.

### 2. Ownership and enforceability

Does the borrower or pledgor own rights that can be pledged? Is the security agreement valid? Was the lien perfected through the legally required filing, possession, control, notation, or other step? Are descriptions accurate? Have filings lapsed? Do local law, bankruptcy, consumer protections, or another legal constraint limit enforcement?

### 3. Priority

Who is paid first? Taxes, prior liens, purchase-money interests, warehouse claims, landlords, possessory liens, setoff rights, or other claims may rank ahead of the lender. A lender can hold a valid lien and still receive little because its priority is junior.

### 4. Control and preservation

Can the borrower sell, move, substitute, dilute, or encumber the collateral without detection? Are receivable proceeds directed through controlled accounts? Are inspections, field audits, title checks, insurance, maintenance, storage, and concentration limits adequate? A first-priority lien on disappearing collateral is less comforting than the paperwork suggests.

### 5. Current realizable value

Which value is relevant: retail, wholesale, orderly liquidation, forced liquidation, fair value, appraised market value, or another defined basis? How current is the valuation? What assumptions concern condition, occupancy, market depth, collection rates, dilution, volatility, or time to sale? Value at origination is not necessarily value during stress.

### 6. Time and cost to realize

Repossession, foreclosure, transport, storage, legal work, repairs, taxes, brokers, auction discounts, environmental remediation, and selling costs consume recovery. Delay also matters: a nominal future receipt is not identical to immediately available cash, and collateral can deteriorate while enforcement proceeds.

A useful operator’s question is therefore not “What is the collateral worth?” but:

> What net cash can this institution legally obtain, in what time, under a realistic stress scenario, after senior claims and realization costs?

**Simplification label:** The correct valuation and legal analysis is asset-, transaction-, jurisdiction-, and reporting-date-specific. “Haircuts” and advance rates are policy tools, not universal facts. A valuation should not be adjusted casually to manufacture the desired decision.

## Worked collateral case: appraisal value is not net recovery

A bank has a $1 million outstanding loan. The borrower’s operating cash flow has failed, and the bank is evaluating the collateral. Use these deliberately simplified facts:

- current collateral fair value: **$800,000**;
- estimated costs to sell: **$60,000**;
- a legally senior claim that must be satisfied from the same collateral: **$100,000**; and
- no other assumed recovery for this illustration.

A simplified recovery bridge is:

> $800,000 fair value − $60,000 selling costs − $100,000 senior claim = $640,000 net collateral available

The simplified uncovered amount is:

> $1,000,000 exposure − $640,000 net collateral available = $360,000

The corresponding simplified loss severity is:

> $360,000 ÷ $1,000,000 = 36 percent

This does **not** automatically mean the bank should record a $360,000 allowance or charge-off. Before reaching an accounting conclusion, management must determine the applicable measurement framework, whether the asset is collateral-dependent, whether the valuation is current and supported, which costs and claims are appropriate, whether other repayment sources are meaningful, and whether any portion is confirmed uncollectible.

The case demonstrates only the economic mechanism: headline collateral value can materially overstate net recovery.

## When a loan becomes collateral-dependent

The OCC and FDIC describe a **collateral-dependent financial asset** as one for which repayment is expected to be provided substantially through operation or sale of the collateral when the borrower is experiencing financial difficulty as of the reporting date.

That is narrower than “a secured loan.” A healthy mortgage, equipment loan, or secured commercial loan does not become collateral-dependent merely because collateral exists. The determination depends on the borrower’s financial difficulty and whether cash flows from sources other than collateral—including guarantors—are expected to be more than nominal.

For regulatory reporting, the allowance for a collateral-dependent loan is measured using the fair value of collateral. If repayment depends on **sale**, fair value is adjusted for estimated costs to sell. If repayment depends only on **operation** of the collateral, the selling-cost adjustment is not made. The OCC states that loss recognition cannot be delayed until foreclosure occurs.

If the collateral’s fair value changes, the estimate must respond. A stale appraisal may not represent fair value at the balance-sheet date when market conditions, property use, asset condition, or realization assumptions have changed. Management needs support for appraisals, evaluations, adjustments, costs to sell, and the independence and competence of valuation work.

**Simplification label:** “Collateral-dependent” is an accounting and regulatory-reporting term with defined conditions. It should not be used loosely to describe every secured exposure or every loan whose collateral coverage has weakened.

## The allowance is an estimate, not a vault of cash

The **allowance for credit losses (ACL)** is a balance-sheet valuation account. For financial assets carried at amortized cost, it generally reduces the reported asset amount to present the net amount expected to be collected over the contractual term, considering the applicable accounting requirements.

The ACL is not:

- cash set aside in a separate account;
- regulatory capital;
- a liquidity buffer;
- proof that a specific borrower has defaulted;
- the same thing as a charge-off; or
- a discretionary rainy-day fund that management may inflate or suppress to smooth earnings.

Under CECL, an ACL is established upon origination or acquisition for in-scope assets and reevaluated at each reporting period. Management considers historical loss information, current conditions, and reasonable and supportable forecasts, with the required treatment beyond the forecastable period. Assets sharing similar risk characteristics are generally evaluated collectively; assets that do not share those characteristics are evaluated individually.

Estimation is inherently judgmental, but not arbitrary. The OCC’s handbook says the bank should support and record its best estimate within the range of expected credit losses. Methods, data, segmentation, forecasts, qualitative adjustments, governance, controls, and documentation must fit the institution’s portfolio, complexity, and risk profile.

**Terminology warning:** People often say “loan-loss reserves.” In this lesson, use the precise term **allowance for credit losses** when referring to the contra-asset valuation account. “Reserve” can also refer informally to liquidity, central-bank balances, capital buffers, or other accounts. Those are not interchangeable.

## Provision expense changes the allowance

A **provision for credit losses (PCL)** is the income-statement mechanism used to adjust the related ACL to the amount management determines is appropriate at the reporting date. In ordinary simplified terms:

- increasing the needed ACL produces provision expense and lowers pre-tax income;
- decreasing the needed ACL can produce a negative provision or provision benefit, subject to the applicable framework; and
- the resulting allowance remains on the balance sheet as a valuation account.

This links credit deterioration to earnings before the final cash loss is known. If forecasts weaken, risk ratings deteriorate, collateral values fall, or portfolio composition changes, the estimated expected loss may rise and require more allowance through provision expense.

Provision is not the loss event itself. It is the accounting adjustment to the estimate.

## Charge-offs remove amounts deemed uncollectible

A **charge-off**—also called a write-off under ASC Topic 326—records that all or part of a financial asset is deemed uncollectible. The OCC states that write-offs may be full or partial and are deducted from the allowance. Financial-asset charge-offs generally debit the ACL and establish a new amortized cost basis for the remaining asset.

The timing matters. Uncollectible amounts should be charged off in the period they become uncollectible; a bank should not keep a basically worthless amount on the balance sheet merely because some future salvage recovery remains possible. OCC credit-classification guidance defines **loss** assets as uncollectible and of such little value that continuing them as bankable assets is not warranted, even though partial recovery may occur later.

A charge-off does not necessarily mean:

- collection activity stops;
- the legal debt is forgiven;
- no future recovery is possible;
- the bank first experiences the economics of the loss that day; or
- current-period provision expense must equal the charge-off.

If charge-offs make the remaining ACL inappropriate, provision expense is recognized to restore the allowance to an appropriate level. Charge-offs are not debited directly to retained earnings.

**Simplification label:** Product-specific regulatory policies can prescribe charge-off timing, particularly for retail credit. Legal discharge, debt forgiveness, tax treatment, nonaccrual status, regulatory classification, and accounting charge-off are related but distinct determinations.

## Recoveries are later collections on charged-off amounts

A **recovery** occurs when the institution collects an amount previously charged off. Recoveries are recognized when received and become part of the institution’s historical loss record. The FDIC manual states that recoveries on financial assets measured at amortized cost are credited to the related ACL, subject to the applicable limit based on amounts previously charged off; excess collections are generally noninterest income.

The possibility of recovery does not justify delaying a required charge-off. The accounting sequence preserves the distinction:

1. estimate expected losses through the ACL;
2. charge off amounts when deemed uncollectible; and
3. recognize actual recoveries when collected.

## A simplified allowance roll-forward

A compact roll-forward helps prevent terminology drift:

> Ending ACL = beginning ACL + provision expense − charge-offs + recoveries

Suppose a portfolio begins the quarter with a $40,000 ACL. During the quarter, the bank records $25,000 of provision expense, charges off $10,000, and receives $2,000 of recoveries.

> $40,000 + $25,000 − $10,000 + $2,000 = $57,000 ending ACL

Interpret each movement correctly:

- **$25,000 provision:** current-period income-statement adjustment to the estimate;
- **$10,000 charge-off:** removal of an amount deemed uncollectible against the allowance;
- **$2,000 recovery:** later cash collection on an amount previously charged off; and
- **$57,000 ending ACL:** the valuation account after those movements, not cash and not capital.

The provision does not have to equal the quarter’s charge-offs. Management is estimating losses over the applicable contractual terms of the remaining portfolio, not merely replacing this quarter’s write-offs dollar for dollar.

**Simplification label:** Real regulatory reports separate allowance categories and may include other adjustments, acquired-credit accounting effects, off-balance-sheet credit-loss liabilities, securities treatment, foreign-currency effects, or other items. The equation is a teaching roll-forward, not a Call Report template.

## Why collateral quality and allowance quality depend on operations

A recovery estimate is only as sound as the operational system beneath it. Weak controls can make nominal collateral illusory and expected-loss estimates unreliable.

A sound institution needs processes that can:

- perfect and renew liens on time;
- establish and verify priority;
- inspect physical collateral and test title or ownership;
- validate receivables, inventory, and borrowing-base reports;
- monitor insurance, taxes, maintenance, location, and condition;
- obtain independent, current appraisals or evaluations when required;
- identify concentrations and correlated collateral-value declines;
- re-rate deteriorating credits promptly;
- transfer assets out of pools when they no longer share similar risk characteristics;
- identify collateral-dependent status at the reporting date;
- distinguish current fair value from stale origination value;
- document assumptions, forecasts, overrides, and qualitative adjustments;
- charge off uncollectible amounts on time; and
- record recoveries consistently so historical loss data remain usable.

A delayed charge-off is not merely cosmetic. The OCC notes that timely charge-offs and recoveries form foundational historical loss data. Poor charge-off discipline can therefore distort both today’s asset values and tomorrow’s expected-loss estimates.

## Institutional operator scenario

A bank made a $1.5 million loan to a regional equipment dealer. The original approval relied on operating cash flow, a first lien on inventory and receivables, and a personal guarantee. Eighteen months later:

- sales are down 25 percent;
- receivables aging has lengthened;
- several major receivables are disputed;
- inventory reports have not been field-tested for nine months;
- some equipment models are obsolete;
- a tax lien may have priority;
- the guarantor’s financial statement is 14 months old;
- the last collateral appraisal predates the downturn; and
- management says the loan is “fully secured” using the old gross values.

A rigorous operator should not begin with a single reserve percentage. The sequence is:

1. **Reassess repayment:** Is ordinary operating cash flow still a meaningful source, or is repayment now expected substantially from collateral?
2. **Verify the collateral:** Test existence, eligibility, aging, disputes, obsolescence, ownership, lien perfection, priority, insurance, and control of proceeds.
3. **Update realizable value:** Use a valuation basis appropriate to the reporting date and stress conditions; deduct relevant costs and senior claims rather than relying on gross appraisal value.
4. **Reassess the guarantee:** Verify enforceability, liquidity, competing claims, and willingness; an old personal financial statement is not cash.
5. **Determine accounting status:** Evaluate risk rating, pooling or individual evaluation, collateral-dependent status, ACL measurement, nonaccrual, and any confirmed uncollectible portion under the applicable standards.
6. **Act operationally:** Tighten reporting, preserve collateral, control proceeds, consider restructuring or collection alternatives, and escalate exceptions without delaying loss recognition.

The decision may include continued collection, a workout, more collateral, a partial charge-off, or exit. The disciplined outcome is not a preferred tactic; it is alignment between current facts, legal rights, net recovery assumptions, accounting treatment, and operational action.

No Bitcoin or Galoy application is needed. This institutional credit-loss mechanism should stand on its own.

## What must not be confused

1. **Default versus loss:** default is a performance event; loss is the portion not ultimately recovered.
2. **Collateral versus repayment capacity:** collateral may reduce severity, but it does not automatically produce ordinary-course payment.
3. **Gross value versus net realizable recovery:** priority, liquidity, condition, delay, volatility, and realization costs can materially reduce proceeds.
4. **Secured versus collateral-dependent:** many healthy loans are secured; collateral-dependent is a defined reporting condition involving borrower financial difficulty and substantial reliance on collateral repayment.
5. **ACL versus cash:** the allowance is a valuation account, not segregated money.
6. **ACL versus capital:** the allowance and regulatory capital can interact under defined rules, but they are not the same loss-absorbing layer.
7. **Provision versus charge-off:** provision adjusts the loss estimate through income; charge-off removes an amount deemed uncollectible against the allowance.
8. **Charge-off versus forgiveness:** accounting removal does not by itself settle the legal debt or end collection.
9. **Charge-off versus recovery:** a required charge-off should not be postponed merely because later recovery is possible.
10. **Expected repayment versus expected credit loss:** underwriting asks how the borrower is expected to pay; CECL estimates the amount the institution does not expect to collect under the applicable accounting framework.

## Primary official sources

Use these as institutional anchors. This pack’s explanations and numerical cases are labeled simplifications, not legal, accounting, supervisory, valuation, tax, or credit advice.

1. **Office of the Comptroller of the Currency — Comptroller’s Handbook, “Allowances for Credit Losses,” Version 1.0 (April 2021; reputation-risk references updated March 2025).** Official supervisory treatment of CECL, ACL and provision mechanics, charge-offs and recoveries, collective and individual evaluation, collateral-dependent assets, forecasts, controls, and examiner review.  
   https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/allowances-for-credit-losses/pub-ch-allowances-credit-losses.pdf

2. **Federal Deposit Insurance Corporation — Risk Management Manual of Examination Policies, Section 3.2, “Loans” (March 2026).** Official examination material covering collateral valuation and administration, repayment ability, CECL, ACL changes, charge-offs, recoveries, collateral-dependent loans, classification, and lending controls.  
   https://www.fdic.gov/resources/supervision-and-examinations/examination-policies-manual/section3-2.pdf

3. **Office of the Comptroller of the Currency — Comptroller’s Handbook, “Rating Credit Risk” (April 2001; updated June 26, 2017 for nonaccrual status; reputation-risk references updated March 2025).** Official guidance defining substandard, doubtful, and loss classifications; discussing collateral-supported split ratings, partial charge-offs, and timely recognition of uncollectible amounts.  
   https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/rating-credit-risk/pub-ch-rating-credit-risk.pdf

4. **Federal Deposit Insurance Corporation — Interagency Policy Statement on Allowances for Credit Losses (Revised April 2023).** Joint agency policy statement on CECL governance, documentation, measurement, collateral-dependent financial assets, charge-offs, and supervisory expectations.  
   https://www.fdic.gov/news/financial-institution-letters/2023/fil23017.html

5. **Office of the Comptroller of the Currency — Comptroller’s Handbook, “Commercial Loans.”** Official examination material grounding the distinction between operating repayment capacity, collateral support, credit administration, monitoring, and problem-loan management.  
   https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/commercial-loans/pub-ch-commercial-loans.pdf

## Spaced retrieval prompts

Pause before answering each. Do not reveal an answer until the listener has attempted it.

1. **Retrieval from Day 006:** A borrower has valuable collateral but cannot demonstrate cash flow sufficient for scheduled debt service. Why does that weaken the underwriting thesis even if collateral may reduce the bank’s eventual loss?
2. A $1 million exposure has collateral with an $800,000 current fair value, $60,000 of selling costs, and a $100,000 senior claim. What is the simplified net collateral available, uncovered amount, and loss severity—and which facts would you verify before treating those figures as an accounting result?
3. In your own words, distinguish the ACL, provision expense, charge-off, and recovery. Why can a bank record provision expense before a specific loan is charged off, and why can it collect money after a charge-off?

## Voice memo request

Ask for a 60-to-90-second response containing all three:

- **Explanation:** Explain why collateral changes recovery and loss severity without automatically proving repayment capacity, then distinguish allowance, provision, charge-off, and recovery.
- **Application:** Apply the sequence to the equipment-dealer scenario: name the first collateral fact you would verify and the accounting or operational decision it could change.
- **Uncertainty:** State which legal, valuation, forecast, priority, or collectibility assumption you remain least certain about and how you would verify it.

Pause here and record a 60 to 90 second voice memo answering the retrieval questions.
