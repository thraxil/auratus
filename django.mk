jenkins: $(SENTINAL) check test flake8

test: $(SENTINAL)
	$(MANAGE) test

coverage: $(SENTINAL) flake8
	. $(VE)/bin/activate && $(VE)/bin/coverage run --source='$(APP)' $(MANAGE) test \
	&& $(VE)/bin/coverage html -d reports --omit='*migrations*,*settings_*,*wsgi*'

$(SENTINAL): $(REQUIREMENTS)
	rm -rf $(VE)
	$(SYS_PYTHON) -m venv $(VE)
	$(PIP) install wheel==$(WHEEL_VERSION)
	$(PIP) install --no-deps --requirement $(REQUIREMENTS)
	touch $(SENTINAL)

flake8: $(SENTINAL)
	$(FLAKE8) $(APP) --max-complexity=$(MAX_COMPLEXITY)

runserver: $(SENTINAL) check
	$(MANAGE) runserver

migrate: $(SENTINAL) check
	$(MANAGE) migrate

makemigrations: $(SENTINAL) check
	$(MANAGE) makemigrations

check: $(SENTINAL)
	$(MANAGE) check

shell: $(SENTINAL)
	$(MANAGE) shell_plus

clean:
	rm -rf ve
	rm -rf media/CACHE
	rm -rf reports
	rm celerybeat-schedule
	rm .coverage
	find . -name '*.pyc' -exec rm {} \;

pull:
	git pull
	make check
	make test
	make migrate
	make flake8

rebase:
	git pull --rebase
	make check
	make test
	make migrate
	make flake8

collectstatic: $(SENTINAL) check
	$(MANAGE) collectstatic --noinput --settings=$(APP).settings_production

compress: $(SENTINAL) check
	$(MANAGE) compress --settings=$(APP).settings_production

# run this one the very first time you check
# this out on a new machine to set up dev
# database, etc. You probably *DON'T* want
# to run it after that, though.
install: $(SENTINAL) check test flake8
	createdb $(APP)
	$(MANAGE) syncdb --noinput
	make migrate

.PHONY: clean collectstatic compress install pull rebase shell check migrate runserver flake8 test jenkins
