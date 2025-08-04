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

sentinelpulse/
│
├── app.py                  # Streamlit or Dash frontend
├── monitor/
│   ├── __init__.py
│   ├── system_metrics.py   # CPU, RAM, etc.
│   ├── service_checker.py  # Ping mock services
│   └── alert_manager.py    # Threshold logic
│
├── data/
│   └── logs/               # Saved logs, SQLite or flat files
│
├── utils/
│   ├── config.py           # Thresholds, refresh rate, etc.
│   └── logger.py           # Logging logic
│
├── tests/
│   └── test_metrics.py     # Unit tests for monitor components
│
└── README.md
