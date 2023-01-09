# How to install and run this app

## install venv
python -m venv .venv

## install dependencies
.venv\scripts\activate
pip install -r requirements.txt

## run
uvicorn main:app --reload

## How to use this app
In chrome browser, navigate to http://127.0.0.1:8000/docs <br />
Click "POST /developers Create Developer" collapse button <br />
Click "Try it out" button in the right side. <br />
Optionaly modify content of textfiled <br />
Click "Execute" button <br />
And then navigate to http://127.0.0.1:8000/developers  <br />
You will be able to see the mongodb database.