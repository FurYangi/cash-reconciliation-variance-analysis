-- Schema (SQLite/PostgreSQL compatible)
CREATE TABLE pos_transactions (
      date DATE,
      shift TEXT,
      cashier TEXT,
      expected_cash NUMERIC,
      actual_cash NUMERIC,
      variance NUMERIC
);

-- 1. Flag shifts with a variance beyond the $10 materiality threshold
SELECT
  date,
  shift,
  cashier,
  variance
FROM pos_transactions
WHERE ABS(variance) > 10
ORDER BY ABS(variance) DESC;

-- 2. Total and average variance by cashier
SELECT
  cashier,
COUNT(*) AS shifts_worked,
ROUND(SUM(variance), 2) AS total_variance,
ROUND(AVG(variance), 2) AS avg_variance,
SUM(CASE WHEN ABS(variance) > 10 THEN 1 ELSE 0 END) AS flagged_shifts
FROM pos_transactions
GROUP BY cashier
ORDER BY total_variance ASC;

-- 3. Variance by shift type (Morning vs Evening)
SELECT
  shift,
ROUND(AVG(variance), 2) AS avg_variance,
ROUND(SUM(variance), 2) AS total_variance,
COUNT(*) AS shifts
FROM pos_transactions
GROUP BY shift;

-- 4. Running cumulative variance over time (window function)
  SELECT
    date,
    shift,
    cashier,
    variance,
  ROUND(SUM(variance) OVER (ORDER BY date, shift), 2) AS running_variance
  FROM pos_transactions
  ORDER BY date, shift;

  -- 5. Rank cashiers by average variance magnitude (window function)
    SELECT
      cashier,
    ROUND(AVG(ABS(variance)), 2) AS avg_abs_variance,
    RANK() OVER (ORDER BY AVG(ABS(variance)) DESC) AS variance_rank
    FROM pos_transactions
    GROUP BY cashier;
