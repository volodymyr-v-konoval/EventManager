# Welcome to EventManager!
EventManager is a web application developed with DRF (Django Rest Framework), allowing users to manage events and register for them. The platform supports a variety of features including user registration, authentication, event creation, and registration. The app integrates with PostgreSQL, Redis, and Celery to manage events and send email notifications to users upon event registration.

# Features
- **User Authentication**: Register, log in, log out
- **Events**: Create, update, delete your own events
- **Event Registration**: Register for others' events

## Technologies Used
- **Django** – main framework to build the app
- **DRF** – for building the REST API
- **PostgreSQL** – for data storage
- **drf-spectacular** – for API documentation (Swagger, ReDoc, raw schemas)
- **django-filter** – for filtering, search, sorting support

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [DockerHub](#dockerhub)
- [Usage](#usage)
- [Web](#web)
- [Contributing](#contributing)
- [License](#license)

## Requirements
Before you start, make sure you have installed:
- Python 3.10 or higher
- Poetry for dependency management
- Docker

## Installation
1. Clone the repository:
```bash
git clone https://github.com/volodymyr-v-konoval/EventManager.git
```

2. Setup virtual environment:
```bash
poetry install
poetry shell
```

3. Run Docker Compose to build and run the app locally with all dependencies:
```bash
docker compose up --build
```

## DockerHub
You can also pull the prebuilt image with all dependencies from DockerHub:

```bash
docker pull konovalvolodymyr/event-manager
```

[DockerHub page](https://hub.docker.com/repository/docker/konovalvolodymyr/event-manager/general)

## Usage
Once the project is up and running, visit:
```
http://127.0.0.1:8000/api/v1/docs/
```

The first user with admin role is created during startup. Credentials are defined in `entrypoint.sh`:
```
SUPERUSER: admin
EMAIL: admin@example.com
PASSWORD: adminpass
```

## Web
You can try the **cut-down version** of the app deployed on the web:
[Live demo (Koyeb)](https://stale-dallas-join-to-it-event-manager-60648aaa.koyeb.app/api/v1/)

Source code of the lightweight version:  
[GitHub - for_deploy_with_no_celery_and_redis](https://github.com/volodymyr-v-konoval/EventManager/tree/for_deploy_with_no_celery_and_redis)

## Contributing
1. Fork the repository
2. Create a new branch:
```bash
git checkout -b feature-name
```
3. Make your changes
4. Push your branch:
```bash
git push origin feature-name
```
5. Create a pull request

## Author
[@volodymyr-v-konoval](https://github.com/volodymyr-v-konoval)(volodymyr.v.konoval@gmail.com)

## License
Copyright © 2025

_This README was generated with ❤️_
