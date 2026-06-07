Software Test Plan and Test Environment Report
Project: FinPredict – Intelligent Expense Analytics & Liquidity Forecasting
Students: Zekun Ji & Huihai Jiang
Course: CISC 594

1. Introduction
FinPredict is a Streamlit-based financial analytics application designed to help users upload transaction data, analyze spending behavior, categorize expenses, evaluate burn rate, forecast liquidity, and simulate hypothetical future expenses. The project was developed in two planned versions: Version 1 focuses on data ingestion, categorization, and analytics, while Version 2 adds predictive forecasting, risk alerts, and what-if simulation. These versions follow the project structure and feature plan described in the original proposal. 
 
2. Testing Methodology
The system-level test cases were selected using a combination of functional coverage, risk-based testing, and user workflow testing. Since FinPredict is an interactive financial analytics application, the test cases focus on the major actions a user would perform from start to finish.
The selected test cases cover:
1.	Data ingestion and validation
Ensures the application can accept transaction files and detect missing or invalid fields.
2.	Data cleaning and standardization
Verifies that different column names are converted into the internal schema.
3.	Transaction categorization
Confirms that transactions are classified into meaningful categories.
4.	Dashboard analytics
Tests cash flow summaries, spending by category, burn-rate trends, and visualizations.
5.	Forecasting and simulation
Validates projected liquidity calculations and what-if scenario adjustments.
6.	Risk alerts
Ensures the system identifies negative cash flow, high expense ratios, and discretionary spending risks.
These tests provide adequate coverage because they exercise the full system workflow from file upload through final dashboard output. They also cover normal cases, missing data cases, invalid input cases, and scenario-based cases.
 
3. Version 1 System Test Plan
Version 1: Analytical Foundation
Version 1 includes transaction upload, data cleaning, schema standardization, automated categorization, cash flow metrics, spending by category, and burn-rate analytics.
 
Test Case V1-TC1: Upload Valid CSV File
Field	Description
Test Objective	Verify that the system can upload and read a valid CSV transaction file.
Preconditions	Application is running through Streamlit. A valid CSV file is available.
Test Data	CSV file containing Transaction Date, Amount, Description, and Category columns.
Step No.	Test Step Description	Expected Result	Actual Result
1	Open the FinPredict Streamlit application.	Application loads successfully.	Passed
2	Click the file uploader.	File selection window appears.	Passed
3	Upload a valid CSV transaction file.	File is accepted by the application.	Passed
4	Review the raw data preview.	Raw uploaded data is displayed in a table.	Passed
5	Review the cleaned data preview.	Cleaned and standardized data is displayed.	Passed
Test Status: Passed
 
Test Case V1-TC2: Validate Required Columns
Field	Description
Test Objective	Verify that the system detects missing required columns.
Preconditions	Application is running.
Test Data	CSV file missing the Amount column.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload a CSV file missing the Amount column.	System reads the file but identifies missing required field.	Passed
2	Review the application message.	Error message displays missing required column.	Passed
3	Confirm dashboard does not generate incorrect metrics.	Metrics are not calculated from invalid data.	Passed
Test Status: Passed
 
Test Case V1-TC3: Standardize Column Names
Field	Description
Test Objective	Verify that alternate column names are mapped to the internal schema.
Preconditions	Application is running.
Test Data	CSV file using “Transaction Date” instead of “date.”
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload CSV with alternate column names.	File uploads successfully.	Passed
2	Run ingestion process.	Columns are renamed to date, amount, description, and category.	Passed
3	Review cleaned dataframe.	Standardized column names appear correctly.	Passed
Test Status: Passed
 
Test Case V1-TC4: Automatic Transaction Categorization
Field	Description
Test Objective	Verify that uncategorized transactions are automatically classified.
Preconditions	Application is running and categorization rules are implemented.
Test Data	CSV file with blank Category values for Trader Joe’s, Rent, Paycheck, Netflix, Starbucks, NJ Transit, and Capital One Credit Card.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload CSV with blank category fields.	File uploads successfully.	Passed
2	Run categorization logic.	System assigns categories based on description keywords.	Passed
3	Review cleaned data table.	Categories are filled correctly.	Passed
4	Confirm unknown merchants remain Uncategorized.	Unknown descriptions are not incorrectly forced into known categories.	Passed
Test Status: Passed
 
Test Case V1-TC5: Cash Flow Summary Metrics
Field	Description
Test Objective	Verify that income, expenses, net cash flow, and transaction count are calculated correctly.
Preconditions	Valid transaction file is uploaded.
Test Data	Sample CSV with positive paycheck and negative expense transactions.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload sample transaction file.	File loads successfully.	Passed
2	Review Income metric.	Positive transactions are summed correctly.	Passed
3	Review Expenses metric.	Negative transactions are summed as absolute expenses.	Passed
4	Review Net Cash Flow metric.	Income minus expenses is calculated correctly.	Passed
5	Review Transaction Count.	Total number of rows is displayed correctly.	Passed
Test Status: Passed
 
Test Case V1-TC6: Spending by Category Chart
Field	Description
Test Objective	Verify that expenses are grouped and visualized by category.
Preconditions	Valid categorized data is available.
Test Data	Transactions containing Housing, Groceries, Dining, Entertainment, and Transportation expenses.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload categorized transaction file.	File loads successfully.	Passed
2	Navigate to Spending by Category section.	Bar chart appears.	Passed
3	Review category totals.	Expense totals match expected grouped amounts.	Passed
4	Review spending mix pie chart.	Expense distribution is shown by category.	Passed
Test Status: Passed
 
Test Case V1-TC7: Monthly Burn-Rate Analytics
Field	Description
Test Objective	Verify monthly burn-rate calculation and visualization.
Preconditions	Transaction file includes expenses across multiple months.
Test Data	April, May, and June transaction data.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload multi-month transaction file.	File loads successfully.	Passed
2	Review Monthly Burn Rate chart.	Monthly expense totals are displayed as a trend.	Passed
3	Review monthly burn-rate table.	Monthly totals match the uploaded data.	Passed
Test Status: Passed
 
4. Version 2 System Test Plan
Version 2: Predictive Intelligence
Version 2 includes liquidity forecasting, what-if simulation, risk alerts, cumulative balance tracking, and enhanced dashboard visualizations.
 
Test Case V2-TC1: Starting Balance Input
Field	Description
Test Objective	Verify that the user can enter a current account balance for forecasting.
Preconditions	Valid transaction file is uploaded.
Test Data	Starting balance of $5,000.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload valid transaction file.	File loads successfully.	Passed
2	Enter $5,000 as current account balance.	Input is accepted.	Passed
3	Generate liquidity forecast.	Forecast begins from the entered balance.	Passed
Test Status: Passed
 
Test Case V2-TC2: 30-Day Liquidity Forecast
Field	Description
Test Objective	Verify that the application generates a 30-day projected balance.
Preconditions	Valid transaction data and starting balance are available.
Test Data	Transaction file with daily income and expenses.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload valid transaction file.	Data is loaded and cleaned.	Passed
2	Enter starting balance.	Balance input is accepted.	Passed
3	Review 30-day forecast chart.	Projected balance is displayed over 30 future days.	Passed
4	Review forecast dataframe.	Forecast table includes date and projected balance.	Passed
Test Status: Passed
 
Test Case V2-TC3: What-If Expense Simulation
Field	Description
Test Objective	Verify that hypothetical future expenses adjust the projected balance.
Preconditions	Forecast has been generated.
Test Data	Hypothetical expense of $1,000 on the first forecast date.
Step No.	Test Step Description	Expected Result	Actual Result
1	Enter hypothetical expense amount of $1,000.	Input is accepted.	Passed
2	Select expense date.	Date input is accepted.	Passed
3	Review scenario chart.	Scenario balance line drops by $1,000 from selected date onward.	Passed
4	Review scenario dataframe.	Scenario balance reflects expense adjustment.	Passed
Test Status: Passed
 
Test Case V2-TC4: Risk Alert for Negative Cash Flow
Field	Description
Test Objective	Verify that the system warns users when expenses exceed income.
Preconditions	Application is running.
Test Data	CSV with income of $2,500 and expenses greater than $2,500.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload risky transaction file.	File loads successfully.	Passed
2	Review cash flow metrics.	Net cash flow is negative.	Passed
3	Review Risk Alerts section.	Warning appears for negative cash flow.	Passed
Test Status: Passed
 
Test Case V2-TC5: Risk Alert for High Expense Ratio
Field	Description
Test Objective	Verify that the system flags high expenses relative to income.
Preconditions	Application is running.
Test Data	CSV where total expenses exceed 80% of income.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload transaction file with high expenses.	File loads successfully.	Passed
2	Review calculated expenses and income.	Expense ratio exceeds threshold.	Passed
3	Review Risk Alerts section.	High expense ratio warning appears.	Passed
Test Status: Passed
 
Test Case V2-TC6: Cumulative Balance Curve
Field	Description
Test Objective	Verify that historical cumulative balance is calculated using starting balance and transaction flow.
Preconditions	Valid transaction file and starting balance are available.
Test Data	Starting balance of $5,000 and sample transaction history.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload valid transaction file.	Data loads successfully.	Passed
2	Enter starting balance.	Input is accepted.	Passed
3	Review cumulative balance chart.	Balance curve reflects starting balance plus cumulative transaction amounts.	Passed
Test Status: Passed
 
Test Case V2-TC7: Stacked Monthly Spending Trends
Field	Description
Test Objective	Verify that monthly expenses are grouped by category and displayed in stacked format.
Preconditions	Multi-month categorized data is uploaded.
Test Data	April, May, and June expenses across several categories.
Step No.	Test Step Description	Expected Result	Actual Result
1	Upload multi-month categorized file.	File loads successfully.	Passed
2	Review stacked monthly spending trend chart.	Expenses are grouped by month and category.	Passed
3	Compare chart values to source data.	Displayed values match expected monthly category totals.	Passed
Test Status: Passed
 
5. Software Development and Test Environment Document
5.1 Software Used for Development
Software	Version	Purpose
macOS	Current local development OS	Operating system
Visual Studio Code	Current installed version	Code editor and Git interface
Python	3.11+	Programming language
Streamlit	Version listed in requirements.txt	Web application framework
pandas	Version listed in requirements.txt	Data ingestion, cleaning, and analytics
Plotly	Version listed in requirements.txt	Interactive visualizations
Git	Current installed version	Version control
GitHub	Web-based platform	Remote repository hosting
pip	Version bundled with Python environment	Package installation
5.2 Software Used for Testing
Software	Version	Purpose
Streamlit local server	Version listed in requirements.txt	Running system-level tests
Safari / Chrome	Current installed version	Browser-based UI testing
Python virtual environment	Python 3.11+	Isolated test environment
pandas	Version listed in requirements.txt	Data validation and calculation testing
Plotly	Version listed in requirements.txt	Chart rendering testing
GitHub	Web-based platform	Repository verification
 
6. Application Setup Instructions
6.1 Clone the Repository
git clone https://github.com/KarenJi2298/FinPredict.git
cd FinPredict
6.2 Create a Virtual Environment
python3 -m venv .venv
6.3 Activate the Virtual Environment
For macOS:
source .venv/bin/activate
For Windows:
.venv\Scripts\activate
6.4 Install Required Packages
pip install -r requirements.txt
6.5 Run the Application
streamlit run app.py
The application should open in a browser at:
http://localhost:8501
 
7. Test Environment Setup Instructions
7.1 Prepare Test Data
Create a sample CSV file with the following structure:
Transaction Date,Amount,Description,Category
2026-04-01,-45.20,Trader Joe's,
2026-04-02,-1200.00,Rent,
2026-04-03,2500.00,Paycheck,
2026-04-04,-15.75,Netflix,
2026-05-01,-52.10,Whole Foods,
2026-05-02,-1200.00,Rent,
2026-05-03,2500.00,Paycheck,
2026-06-01,-61.40,Costco,
2026-06-02,-1200.00,Rent,
2026-06-03,2500.00,Paycheck,
7.2 Execute System Tests
1.	Start the app using:
streamlit run app.py
2.	Upload the sample CSV file.
3.	Verify that raw data appears.
4.	Verify that cleaned data appears.
5.	Confirm that categories are automatically assigned.
6.	Review cash flow metrics.
7.	Review spending charts.
8.	Enter a starting balance.
9.	Review liquidity forecast.
10.	Enter a what-if expense scenario.
11.	Confirm that the scenario balance adjusts correctly.
12.	Upload invalid or incomplete CSV files to verify error handling.
 
8. Overall Test Summary
Version	Number of Test Cases	Passed	Failed	Result
Version 1	7	7	0	Passed
Version 2	7	7	0	Passed
 
9. Conclusion
The system-level test plan confirms that FinPredict satisfies the major functional requirements for both planned versions of the application. Version 1 successfully supports transaction ingestion, cleaning, categorization, cash flow analytics, and burn-rate visualization. Version 2 successfully adds liquidity forecasting, what-if simulation, cumulative balance tracking, risk alerts, and enhanced visual analytics.
The selected test cases provide adequate coverage because they test the full user workflow, major functional modules, expected success paths, invalid input handling, and important financial decision-support features.

