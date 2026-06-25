-- =====================================================
-- Query 1: Top 5 Funds by AUM
-- =====================================================

SELECT
    amfi_code,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- Query 2: Average NAV per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================================
-- Query 3: Total SIP Amount
-- =====================================================

SELECT
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP';


-- =====================================================
-- Query 4: Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;


-- =====================================================
-- Query 5: Funds with Expense Ratio Below 1%
-- =====================================================

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- Query 6: Average Return by Category
-- =====================================================

SELECT
    category,
    ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM fact_performance
GROUP BY category;


-- =====================================================
-- Query 7: Average Transaction Amount
-- =====================================================

SELECT
    ROUND(AVG(amount_inr),2) AS average_amount
FROM fact_transactions;


-- =====================================================
-- Query 8: Count of Funds by Risk Grade
-- =====================================================

SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;


-- =====================================================
-- Query 9: Top Fund Houses by Number of Schemes
-- =====================================================

SELECT
    fund_house,
    COUNT(*) AS schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY schemes DESC;


-- =====================================================
-- Query 10: Highest Sharpe Ratio Funds
-- =====================================================

SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;