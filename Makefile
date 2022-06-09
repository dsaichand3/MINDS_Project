test:
	black --check .

format:
	black .

install:
	pip install -r requirements.txt

run:
	black --check .
	python main.py