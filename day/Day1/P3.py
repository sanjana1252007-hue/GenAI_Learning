# pip, virtual environment, .env file
# pip: pip installs Pacakages, Pacakage manager

# virtual environment: a 'venv' is a directory that contains 
# 1. A copy of the python interpreter
# 2. Its own 'pip'
# 3. Its own site-packages directory. Default target location
# 4. Activation scripts that modify PATH


python --version #windows

#To create virtual environment
python -m venv .venv

#Activate virtual environment
.venv\Scripts\activate.bat

# Deactivate
deactivate

#pip installation (install dependencies/libraries)
pip install package_name #syntax

pip install python-dotenv