server: clean
	python3 app.py

run: clean
	gunicorn app:application --preload -b 0.0.0.0:5000

clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	rm -f .coverage
	rm -f pylint.out

test: clean
	nosetests -s --rednose

coverage: clean
	nosetests --with-coverage --cover-package=ads

translate:
	flask translate compile
