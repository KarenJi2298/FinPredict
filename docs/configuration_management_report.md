Configuration Management Report
Project: FinPredict – Intelligent Expense Analytics & Liquidity Forecasting
Course: CISC 594
Students: Zekun Ji & Huihai Jiang
 
1. Introduction
This report describes the configuration management activities used throughout the development of the FinPredict semester project. Configuration management practices were implemented to maintain source code integrity, track software evolution, manage releases, control changes to the application baseline, and support reliable recovery of stable software versions.
Git and GitHub were used as the project’s version control system for:
•	source code management
•	change tracking
•	release tagging
•	repository backup
•	branch management
•	collaborative configuration control
The instructor was provided access to the project repository throughout development.
 
2. Version Control System
Version Control Tools
Tool	Purpose
Git	Local version control and change tracking
GitHub	Remote repository hosting and repository backup
Visual Studio Code	Integrated development environment with Git integration
 
Repository Information
Item	Description
Repository Name	FinPredict
Repository Platform	GitHub
Repository URL	https://github.com/KarenJi2298/FinPredict
Main Branch	main
Documentation Branch	feature/project-documentation
The GitHub repository maintained the complete development history of:
•	application source code
•	forecasting logic
•	dashboard visualizations
•	categorization rules
•	risk alerts
•	testing documentation
•	configuration management documentation
 
3. Repository Structure
The project used a modular repository structure to improve maintainability and support controlled development.
FinPredict/
│
├── src/
│   ├── ingestion.py
│   ├── analytics.py
│   ├── categorization.py
│   └── __init__.py
│
├── data/
├── models/
├── tests/
├── docs/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
The modular organization separated:
•	ingestion logic
•	analytics calculations
•	categorization logic
•	forecasting functionality
•	dashboard interface
•	project documentation
This structure simplified maintenance and reduced integration risk.
 
4. Configuration Identification
The following items were treated as controlled configuration items:
Configuration Item	Description
Source Code	Python application files
requirements.txt	Dependency configuration
README.md	Project setup documentation
Forecasting Logic	Liquidity prediction functionality
Dashboard Components	Streamlit visualizations and metrics
Categorization Rules	Automated transaction classification logic
Risk Management Documents	Semester project documentation
System Test Documents	Test procedures and validation records
 
5. Branch Management Process
Early Development Workflow
During the initial implementation phase, most development was performed directly on the main branch after local testing. Features were implemented incrementally and validated through local Streamlit execution before commits were pushed to GitHub.
Examples of development activities completed during this phase included:
•	Streamlit application setup
•	transaction ingestion
•	cash flow analytics
•	automatic categorization
•	forecasting
•	dashboard visualizations
•	what-if simulation
•	risk alerts
Although the software remained stable during development, the workflow did not initially follow a formal branch-based strategy.
 
Corrective Configuration Management Actions
After reviewing the configuration management requirements, the development process was formalized by:
1.	creating tagged release baselines
2.	introducing a feature branch workflow
3.	separating documentation changes from the stable main branch
A dedicated feature branch named:
feature/project-documentation
was created for configuration-controlled documentation updates before merging changes back into main.
 
Feature Branch Workflow
The following branch workflow was adopted for controlled updates:
Step 1: Create Branch
Example:
git checkout -b feature/project-documentation
 
Step 2: Implement and Validate Changes
Documentation and configuration updates were completed and reviewed locally.
 
Step 3: Commit Changes
Example:
git add docs/
git commit -m "Add project documentation reports"
 
Step 4: Push Branch to GitHub
Example:
git push -u origin feature/project-documentation
 
Step 5: Merge into Main
After validation, the branch was merged back into the stable baseline branch:
git checkout main
git merge feature/project-documentation
git push
This process ensured controlled integration of changes into the working software baseline.
 
6. Change Control Process
A formal change control process was used to introduce changes into the software baseline in a controlled manner.
 
Change Control Objectives
The change control process was designed to:
•	maintain software stability
•	reduce regression risk
•	improve traceability
•	ensure controlled modification of the application baseline
•	support reliable release management
 
Change Control Workflow
Phase 1: Change Identification
A proposed change was identified based on:
•	feature requirements
•	usability improvements
•	testing feedback
•	defect correction
•	visualization enhancements
Examples included:
•	adding liquidity forecasting
•	implementing risk alerts
•	redesigning the dashboard sidebar
•	improving visual analytics
 
Phase 2: Change Analysis
Each proposed change was evaluated to determine:
•	affected modules
•	implementation complexity
•	testing requirements
•	impact on existing functionality
 
Phase 3: Implementation
Changes were implemented locally and validated using:
•	CSV upload tests
•	dashboard rendering checks
•	forecasting validation
•	scenario simulation testing
•	visualization verification
 
Phase 4: Configuration Update
Once validated:
•	changes were committed
•	pushed to GitHub
•	merged into the stable baseline branch
 
Phase 5: Baseline Preservation
Stable versions of the software were preserved through Git release tagging.
 
7. Release Management and Version Tagging
After successful testing and stabilization, major software baselines were tagged using Git release tags.
 
Version 1 Baseline
Release Tag
v1.0
Commit Reference
9764faa
Features Included
•	transaction ingestion
•	schema standardization
•	automatic categorization
•	cash flow summary metrics
•	spending analytics
Tagging Commands
git tag -a v1.0 9764faa -m "Release Version 1.0 - Analytical Foundation"
git push origin v1.0
 
Version 2 Baseline
Release Tag
v2.0
Commit Reference
69d7e54
Features Included
•	liquidity forecasting
•	what-if simulation
•	risk alerts
•	enhanced dashboard visualizations
•	sidebar interface redesign
Tagging Commands
git tag -a v2.0 69d7e54 -m "Release Version 2.0 - Predictive Intelligence"
git push origin v2.0
 
8. Configuration Status Accounting
GitHub commit history provided full traceability for:
•	feature additions
•	dashboard enhancements
•	forecasting updates
•	categorization improvements
•	visualization changes
•	documentation updates
The repository maintained records of:
•	when changes occurred
•	what functionality changed
•	release baselines
•	branch merges
•	configuration updates
 
9. Backup and Recovery
GitHub functioned as the project’s remote backup repository.
Backup and recovery protection included:
•	regular commits
•	remote pushes
•	release tags
•	stable baseline preservation
This ensured that previous working versions could be restored if necessary.
 
10. Software Baselines
Two primary baselines were maintained:
Baseline	Description
Version 1.0	Analytical foundation release
Version 2.0	Predictive intelligence release
Each baseline represented:
•	tested functionality
•	stable configuration state
•	controlled release snapshot
 
11. Source Code Submission
The complete source code was submitted separately as a ZIP archive together with this configuration management report.
The ZIP archive included:
•	Python source files
•	requirements.txt
•	README.md
•	project documentation
•	test data
•	configuration files
The .venv virtual environment directory was excluded from the ZIP package to reduce file size and improve portability.
 
12. Conclusion
Configuration management activities were integrated throughout the development lifecycle of FinPredict to support software stability, traceability, release control, and repository management.
Git and GitHub were successfully used for:
•	source code versioning
•	release tagging
•	baseline preservation
•	branch management
•	repository backup
Although early development occurred primarily on the main branch, the process was later formalized through release tagging and the introduction of a feature branch workflow for controlled updates. These practices improved project maintainability and ensured that stable software baselines were preserved throughout the semester project lifecycle.

