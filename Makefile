.PHONY: setup run clean

setup:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install -e .

run:
	python src/project/example_task.py

clean:
	rm -rf artifacts/* cache/*

run-jambase-enrich:
	@echo "Running JamBase Spotify enrichment..."
	python scripts/jambase_spotify_enricher.py

run-jambase-enrich:
	@echo "Running JamBase enrichment..."
	python scripts/jambase_spotify_enricher.py \
		--input $(INPUT) \
		--output $(OUTPUT)
