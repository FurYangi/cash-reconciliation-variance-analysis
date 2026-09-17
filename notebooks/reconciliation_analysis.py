"""
Cash Reconciliation & Sales Variance Analysis
Loads shift-level POS data, computes variances, flags shifts for review,
and summarizes patterns by cashier and shift type.
"""

import pandas as pd

FLAG_THRESHOLD = 10.00


def load_data(path="../data/pos_transactions.csv"):
  df = pd.read_csv(path, parse_dates=["date"])
  return df

def compute_variance(df):
  df["variance"] = (df["actual_cash"] - df["expected_cash"]).round(2)
  df["flagged"] = df["variance"].abs() > FLAG_THRESHOLD
  return df

def summarize_by_cashier(df):
  summary = df.groupby("cashier").agg(
    shifts_worked=("variance", "count"),
    total_variance=("variance", "sum"),
    avg_variance=("variance", "mean"),
    flagged_shifts=("flagged", "sum"),
  )
  return summary.round(2).sort_values("total_variance")

def summarize_by_shift(df):
  summary = df.groupby("shift").agg(
    avg_variance=("variance", "mean"),
    total_variance=("variance", "sum"),
    shifts=("variance", "count"),
  )
  return summary.round(2)

def main():
  df = load_data()
  df = compute_variance(df)
  flagged_count = df["flagged"].sum()
  flagged_pct = 100 * df["flagged"].mean()
  print("=== Overall Summary ===")
  print(f"Total shifts: {len(df)}")
  print(f"Average variance per shift: ${df['variance'].mean():.2f}")
  print(f"Cumulative variance: ${df['variance'].sum():.2f}")
  print(f"Flagged shifts (over ${FLAG_THRESHOLD}): {flagged_count} ({flagged_pct:.1f}%)")
  print()
  print("=== By Cashier ===")
  print(summarize_by_cashier(df))
  print()
  print("=== By Shift ===")
  print(summarize_by_shift(df))
  print()
  print("=== Largest Shortfalls ===")
  print(df.nsmallest(5, "variance")[["date", "shift", "cashier", "variance"]])

main()
