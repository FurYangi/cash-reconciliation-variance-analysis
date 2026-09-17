# Cash Reconciliation & Sales Variance Analysis

End-to-end cash-handling analysis project: reconciling expected vs. actual cash drawer totals across POS shifts, flagging discrepancies, and surfacing patterns by cashier and shift using SQL and Python.

## Project Overview

Retail and food-service businesses close out every shift by reconciling the cash drawer against the point-of-sale system's expected total. Small discrepancies are normal, but consistent or large ones can point to training gaps, process breakdowns, or theft. This project simulates that reconciliation workflow: loading shift-level POS data, computing variances, flagging shifts that need review, and summarizing patterns by cashier and shift type.

Business questions addressed: which shifts and cashiers have the largest or most frequent cash variances, whether there's a pattern by shift (morning vs. evening), and how much unexplained variance accumulated over the period.

## Tech Stack

| Area | Tools |
|---|---|
| Data querying | SQL (PostgreSQL/SQLite) |
| Data analysis | Python, Pandas |
| Environment | Jupyter Notebook |
| Version control | Git & GitHub |

## Dataset

`data/pos_transactions.csv` is a sample of 60 shifts (30 days, 2 shifts/day), each with expected cash from the POS system and actual cash counted. Generated to resemble real POS reconciliation records.

## Repository Structure

```
cash-reconciliation-variance-analysis/
  data/
    pos_transactions.csv       (sample shift-level reconciliation data)
  notebooks/
    reconciliation_analysis.py (variance calculation and summary analysis)
  sql/
    variance_queries.sql       (flagging and aggregation queries)
  requirements.txt
  README.md
```

## Methodology

**Data preparation.** Each row represents one shift: date, shift (Morning/Evening), cashier, expected cash from the POS system, and actual cash counted.

**Variance calculation.** variance = actual_cash - expected_cash, computed per shift.

**Flagging.** Shifts with an absolute variance greater than $10 are flagged for review, based on a materiality threshold common in cash-handling policies.

**Aggregation.** Variances are summarized by cashier and by shift type to spot systematic patterns rather than one-off errors.

## Key Insights (Sample)

Across 60 sample shifts, the average variance was -$5.06 per shift, with a cumulative shortfall of -$303.70 over the period. 13 of 60 shifts (21.7%) were flagged under the $10 materiality threshold. Variance was not evenly distributed by cashier, which is a fast way to tell a systemic issue from an individual one. Morning shifts averaged a larger variance (-$6.45) than evening shifts (-$3.67) in this sample.

(Sample data is synthetic, generated to resemble real POS reconciliation records; see `data/pos_transactions.csv`.)

## Skills Demonstrated

Writing SQL for aggregation, flagging, and window functions (running totals, ranking). Data cleaning and analysis with Pandas. Variance analysis and materiality-based flagging. Translating operational data into a management-ready summary.

## How to Use

**Clone the repository:**

```
git clone https://github.com/FurYangi/cash-reconciliation-variance-analysis.git
cd cash-reconciliation-variance-analysis
```

**Install dependencies:**

```
pip install -r requirements.txt
```

**Run the analysis:**

```
python notebooks/reconciliation_analysis.py
```

Explore the SQL queries in `sql/variance_queries.sql` against the same data loaded into SQLite or PostgreSQL.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
