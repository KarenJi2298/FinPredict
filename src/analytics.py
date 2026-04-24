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