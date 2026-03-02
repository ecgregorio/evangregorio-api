# Deploying FastAPI on AWS EC2 (Ubuntu 24.04)

## Project Overview

This project documents my first successful deployment of a FastAPI application on an AWS EC2 instance running Ubuntu 24.04.

The goal was to:

- Launch and configure an EC2 instance
- Connect via SSH
- Set up Python properly (handling Ubuntu 24 restrictions)
- Create and activate a virtual environment
- Install FastAPI and Uvicorn
- Configure AWS Security Groups
- Deploy a live API accessible from the browser
- Manage background processes using screen
- This repository documents both the setup and the challenges encountered.

## Tech Stack
- AWS EC2
- Ubuntu 24.04 LTS
- Python 3.12
- FastAPI
- Uvicorn
- Linux (SSH, process management)
- screen (for background execution)

## Outcome 
Outcome
Successfully deployed a live FastAPI API on AWS EC2, configured networking and security rules, and managed background services properly.

This is my first complete cloud backend deployment from scratch.