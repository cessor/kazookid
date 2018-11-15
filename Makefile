.PHONY: test
test:
	nosetests --nocapture

verbose:
	nosetests --nocapture --verbose

cover:
	nosetests --with-coverage --cover-html --cover-package=kazookid