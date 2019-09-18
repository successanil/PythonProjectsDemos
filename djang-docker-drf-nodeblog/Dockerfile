FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/django_rest/src

WORKDIR /opt/services/django_rest/src

COPY . /opt/services/django_rest/src
RUN pip install -r /opt/services/django_rest/src/requirements.txt

RUN cd django_rest && python manage.py collectstatic --no-input

EXPOSE 9002
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", "0.0.0.0:9002", "--chdir", "django_rest", "django_rest.wsgi:application"]
#CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", "0.0.0.0:8000", "--chdir", "django_rest", "django_rest.wsgi:application"]
