FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update && apt-get install -y postgresql-client
COPY requirements /app/requirements
COPY iamsitting_site /app/iamsitting_site
COPY scripts /app/scripts
ENV DJANGO_SETTINGS_MODULE iamsitting_site.settings.development
RUN pip install -r requirements/production.txt
EXPOSE 8000
RUN chmod +x scripts/run_docker_dev.sh && chmod +x scripts/wait-for-it.sh
CMD ["scripts/run_docker_dev.sh"]

