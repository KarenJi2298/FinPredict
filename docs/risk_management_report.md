Risk Management Report
Project: FinPredict – Intelligent Expense Analytics & Liquidity Forecasting
Course: CISC 594
Students: Zekun Ji & Huihai Jiang
 
Introduction
This document tracks project risks throughout the development lifecycle of FinPredict. The report is updated weekly to monitor existing risks, identify new risks, evaluate mitigation effectiveness, and retire risks that are no longer relevant. Risks are prioritized using probability and impact analysis to support proactive project management.
 
Risk Assessment Criteria
Probability Level	Description
Low	Unlikely to occur
Medium	Possible during development
High	Likely to occur
Impact Level	Description
Low	Minor inconvenience
Medium	Moderate impact on functionality or schedule
High	Significant impact on project success
 
Week 1: Project Initialization and Data Ingestion
Development Focus
•	GitHub repository setup
•	Streamlit application initialization
•	Transaction ingestion pipeline
•	CSV validation and schema standardization
 
Risk 1: Inconsistent Transaction File Formats
Description
Different financial institutions export transaction files using inconsistent schemas, column names, and date formats.
Probability
High
Impact
High
Mitigation Strategy
•	Implement standardized internal schema
•	Add column normalization logic
•	Validate required columns during upload
•	Add error handling for malformed files
Status
Active
 
Risk 2: Dependency and Environment Configuration Issues
Description
Missing packages or inconsistent virtual environments may prevent the application from running correctly.
Probability
Medium
Impact
Medium
Mitigation Strategy
•	Maintain requirements.txt
•	Use Python virtual environments
•	Verify package compatibility
•	Document installation procedures
Status
Active
 
Risk 3: Project Architecture Instability
Description
Poor repository organization or inconsistent module structure may complicate future feature development.
Probability
Medium
Impact
Medium
Mitigation Strategy
•	Separate ingestion, analytics, and categorization modules
•	Maintain modular folder structure
•	Use GitHub version control workflow
Status
Active
 
Week 2: Categorization and Analytics Development
Development Focus
•	Automated transaction categorization
•	Cash flow analytics
•	Spending summaries
•	Burn-rate calculations
 
Reassessment of Existing Risks
Risk 1: Inconsistent Transaction File Formats
Updated Analysis
Implementation of schema validation and standardized column mapping reduced ingestion failures.
Probability
Reduced from High to Medium
Impact
High
Status
Active
 
Risk 2: Dependency and Environment Configuration Issues
Updated Analysis
Virtual environment setup and dependency management improved stability.
Probability
Reduced from Medium to Low
Impact
Medium
Status
Active
 
New Risk 4: Incorrect Transaction Categorization
Description
Keyword-based categorization logic may incorrectly classify transactions with ambiguous merchant descriptions.
Probability
Medium
Impact
Medium
Mitigation Strategy
•	Expand keyword rules
•	Add fallback Uncategorized category
•	Improve categorization coverage over time
Status
Active
 
New Risk 5: Inaccurate Spending Analytics
Description
Incorrect calculations or malformed transaction data may distort spending summaries and burn-rate metrics.
Probability
Medium
Impact
Medium
Mitigation Strategy
•	Validate numeric transaction amounts
•	Use standardized aggregation logic
•	Test calculations using sample datasets
Status
Active
 
Week 3: Forecasting and What-If Simulation
Development Focus
•	Liquidity forecasting
•	Scenario simulation
•	Starting balance configuration
•	Forecast visualizations
 
Reassessment of Existing Risks
Risk 4: Incorrect Transaction Categorization
Updated Analysis
Expanded categorization rules improved classification accuracy, but edge cases remain.
Probability
Reduced from Medium to Low
Impact
Medium
Status
Active
 
New Risk 6: Forecasting Model Inaccuracy
Description
The liquidity forecast may produce unrealistic projections due to irregular spending behavior or insufficient historical data.
Probability
Medium
Impact
High
Mitigation Strategy
•	Use interpretable average daily cash flow model
•	Clearly indicate forecasts are estimates
•	Allow user-controlled scenario testing
•	Consider future Prophet or ARIMA integration
Status
Active
 
New Risk 7: Misleading Scenario Simulations
Description
Users may misinterpret what-if simulations as guaranteed future outcomes rather than estimated scenarios.
Probability
Medium
Impact
Medium
Mitigation Strategy
•	Display explanatory forecast disclaimers
•	Clearly separate projected and simulated balances
•	Emphasize estimation-based forecasting
Status
Active
 
Week 4: Dashboard Visualization and User Interface Enhancements
Development Focus
•	Pie charts
•	Stacked monthly spending trends
•	Cumulative balance visualization
•	Sidebar interface redesign
 
Reassessment of Existing Risks
Risk 6: Forecasting Model Inaccuracy
Updated Analysis
Forecast visualization improved interpretability, but prediction uncertainty remains inherent.
Probability
Medium
Impact
High
Status
Active
 
New Risk 8: Visualization Performance Issues
Description
Large transaction datasets may slow chart rendering and reduce dashboard responsiveness.
Probability
Medium
Impact
Medium
Mitigation Strategy
•	Optimize pandas transformations
•	Avoid redundant dataframe calculations
•	Limit rendering complexity where necessary
Status
Active
 
New Risk 9: Visualization Dependency Failures
Description
External visualization libraries such as Plotly may introduce compatibility or installation issues.
Probability
Medium
Impact
Low
Mitigation Strategy
•	Maintain dependency documentation
•	Verify virtual environment configuration
•	Update requirements.txt after package installation
Status
Mitigated
 
Week 5: Testing and Stability Review
Development Focus
•	System testing
•	Feature integration validation
•	User interface refinement
•	Risk review
 
Reassessment of Existing Risks
Risk 1: Inconsistent Transaction File Formats
Updated Analysis
The ingestion engine successfully handles standardized CSV structures. Remaining risk primarily involves unsupported bank-specific export formats.
Probability
Low
Impact
High
Status
Active
 
Risk 2: Dependency and Environment Configuration Issues
Updated Analysis
Stable virtual environment configuration significantly reduced setup failures.
Probability
Low
Impact
Medium
Status
Retired
 
Risk 6: Forecasting Model Inaccuracy
Updated Analysis
Forecasting remains the highest-priority technical risk because simplified assumptions may not fully capture complex financial behavior.
Probability
Medium
Impact
High
Status
Active
 
Risk 8: Visualization Performance Issues
Updated Analysis
Current datasets perform well, but scalability concerns may emerge with significantly larger transaction histories.
Probability
Low
Impact
Medium
Status
Active
 
Final Risk Prioritization Summary
Risk	Probability	Impact	Priority	Status
Forecasting Model Inaccuracy	Medium	High	High	Active
Inconsistent Transaction File Formats	Low	High	Medium	Active
Incorrect Transaction Categorization	Low	Medium	Medium	Active
Visualization Performance Issues	Low	Medium	Low	Active
Misleading Scenario Simulations	Medium	Medium	Medium	Active
Dependency and Environment Issues	Low	Medium	Low	Retired
 
Conclusion
Risk management was continuously integrated into the FinPredict development process throughout the semester. As new features such as forecasting, categorization, visual analytics, and scenario simulation were introduced, the project team regularly reassessed technical and operational risks. Mitigation strategies reduced several early-stage development risks, while forecasting accuracy remained the most significant ongoing challenge due to the uncertainty inherent in financial prediction systems.
The iterative monitoring and reassessment process helped improve project stability, usability, and maintainability while supporting successful implementation of the core project objectives.