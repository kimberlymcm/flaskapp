# Creates virtual environment and installs relevant packages
python3 -m venv venv

source venv/bin/activate
pip3 install -r requirements.txt

# To run the application
python3 application.py

# Files aws_config.py and rds_config.py were intentionally
# left out of git because they contain passwords
