import pandas as pd
from datetime import timedelta


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

def generate_risk_alerts(df: pd.DataFrame, metrics: dict) -> list[str]:
    alerts = []
    if metrics["net_cash_flow"] < 0:
        alerts.append(
            "Negative cash flow detected. Expenses exceed income."
        )
    if metrics["expenses"] > metrics["income"] * 0.8:
        alerts.append(
            "High expense ratio detected. Spending exceeds 80% of income."
        )
    discretionary_categories = [
        "Dining",
        "Entertainment",
    ]
    discretionary_spending = df.loc[
        df["category"].isin(discretionary_categories)
        & (df["amount"] < 0),
        "amount"
    ].abs().sum()
    if discretionary_spending > metrics["income"] * 0.3:
        alerts.append(
            "High discretionary spending detected."
        )
    return alerts

def liquidity_forecast(df: pd.DataFrame, forecast_days: int = 30) -> pd.DataFrame:
    forecast_df = df.copy()
    daily_cash_flow = (
        forecast_df.groupby("date", as_index=False)["amount"]
        .sum()
        .sort_values("date")
    )
    average_daily_cash_flow = daily_cash_flow["amount"].mean()
    latest_date = daily_cash_flow["date"].max()
    current_balance = daily_cash_flow["amount"].sum()
    future_rows = []
    projected_balance = current_balance
    for i in range(1, forecast_days + 1):
        future_date = latest_date + timedelta(days=i)
        projected_balance += average_daily_cash_flow
        future_rows.append({
            "date": future_date,
            "projected_balance": projected_balance,
        })
    future_df = pd.DataFrame(future_rows)
    return future_df

def apply_what_if_expense(
    forecast_df: pd.DataFrame,
    expense_amount: float,
    expense_date,
) -> pd.DataFrame:
    scenario_df = forecast_df.copy()
    scenario_df["scenario_balance"] = scenario_df["projected_balance"]
    scenario_df.loc[
        scenario_df["date"] >= pd.to_datetime(expense_date),
        "scenario_balance",
    ] = (
        scenario_df.loc[
            scenario_df["date"] >= pd.to_datetime(expense_date),
            "scenario_balance",
        ]
        - expense_amount
    )
    return scenario_df