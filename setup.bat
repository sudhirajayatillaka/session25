@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Python was not found.
  echo Install Python 3.12 and select "Add Python to PATH", then try again.
  exit /b 1
)

echo [1/4] Creating the project environment...
py -3.12 -m venv .venv
if errorlevel 1 exit /b 1

echo [2/4] Updating pip...
.venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 exit /b 1

echo [3/4] Installing workshop tools...
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
if errorlevel 1 exit /b 1

echo [4/4] Installing the test browser...
.venv\Scripts\python.exe -m playwright install chromium
if errorlevel 1 exit /b 1

.venv\Scripts\python.exe tools\preflight.py
exit /b %errorlevel%

