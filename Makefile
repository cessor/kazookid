.PHONY: test
test:
	nosetests --nocapture

verbose:
	nosetests --nocapture --verbose

cover:
	nosetests --with-coverage --cover-html --cover-package=kazookid

dist:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*