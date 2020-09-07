# PRICEPLUSCOST

Project to show net present value of various appliances.

Consists of four apps:

1. Scripts using SQLalchemy for building, storing, and managing PostgreSQL database of extracted and transformed data
2. Flask app with Jinja2 templating for providing a web frontend for the data
3. Django application for machine-learning assisted mapping of data sources
4. Apache Airflow instance for moving data and performing calculations via scheduled DAGs

## Usage

Docker is the preferred method. 

### Development

Docker compose override will create local containers for postgres, redis (used for Airflow celery), and localstack (s3 clone).

```
docker-compose up
```

To work only on the package application, use `DockerFile`.

```
docker build -t pricepluscost -f ./_docker/DockerFile.dev .
docker run -it --rm pricepluscost
```

For development, try bind mounting so to link files from container to local. Unforuntunately, Docker currently only supports absolutel path (docker compose can use relative paths, though). Replace as needed:

```
docker run -it --rm -v x:/phi/github/pricepluscost:/pricepluscost/ pricepluscost
```

Also, if you have ran docker-compose and created all containers, you can use Docker Desktop to run individual containers and access CLI.

### Production

`.env` and `-f docker-compose.yml` to ignore the override and generate only containers for the needed applications:
* Airflow-webserver
* Airflow-scheduler
* Airflow-worker
* Flask-webserver

Alternatively, if using something like Google Composer, where Airflow is run via custom Google frontend, then use the individual `DockerFile` to generate only the Flask app.