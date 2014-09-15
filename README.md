# tracker
Track the latest content from the specified sites.

### Dependencies
1. Python 2.6 or higher
2. [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation) installed

### Build & Run

1. Prepare the dependencies of flask web application

		$ cd tracker/
		$ virtualenv venv; 
		$ venv/bin/pip install -r requirements.txt

2. Database migration

		$ venv/bin/python manage.py db upgrade

3. Run flask application

		$ venv/bin/python -B manage.py runserver

4. Fire the API

		Open the browser, visit `http://127.0.0.1:5000/parser/<search_term>`
		e.g. `http://127.0.0.1:5000/parser/htc`


### Chrome extension client

1. The Chrome extension is located at [here](https://github.com/browny/tracker/tree/master/cex)
2. It could be installed from source by [this](https://developer.chrome.com/extensions/getstarted#unpacked)


### License
tracker is released under the [WTFPL](http://en.wikipedia.org/wiki/WTFPL).
