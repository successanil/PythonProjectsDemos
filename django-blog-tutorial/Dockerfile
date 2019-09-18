FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/django_project/src

WORKDIR /opt/services/django_project/src

COPY . /opt/services/django_project/src
RUN pip install -r /opt/services/django_project/src/requirements.txt

RUN cd django_project && python manage.py collectstatic --no-input

EXPOSE 9001

#RUN cd django_project && gunicorn django_project.wsgi -b 0.0.0.0:9001

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", "0.0.0.0:9001", "--chdir", "django_project", "django_project.wsgi:application"]
#CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", "0.0.0.0:8000", "--chdir", "django_rest", "django_rest.wsgi:application"]
