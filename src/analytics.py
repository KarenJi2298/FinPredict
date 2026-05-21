import pandas as pd


def calculate_cash_flow_metrics(df: pd.DataFrame) -> dict:
    income = df.loc[df["amount"] > 0, "amount"].sum()
    expenses = df.loc[df["amount"] < 0, "amount"].sum()
    net_cash_flow = income + expenses

    return {
        "income": income,
        "expenses": abs(expenses),
        "net_cash_flow": net_cash_flow,
        "transaction_count": len(df),
    }

def spending_by_category(df: pd.DataFrame) -> pd.DataFrame:
    expenses = df[df["amount"] < 0].copy()
    category_summary = (
        expenses.groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount")
    )
    category_summary["amount"] = category_summary["amount"].abs()
    return category_summary

def monthly_burn_rate(df: pd.DataFrame) -> pd.DataFrame:
    expenses = df[df["amount"] < 0].copy()

    expenses["month"] = expenses["date"].dt.to_period("M").astype(str)

    monthly_summary = (
        expenses.groupby("month", as_index=False)["amount"]
        .sum()
        .sort_values("month")
    )

    monthly_summary["burn_rate"] = monthly_summary["amount"].abs()

    return monthly_summary[["month", "burn_rate"]]