.PHONY: setup run clean

setup:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install -e .

run:
	python src/project/example_task.py

clean:
	rm -rf artifacts/* cache/*
