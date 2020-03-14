build:
	pip install -r requirements.txt

test:
	py.test test

all: build test

clean:
	@echo "done"

.PHONY: build test all clean