# SentinelPulse
Automated System Health and Resource Monitoring Dashboard

💡 Project Summary
Create a Python-based, modular system that monitors and displays the health of various systems or simulated services (CPU, memory, disk, network I/O, and mock service statuses), with real-time updates via a web dashboard (e.g., using Dash or Streamlit).

🧱 Core Features
Feature	                Description
System metrics	        Collect live CPU, RAM, disk, I/O, uptime, etc. using psutil
Service status check	  Simulated pings to mock services or endpoints
Alerting system	        Simple thresholds for warning and critical states
Real-time dashboard	    Web interface to visualize system state
Logging	                Write system logs to local .log files or SQLite
Modular design	        Easy to extend new modules like GPU stats or container metrics

📁 Folder Structure
```
sentinelpulse/
│
├── app.py                  # Main Streamlit app entry point
├── README.md               # Project overview, instructions
├── requirements.txt        # Python dependencies
│
├── monitor/                # Core monitoring modules
│   ├── __init__.py
│   ├── system_metrics.py   # CPU, RAM, disk usage etc.
│   ├── service_checker.py  # Service availability checks
│   └── alert_manager.py    # Alerts and thresholds
│
├── utils/                  # Utility/helper functions
│   ├── __init__.py
│   ├── config.py           # Configuration variables, thresholds
│   └── logger.py           # Logging setup and functions
│
├── data/                   # Data storage (logs, databases)
│   └── logs/               # Log files, SQLite DB files if any
│
├── tests/                  # Unit tests
│   └── test_metrics.py     # Tests for monitor modules
│
└── .gitignore              # Files/folders to ignore in git

