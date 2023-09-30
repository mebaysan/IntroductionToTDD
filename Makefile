format:
	@black src

lint:
	@flake8 src/

test:
	@pytest src/ -vv --disable-warnings --cov

coverage:
	@coverage report -m
	@coverage html
	@coverage xml

run:
	@python src/main.py