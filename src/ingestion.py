import pandas as pd


STANDARD_COLUMN_MAP = {
    "date": "date",
    "transaction date": "date",
    "posted date": "date",
    "amount": "amount",
    "transaction amount": "amount",
    "debit": "amount",
    "credit": "amount",
    "description": "description",
    "details": "description",
    "merchant": "description",
    "category": "category",
}


def normalize_column_name(column_name: str) -> str:
    return column_name.strip().lower()


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    renamed_columns = {}

    for col in df.columns:
        normalized = normalize_column_name(col)
        if normalized in STANDARD_COLUMN_MAP:
            renamed_columns[col] = STANDARD_COLUMN_MAP[normalized]

    df = df.rename(columns=renamed_columns)
    return df


def validate_required_columns(df: pd.DataFrame) -> list[str]:
    required = ["date", "amount", "description"]
    missing = [col for col in required if col not in df.columns]
    return missing


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_columns(df)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    if "description" in df.columns:
        df["description"] = df["description"].astype(str).str.strip()

    return df