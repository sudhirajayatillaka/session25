@echo off
setlocal
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
  echo [ERROR] Setup has not been run. Double-click setup.bat first.
  exit /b 1
)

echo Open http://127.0.0.1:8000 in your browser.
echo Press Ctrl+C here to stop the server.
.venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

