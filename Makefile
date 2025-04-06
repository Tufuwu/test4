NODE_BIN=./node_modules/.bin

help:
	@echo '                                                                                     		'
	@echo 'Makefile for the xqueue-watcher                                                   		'
	@echo '                                                                                     		'
	@echo 'Usage:                                                                               		'
	@echo '    make requirements                 install requirements for local development     		'
	@echo '    make test                         run python unit-tests     	                 		'
	@echo '    make clean                        delete generated byte code and coverage reports		'
	@echo '                                                                                     		'

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -q -r requirements/pip_tools.txt
	pip-compile --upgrade -o requirements/pip_tools.txt requirements/pip_tools.in
	pip-compile --upgrade -o requirements/base.txt requirements/base.in
	pip-compile --upgrade -o requirements/production.txt requirements/production.in
	pip-compile --upgrade -o requirements/test.txt requirements/test.in
	pip-compile --upgrade -o requirements/ci.txt requirements/ci.in

requirements:
	pip install -qr requirements/production.txt --exists-action w

test.requirements:
	pip install -q -r requirements/test.txt --exists-action w

ci.requirements:
	pip install -q -r requirements/ci.txt --exists-action w

test: test.requirements
	pytest --cov=xqueue_watcher --cov-report=xml tests

clean:
	find . -name '*.pyc' -delete

# Targets in a Makefile which do not produce an output file with the same name as the target name
.PHONY: help requirements clean
