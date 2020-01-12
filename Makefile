run:
	python -m hotel_system $(FILE)
test:
	py.test tests
clean:
	find . -name "*.pyc" -exec rm '{}' ';'
	find . -type d -empty -delete
	rm -rf .pytest_cache

.PHONY: init test