@echo off
setlocal
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
  echo [ERROR] Setup has not been run. Double-click setup.bat first.
  exit /b 1
)

if "%~1"=="" (
  echo Usage: check.bat LEVEL
  echo Examples: check.bat 2    or    check.bat all
  exit /b 2
)

.venv\Scripts\python.exe tools\check.py %*
exit /b %errorlevel%

