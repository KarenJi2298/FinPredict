import pandas as pd


CATEGORY_RULES = {
    "Income": [
        "paycheck",
        "payroll",
        "salary",
        "direct deposit",
        "deposit",
    ],
    "Housing": [
        "rent",
        "mortgage",
        "apartment",
        "lease",
    ],
    "Groceries": [
        "trader joe",
        "whole foods",
        "costco",
        "walmart",
        "target",
        "grocery",
        "market",
    ],
    "Dining": [
        "restaurant",
        "cafe",
        "coffee",
        "starbucks",
        "doordash",
        "ubereats",
        "grubhub",
    ],
    "Transportation": [
        "uber",
        "lyft",
        "mta",
        "nj transit",
        "gas",
        "parking",
        "toll",
    ],
    "Entertainment": [
        "netflix",
        "spotify",
        "hulu",
        "movie",
        "cinema",
    ],
    "Debt Service": [
        "loan",
        "credit card",
        "amex",
        "chase",
        "capital one",
        "minimum payment",
    ],
    "Utilities": [
        "electric",
        "gas bill",
        "water",
        "internet",
        "verizon",
        "comcast",
        "utility",
    ],
}


def categorize_transaction(description: str, amount: float) -> str:
    description = str(description).lower()

    for category, keywords in CATEGORY_RULES.items():
        for keyword in keywords:
            if keyword in description:
                return category

    if amount > 0:
        return "Income"

    return "Uncategorized"


def apply_auto_categorization(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "category" not in df.columns:
        df["category"] = ""

    df["category"] = df["category"].fillna("").astype(str)

    df["auto_category"] = df.apply(
        lambda row: categorize_transaction(row["description"], row["amount"]),
        axis=1,
    )

    df["final_category"] = df["category"].copy()

    missing_category = df["final_category"].str.strip().eq("")

    df.loc[missing_category, "final_category"] = df.loc[
        missing_category, "auto_category"
    ]

    return df