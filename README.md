# Welcome to EventManagement!
EventManagement is a web application developed with DRF (Django Rest Framewrk), allowing users to manage events, and to registrate for events! The platform supports a variety of features including user registration, user authentication, creating events, registrating for the events. The app integrates with PostgreSQL, Redis, Celery for managin events, end sending email notifications to users upon event registration.

# Features
User Authentication: Register, log in, log out.
Events: Creating, Upgrating, Deleting own events. Register for other's events.

## Technologies Used
- Django - the main framework to create the APP
- DRF - for building the REST API
- PostgreSQL - for storing data
- drf-spectacular - for API documentation (Swager, ReDoc, row schemas)
- django-filter - for additional features (filtration, search, selection)

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements
Before you start, make sure you have everything installed:
- Python 3.12
- Poetry for dependency management
- Docker

## Installation
1. Clone the repository:
```bash
 git clone https://github.com/Deminform/instagram_final_project.git
```
2. Setup virtual environment
```bash
poetry install
poetry shell
```
3. Create .env file in your root directory and fill it with necessary environment variables.
Use .env_example file as example

4. Run docker-compose.yml to connect to database and mail service locally
```bash
 docker compose up