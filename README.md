![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)


Simple desktop-app PC-monitor on PyQt5.
1. Install python, pip
2. Open root folder 'pc-monitor-desktop' (cd pc-monitor-desktop)
3. Create and start virtual environment (Linux):
  - python3 -m venv venv
  - source venv/bin/activate
4. Install requierements из requirements.txt:
  - pip install -r requirements.txt
    Run DesktopApp:
  - python3 app.py
    App will start in window.
  - Default update interval is 1 sec, data shows on the page
  - Button "Start Recording" creates DB Sqlite where data saved and timer starts. Is shows timestamps in DB.
  - Interaval can be set by "Set Interval" button.
  - Second tap on "Stop Recording" stopped recording to the DB, timer canceled to 0.
