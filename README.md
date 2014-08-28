## tracker
Track the latest content from the specified sites.

### Dependencies
1. Python 2.6 or higher
2. [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation) installed

### Build & Run

1. Prepare the dependencies of flask web application

		$ cd tracker/
		$ virtualenv env; 
		$ env/bin/pip install -r requirements.txt

2. Run flask application

		$ env/bin/python -B /opt/flask/run.py
