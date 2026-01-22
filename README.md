# Real Estate PF Risk Analytics
## Liquidity Stress Testing & Capital Structure Analysis (£12.7M GDV)

This repository presents a **quantitative liquidity risk analysis** for a highly leveraged real estate development project, applying informatics-based financial modelling to identify structural weaknesses in project finance (PF) and support data-driven capital structure decisions.

---

## Currency Note
All GBP figures are indicative conversions from KRW using an approximate spot rate
(**£1 ≈ ₩1,970**) for analytical consistency.
All core modelling and assumptions are performed in KRW.

---

## 1. Transaction Overview – Capital Stack

The project involves a commercial parking tower development facing a significant funding gap and liquidity risk due to aggressive gearing and a timing mismatch in regional infrastructure.

| Category | Value (KRW) | Value (GBP) | Notes |
| :--- | :--- | :--- | :--- |
| **Appraisal Value** | ₩19.0B | ~£9.65M | Current asset valuation |
| **Equity Capital** | ₩5.7B | ~£2.90M | ~23% of total project cost |
| **Target Debt (PF)** | ₩19B – ₩23B | ~£9.65M – £11.69M | Senior / Mezzanine financing |
| **Implied LTV** | 100% – 121% | 100% – 121% | **Primary structural risk** |
| **Debt / Equity Multiple** | ~3.3x – 4.0x | ~3.3x – 4.0x | High leverage profile |
| **Gross Development Value (GDV)** | ~₩25.0B | ~£12.70M | Stabilised value assumption |

---

## 2. Core Investment Issue – Structural Liquidity Gap

A critical **14-month timing mismatch** exists between:

- **Asset completion:** January 2027
- **Opening of primary demand driver (District Court):** March 2028

During this period, the project experiences a **Negative Carry** profile:

- Continuous accrual of high-cost debt
- Progressive erosion of the equity buffer
- Contracted and projected operating income partially offsets financing costs; however, Net Operating Income remains insufficient to cover debt service during the pre-stabilisation period

Under the current financing structure, liquidity risk is driven not by asset quality, but by **capital structure and timing misalignment**.

---

## 3. Analytical Approach & Methodology

Leveraging an informatics background, I developed a **Python-based cash flow simulation framework** to evaluate downside scenarios beyond static spreadsheet models.

Key components include:

- **Monthly Cash Flow Modelling:**
  Integrated debt terms, interest rates, operating assumptions, and vacancy periods.
- **Scenario-Based Stress Testing:**
  Evaluated DSCR sensitivity across a wide range of occupancy, interest rate, and delay assumptions using Monte Carlo–style simulations.
- **Liquidity Runway Analysis:**
  Quantified the equity exhaustion point under prolonged vacancy and adverse rate environments.

This approach enabled explicit identification of the time threshold at which the project transitions from illiquid to insolvent.

---

## 4. Key Risk Findings (Base Case)

- **Effective Financing Cost:** High single-digit annual rate
- **Monthly Interest Burn:** Material relative to equity base
- **DSCR:** < 1.0 throughout the pre-stabilisation period, even after accounting for contracted income
- **Equity Role:** Functions primarily as an interest carry buffer rather than downside protection

The analysis demonstrates that modest schedule delays materially increase the probability of **equity wipeout** under a lease-only stabilisation strategy.

---

## 5. Strategic Recommendations – Capital Structure Intervention

Based on the quantified downside risk, the analysis supported a shift from a passive hold-and-lease approach to an active **de-risking strategy**:

1. **Strategic Pre-Sales:**
   Partial disposal of upper commercial units to achieve meaningful debt paydown, reducing interest burden and leverage.
2. **Liquidity Buffer Requirement:**
   Identification of a minimum additional liquidity reserve required to bridge the 14-month negative carry period.
3. **Refinancing Roadmap:**
   Establishment of a data-backed timeline for transitioning to lower-cost term debt upon activation of demand drivers.

These measures aim to realign leverage with conventional bankability thresholds (sub-80% LTV range) and stabilise cash flow prior to refinancing.

---

## 6. Illustrative Code Sample – Equity Runway

```python
# Simplified equity runway illustration (base-case assumptions)
# Currency shown in GBP for presentation purposes

def calculate_runway(equity, monthly_burn, months_to_opening):
    remaining_equity = equity - (monthly_burn * months_to_opening)
    if remaining_equity < 0:
        return "Insolvent"
    return f"Remaining Buffer: £{remaining_equity:,.2f}"

# Example: £2.90M equity, ~£52k monthly burn, 14-month vacancy
print(calculate_runway(2_900_000, 52_000, 14))
```

---

## 7. Skills Demonstrated

- Real estate project finance (PF) risk analysis
- Liquidity and downside-case modelling
- Capital structure and leverage assessment
- Python financial modelling (`Pandas`, `NumPy`, `Matplotlib`)
- Translation of quantitative risk into executive-level decision support

---

## 8. Key Takeaway

In highly leveraged development projects, **timing risk can be more destructive than market risk**.
This analysis demonstrates how modest schedule delays, when combined with aggressive leverage, can rapidly convert a completed asset into a liquidity liability.

Proactive capital structure stress-testing enables earlier intervention and materially improves downside protection before value impairment becomes irreversible.