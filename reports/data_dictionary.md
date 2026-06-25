# Data Dictionary

## 1. dim_fund

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct or Regular |
| launch_date | DATE | Launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio (%) |
| exit_load_pct | REAL | Exit load (%) |
| min_sip_amount | INTEGER | Minimum SIP |
| min_lumpsum_amount | INTEGER | Minimum lump sum |
| fund_manager | TEXT | Fund manager |
| risk_category | TEXT | Risk category |
| sebi_category_code | TEXT | SEBI category code |

---

## 2. fact_nav

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## 3. fact_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Scheme code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier of city |
| age_group | TEXT | Investor age group |
| gender | TEXT | Gender |
| annual_income_lakh | REAL | Annual income (Lakhs) |
| payment_mode | TEXT | Payment mode |
| kyc_status | TEXT | KYC verification status |

---

## 4. fact_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme code |
| return_1yr_pct | REAL | 1-year return |
| return_3yr_pct | REAL | 3-year return |
| return_5yr_pct | REAL | 5-year return |
| benchmark_3yr_pct | REAL | Benchmark return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown |
| aum_crore | REAL | Assets Under Management |
| expense_ratio_pct | REAL | Expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk grade |

---

## 5. fact_aum

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | DATE | Reporting month |
| fund_house | TEXT | Fund house |
| aum_crore | REAL | Assets under management |
| num_schemes | INTEGER | Number of schemes |