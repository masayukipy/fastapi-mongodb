# How to install and run this app

## Install mongodb
Click to download mongodb --> https://repo.mongodb.org/yum/amazon/2/mongodb-org/6.0/x86_64/RPMS/mongodb-org-server-6.0.3-1.amzn2.x86_64.rpm <br />
Excute and Install "mongodb-windows-x86_64-6.0.3-signed.msi"

## Install venv
python -m venv .venv

## Install dependencies
.venv\scripts\activate <br />
pip install -r requirements.txt

## Run app
uvicorn main:app --reload

## How to use this app
In chrome browser, navigate to http://127.0.0.1:8000/docs <br />
Click "POST /developers Create Developer" collapse button <br />
Click "Try it out" button in the right side. <br />
Optionaly modify content of textfiled <br />
Click "Execute" button <br />
And then navigate to http://127.0.0.1:8000/developers  <br />
You will be able to see the mongodb database.