@echo off
REM One-liner install (copy-paste this into PowerShell):
REM   powershell -NoProfile -ExecutionPolicy Bypass -Command "(iwr -useb https://raw.githubusercontent.com/truongnat/simple-skills/main/install.ps1).Content | iex"
REM
REM Or run this file directly:
REM   .\install.cmd

setlocal

set "ROOT=%~dp0"
cd /d "%ROOT%"

powershell -NoProfile -ExecutionPolicy Bypass -File "%ROOT%install.ps1" %*
if errorlevel 1 exit /b 1

endlocal
