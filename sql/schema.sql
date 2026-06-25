-- ===========================
-- DIMENSION TABLE: FUND
-- ===========================

CREATE TABLE IF NOT EXISTS dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,
    fund_house TEXT,

    category TEXT,
    sub_category TEXT,

    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    expense_ratio_pct REAL,

    exit_load_pct REAL,

    min_sip_amount INTEGER,
    min_lumpsum_amount INTEGER,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT
);



-- ===========================
-- DIMENSION TABLE: DATE
-- ===========================

CREATE TABLE IF NOT EXISTS dim_date (

    date_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date DATE UNIQUE,

    year INTEGER,
    month INTEGER,
    day INTEGER,

    quarter INTEGER,

    weekday TEXT
);




-- ===========================
-- FACT TABLE: NAV
-- ===========================

CREATE TABLE IF NOT EXISTS fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date DATE,

    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);





-- ===========================
-- FACT TABLE: TRANSACTIONS
-- ===========================

CREATE TABLE IF NOT EXISTS fact_transactions (

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,
    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);






-- ===========================
-- FACT TABLE: PERFORMANCE
-- ===========================

CREATE TABLE IF NOT EXISTS fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,
    beta REAL,

    sharpe_ratio REAL,
    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER,

    risk_grade INTEGER,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);






-- ===========================
-- FACT TABLE: AUM
-- ===========================

CREATE TABLE IF NOT EXISTS fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date DATE,

    fund_house TEXT,

    aum_lakh_crore REAL,

    aum_crore REAL,

    num_schemes INTEGER
);

