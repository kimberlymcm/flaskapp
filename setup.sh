# Creates virtual environment and installs relevant packages
python3 -m venv venv

source venv/bin/activate
pip3 install -r requirements.txt

# Setting needed env security credentials
export AWS_ACCESS_KEY=$(< aws_access_key.txt)
export AWS_SECRET_KEY=$(< aws_secret_key.txt)
