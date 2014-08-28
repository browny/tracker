# tracker
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

		$ env/bin/python -B run.py

3. Fire the API

		Open the browser, visit `http://0.0.0.0:5000/parser/<search_term>`
		e.g. `http://0.0.0.0:5000/parser/htc`

### License
tracker is released under the [WTFPL](http://en.wikipedia.org/wiki/WTFPL).
