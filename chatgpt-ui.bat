@echo off

rem Change to the script's directory
cd /d "%~dp0"

rem Set the Python executable path
set PYTHON_EXE=python

rem Set the Python script path
set SCRIPT_PATH=chatgpt.py

rem Run the Python script
%PYTHON_EXE% %SCRIPT_PATH%

rem Pause the command prompt window
pause
