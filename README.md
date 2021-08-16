# Running the example

Create a python 3 virtual environment 

`python3 -m venv venv`

Activate the virtual environment

- Windows(powershell): `./venv/Scripts/activate.ps1`
- Linux, Mac: `source venv/bin/activate`

Install required modules

`pip install -r requirements.txt`

Setup the flask environment variables

- Linux, Mac: `export FLASK_APP=web_app:init_app`
- Windows: `-TBD-`

Run update the database

`flask db ugrade`

Run the app:

`flask run`



# Running unittests

Running unittest through pytests

`python -m pytest -v`