@echo off

:: Update Python to the latest version
echo Updating Python to the latest version...
python -m pip install --upgrade pip

:: Install virtualenv if not already installed
echo Installing virtualenv...
pip install virtualenv

:: Create a virtual environment
echo Creating a virtual environment...
python -m venv venv

:: Activate the virtual environment
echo Activating the virtual environment...
call venv\Scripts\activate.bat

:: Install required Python packages
echo Installing required Python packages...
pip install -r requirements.txt

echo Setup completed successfully!
pause
