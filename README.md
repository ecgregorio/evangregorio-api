## Project Overview

This project is a FastAPI backend deployed on an **AWS EC2** instance running Ubuntu 24.04 and connected to a **PostgreSQL** database.  
I'm working on this as a prototype for a future project and for learning **cloud deployment**, **backend development**, and **database integration**.

The API is live and accessible via the web. You can test endpoints directly in your browser or with tools like Postman.

Currently in early early experimentation phase.

## Live Server
You can access the homepage here:

🌐 https://evangregorio.me

You can also access the interactive API docs (Swagger UI) directly:

🌐 https://api.evangregorio.me/docs

## Tech Stack
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/docker-containerized-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)

**Cloud / OS**

* AWS EC2
* Ubuntu 24.04 LTS

**Backend**

* Python 3.12
* FastAPI
* Gunicorn
* Uvicorn workers

**Database**

* PostgreSQL 16+
* SQLAlchemy ORM

**Infrastructure / Deployment**

* Docker & Docker Compose
* Nginx reverse proxy
* HTTPS via Certbot
* SSH remote management

## Deployment Architecture

The production deployment uses a reverse proxy architecture:

<img width="200" alt="image" src="https://github.com/user-attachments/assets/636851df-af5b-4004-aaa8-4dd334af8463" />



## Preview

> March 04, 2026 20:44
> The FastAPI Swagger UI automatically documents all available endpoints.
<img width="500" height="450" alt="image" src="https://github.com/user-attachments/assets/a81a5ad0-88f0-4ca7-bfbc-7fc12c954342" />

> March 07, 23:29
> Containers running on the EC2 server via Docker Compose
<img width="1779" height="128" alt="image" src="https://github.com/user-attachments/assets/471d7ceb-cf0f-41cb-a11d-54b8d48d1e59" />


## Notes

- The API is running behind Nginx with HTTPS provided by Certbot.
- FastAPI is served via Gunicorn and managed by systemd for automatic restart and reliability.
- Any changes to code require restarting the FastAPI systemd service: ```sudo systemctl restart fastapi```
- * The API is served via Gunicorn with Uvicorn workers
- The service runs inside Docker containers
- PostgreSQL data is persisted using Docker volumes
