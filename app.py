import pandas as pd
import streamlit as st

from src.ingestion import clean_transactions, validate_required_columns
from src.analytics import (
    calculate_cash_flow_metrics,
    spending_by_category,
    monthly_burn_rate,
    generate_risk_alerts,
    liquidity_forecast,
    apply_what_if_expense,
    monthly_category_trends,
    cumulative_balance
)
from src.categorization import apply_auto_categorization

st.set_page_config(page_title="FinPredict", layout="wide")

st.title("FinPredict 💰")
st.write("Upload a transaction file to begin analyzing your spending and liquidity.")

st.sidebar.title("FinPredict")

st.sidebar.markdown(
    """
    Intelligent Expense Analytics &
    Liquidity Forecasting Platform
    """
)

st.sidebar.header("Data Upload")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        raw_df = pd.read_csv(uploaded_file)

        st.subheader("Raw Uploaded Data")
        st.dataframe(raw_df)

        cleaned_df = clean_transactions(raw_df)
        cleaned_df = apply_auto_categorization(cleaned_df)
        cleaned_df["category"] = cleaned_df["final_category"]
        missing_columns = validate_required_columns(cleaned_df)

        if missing_columns:
            st.error(
                f"Missing required columns after standardization: {', '.join(missing_columns)}"
            )
        else:
            st.subheader("Cleaned and Standardized Data")
            st.dataframe(cleaned_df)

            metrics = calculate_cash_flow_metrics(cleaned_df)

            st.subheader("Cash Flow Summary")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Income", f"${metrics['income']:,.2f}")
            col2.metric("Expenses", f"${metrics['expenses']:,.2f}")
            col3.metric("Net Cash Flow", f"${metrics['net_cash_flow']:,.2f}")
            col4.metric("Transactions", metrics["transaction_count"])

            ####### Spending by Category #######
            category_summary = spending_by_category(cleaned_df)
            st.subheader("Spending by Category")
            if category_summary.empty:
                st.info("No expense transactions found.")
            else:
                st.bar_chart(
                    category_summary,
                    x="category",
                    y="amount"
                )
                st.dataframe(category_summary)
            
            ####### Charts #######
            st.subheader("Spending Mix")
            if category_summary.empty:
                st.info("No expense data available for spending mix.")
            else:
                st.plotly_chart(
                    {
                        "data": [
                            {
                                "labels": category_summary["category"],
                                "values": category_summary["amount"],
                                "type": "pie",
                                "hole": 0.35,
                            }
                        ],
                        "layout": {
                            "title": "Expense Distribution by Category"
                        },
                    },
                    use_container_width=True,
                )

            monthly_category_df = monthly_category_trends(cleaned_df)

            st.subheader("Stacked Monthly Spending Trends")
            if monthly_category_df.empty:
                st.info("No expense data available for monthly category trends.")
            else:
                st.bar_chart(
                    monthly_category_df,
                    x="month",
                    y="expense_amount",
                    color="category",
                )
            ####### Burn Rate Analysis #######
            burn_rate_df = monthly_burn_rate(cleaned_df)
            st.subheader("Monthly Burn Rate")
            if burn_rate_df.empty:
                st.info("No expense transactions found for burn-rate analysis.")
            else:
                st.line_chart(burn_rate_df, x="month", y="burn_rate")
                st.dataframe(burn_rate_df)

            ####### Risk Alerts #######
            alerts = generate_risk_alerts(cleaned_df, metrics)
            st.subheader("Risk Alerts") 
            if alerts:
                for alert in alerts:
                    st.warning(alert)
            else:
                st.success("No financial risk alerts detected.")
            st.sidebar.divider()

            ####### Liquidity Forecast #######
            st.sidebar.header("Forecast Settings")
            st.subheader("Forecast Configuration")

            starting_balance = st.sidebar.number_input(
                "Current account balance",
                min_value=0.0,
                value=5000.0,
                step=100.0,
            )

            st.caption(
                "Forecasts are generated using historical average daily cash flow trends."
            )

            forecast_df = liquidity_forecast(
                cleaned_df,
                starting_balance=starting_balance,
            )
            st.subheader("30-Day Liquidity Forecast")
            st.line_chart(
                forecast_df,
                x="date",
                y="projected_balance"
            )
            st.dataframe(forecast_df)

            historical_balance_df = cumulative_balance(
                cleaned_df,
                starting_balance=starting_balance,
            )

            st.subheader("Historical Cumulative Balance")

            if historical_balance_df.empty:
                st.info("No transaction data available for cumulative balance.")
            else:
                st.line_chart(
                    historical_balance_df,
                    x="date",
                    y="cumulative_balance",
                )
            st.sidebar.divider()
            ####### What-If Scenario Analysis #######
            st.sidebar.header("What-If Scenario")
            expense_amount = st.sidebar.number_input(
                "Hypothetical expense amount",
                min_value=0.0,
                value=500.0,
                step=100.0,
            )
            expense_date = st.sidebar.date_input(
                "Hypothetical expense date",
                value=forecast_df["date"].min().date(),
            )
            scenario_df = apply_what_if_expense(
                forecast_df,
                expense_amount=expense_amount,
                expense_date=expense_date,
            )
            st.line_chart(
                scenario_df,
                x="date",
                y=["projected_balance", "scenario_balance"],
            )
            st.dataframe(scenario_df)

            st.success("File loaded successfully.")
    except Exception as e:
        st.error(f"Error reading file: {e}")