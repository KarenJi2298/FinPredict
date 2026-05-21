import pandas as pd
import streamlit as st

from src.ingestion import clean_transactions, validate_required_columns
from src.analytics import (
    calculate_cash_flow_metrics,
    spending_by_category,
    monthly_burn_rate,
    generate_risk_alerts,
    liquidity_forecast
)
from src.categorization import apply_auto_categorization

st.set_page_config(page_title="FinPredict", layout="wide")

st.title("FinPredict 💰")
st.write("Upload a transaction file to begin analyzing your spending and liquidity.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

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

            ####### Liquidity Forecast #######
            forecast_df = liquidity_forecast(cleaned_df)
            st.subheader("30-Day Liquidity Forecast")
            st.line_chart(
                forecast_df,
                x="date",
                y="projected_balance"
            )
            st.dataframe(forecast_df)

            st.success("File loaded successfully.")
    except Exception as e:
        st.error(f"Error reading file: {e}")