# NotebookLM Source Pack — Banking Fluency Day 002

## Episode

**Banking Fluency for Bitcoin-Age Operators — Day 002: Deposits Are Liabilities**

## Course purpose

This course builds regulated-financial-institution fluency before applying it to Bitcoin or Galoy. The learner is preparing for possible marketing, business-development, or AI-operator work around bank and credit-union infrastructure.

Day 002 develops the balance-sheet perspective introduced in Day 001. The essential shift is:

> A deposit is an asset to the customer and a liability to the institution.

Pronunciation note for audio: **Galoy is pronounced “gah-LOY.”** Use the company name sparingly and pronounce it correctly.

## Audio style instruction

Create a polished, conversational, rigorous educational podcast—not a dry reading. Use concrete ledger examples and correct common misconceptions. Let the two hosts test each other’s understanding. Do not use hype or pretend that all money-like products are deposits.

Desired structure:

1. Cold open: the same $1,000 is an asset to one party and a liability to another.
2. Walk through a simple deposit accounting entry.
3. Explain what the bank owes the customer.
4. Connect deposits to funding and liquidity.
5. Correct the “bank lends out your exact dollars” story.
6. Explain carefully how lending commonly creates deposits while remaining constrained.
7. Explain deposit insurance without implying that every product offered by a bank is insured.
8. Apply the distinction to Bitcoin, custody, stablecoins, payments, and Galoy-style infrastructure.
9. End with the exact reflection question.

## Primary lesson text

Suppose a customer places $1,000 in a checking account.

From the customer’s perspective, the balance is an asset. The customer can use it to make payments, withdraw cash, or transfer funds. Economically and legally, the customer holds a claim against the institution.

From the bank’s perspective, the same balance is a liability. The bank’s ledger says: “We owe this customer $1,000 according to the account terms.” The Federal Reserve’s H.8 release reflects this directly by listing deposits under commercial-bank liabilities.

If the customer deposits physical cash, a simplified balance-sheet entry is:

- Bank asset: cash increases by $1,000.
- Bank liability: customer deposits increase by $1,000.

If the deposit arrives by transfer from another institution, the receiving bank may gain settlement or reserve assets and record the new customer deposit liability. The exact plumbing differs, but the customer balance remains an obligation of the institution.

This liability provides funding. The institution can hold liquid assets, purchase securities, make loans, and settle payments. But it must be able to honor withdrawals and transfers when due. That creates liquidity-management obligations.

Do not imagine the bank labeling a depositor’s dollars and passing those exact dollars to a particular borrower. Banks manage a portfolio of assets and liabilities. When a bank makes a loan, it commonly records:

- Bank asset: a loan receivable increases.
- Bank liability: a deposit account is credited.

In this sense, bank lending commonly creates deposits. That does not make lending unlimited. Capital and liquidity requirements, funding conditions, credit risk, regulation, supervision, profitability, payment outflows, and the availability of creditworthy borrowers all constrain the process. These constraints interact; avoid describing any one constraint as an instantaneous or absolute ceiling.

Deposits are not all equally stable. Transaction accounts, savings accounts, and time deposits have different terms and behavior. Some customer relationships are durable; other balances are rate-sensitive, concentrated, uninsured, or able to move quickly. The institution must understand how its deposit liabilities may behave during normal periods and stress.

Deposit insurance supports public confidence, but precision matters. In the United States, eligible deposits at FDIC-insured banks are protected within applicable insurance limits and ownership categories. Federally insured credit unions have a parallel framework through the National Credit Union Share Insurance Fund administered by NCUA.

Not every product offered by a bank or credit union is a deposit. Securities, mutual funds, cryptoassets, custodial holdings, and other non-deposit products do not become insured deposits merely because the customer accesses them through the institution.

That distinction is central to Bitcoin banking infrastructure. A financial app may display a dollar amount, Bitcoin balance, collateral value, stablecoin balance, or pending payment. The interface does not determine the legal category. The institution must define:

- Who owes what to whom?
- What ledger is authoritative?
- Is the customer’s claim a deposit, custodial entitlement, claim on an issuer, or payment instruction?
- Is the value insured, safeguarded, segregated, collateralized, or exposed to market risk?
- How is every balance reconciled?
- What happens during an outage, failed transfer, insolvency, or disputed transaction?

For a bank-facing vendor, category clarity is part of product credibility. Software cannot blur the difference between an insured deposit liability and a non-deposit digital asset while expecting compliance, risk, audit, and examiners to clean it up later.

## Key concepts to explain

### Deposit liability

The institution’s obligation to repay or make available the customer’s money under the account terms.

### Customer asset

The customer’s claim against the institution. One party’s financial asset is often another party’s liability.

### Funding

The liabilities and capital supporting the institution’s assets. Deposits are typically an important source of bank and credit-union funding.

### Liquidity

The capacity to meet withdrawals, transfers, and other cash obligations when due without unacceptable losses.

### Deposit insurance

Protection for eligible deposits if an insured institution fails, subject to legal limits and account-ownership rules. It is not blanket protection for every product available through a financial institution.

### Reconciliation

Proving that transaction records, customer balances, settlement accounts, and the general ledger agree—or identifying and correcting differences.

## Institutional buyer lens

A regulated institution evaluating technology that touches balances will ask:

- What is the system of record?
- Which legal entity owes the customer?
- Is this an insured deposit or a non-deposit product?
- Can every transaction and balance be reconciled?
- What are the liquidity and settlement implications?
- What happens when a transfer fails, reverses, or remains pending?
- Can compliance, auditors, the board, and examiners understand the arrangement?
- What happens if the vendor or network goes down?

## Galoy / Bitcoin lens

For Galoy-style products, “money in the app” is not a sufficient description.

Bitcoin might be:

- held in custody;
- used as collateral;
- moved as part of a payment service;
- used as a settlement asset;
- exposed through an exchange or brokerage arrangement.

It is not automatically an insured dollar deposit. Bitcoin itself, a custodial Bitcoin entitlement, and an FDIC-insured dollar deposit are different legal and accounting categories. A credible regulated-institution product maps the customer experience to the underlying legal claim, ledger, custody model, disclosures, controls, reconciliation, and insurance status.

## Source links

1. Federal Reserve Board — Assets and Liabilities of Commercial Banks in the United States, H.8  
   https://www.federalreserve.gov/releases/h8/current/default.htm

2. FDIC — Understanding Deposit Insurance  
   https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance

3. Federal Reserve Education — Banking Basics  
   https://www.federalreserveeducation.org/teaching-resources/personal-finance/saving/banking-basics

4. Federal Reserve Bank of Boston — Banking Basics  
   https://www.bostonfed.org/publications/economic-education/banking-basics.aspx

5. Bank of England — Money Creation in the Modern Economy  
   https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy

6. Galoy — Solutions  
   https://galoy.io/solutions

## Reflection question

End the episode with this exact question:

> If a customer sees “$1,000” in a financial app, what questions must an institution answer before calling that balance a deposit?
