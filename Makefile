SHELL = /bin/bash -c
VIRTUAL_ENV = $(shell poetry env info --path)
export BASH_ENV=$(VIRTUAL_ENV)/bin/activate

.DEFAULT_GOAL:=help
.PHONY: help
help:  ## Display this help
    $(info aws-iam-login - simplify AWS logins)
    awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: lint
lint: _black _mypy ## Lint all project files

.PHONY: test
test: lint ## Run the test suite defined in the project
	pytest --cov --cov-report term-missing --junitxml=reports/pytest.xml --cov-report xml:reports/coverage.xml

.PHONY: install
install: $(VIRTUAL_ENV) ## Install all dependencies
	poetry install

.PHONY: clean
clean: ## Cleanup removes all temporary local files and folders
	[[ -d "$(VIRTUAL_ENV)" ]] && rm -rf "$(VIRTUAL_ENV)" || true
	[[ -d .mypy_cache ]] && rm -rf .mypy_cache || true
	[[ -d .pytest_cache ]] && rm -rf .pytest_cache || true
	[[ -d dist ]] && rm -rf dist || true
	[[ -d reports ]] && rm -rf reports || true
	[[ -f .coverage ]] && rm .coverage || true

.PHONY: build
build: ## Build the project
	poetry build

.PHONY: release
release: build ## Create a release
	twine upload dist/*

.PHONY: complexity
complexity: ## Perform complixity scanning
	$(info Maintenability index)
	radon mi --min A --max A --show --sort aws_iam_login
	$(info Cyclomatic complexity index)
	xenon --max-absolute A --max-modules A --max-average A aws_iam_login

.PHONY: _black
_black:
	$(info [*] Formatting python files...)
	black .

.PHONY: _mypy
_mypy:
	$(info [*] Python static type checker...)
	mypy --junit-xml reports/typecheck.xml aws_iam_login

$(VERBOSE).SILENT:
