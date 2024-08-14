# Krisp-Services
* FastAPI have used to run 5 requests parallel
* docker and docker-compose have used to run containerized apps

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Services](#running-the-services)
- [To Do](#to-do)

## Features

- **FastAPI Invoker**: Microservice for high-performance tasks using FastAPI.
- **Flask Generator**: Microservice built with Flask for straightforward operations.
- **Dockerized**: Both services are containerized for easy deployment.

## Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sur1010/Krisp-Services.git
2. **Navigate to the project directory**:
    ```bash
    cd Krisp-Services
3. **Build and run the services**:
   ```bash
   docker-compose up --build

## Running the Services
Servers wil run on:
+ FastAPI Invoker: `http://localhost:8000`
+ Flask Generator: `http://localhost:5000`

## You can find invoker API swagger here
http://localhost:8000/docs


# To Do
1. Create tests for the endpoints (Unit, Integration and API)
2. Add redis for the cache
3. Create separate environments for dev, tst and prod
4. Add nginx with gunicorn and set threads/processes for prod environments
5. Make app more configurable (for example get ttl time and other configs from .env)
6. Create more comfortable structure for the complex tasks like (controllers, serializers, models, request_forms ...etc)
7. Deploy apps to the EC2 and add link to the app in README
