FROM thraxil/django.base:2022-09-11-0efda9ab2fe2
COPY requirements.txt /app/requirements.txt
RUN /ve/bin/pip3 install -r /app/requirements.txt && touch /ve/sentinal
WORKDIR /app
COPY . /app/
RUN VE=/ve/ MANAGE="/ve/bin/python3 manage.py" NODE_MODULES=/node/node_modules make all
EXPOSE 8000
ENV APP auratus
ENTRYPOINT ["/run.sh"]
CMD ["run"]
