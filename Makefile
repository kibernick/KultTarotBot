run:
	python run.py

lint:
	isort --profile black .;\
	black .
