# Karyakram
Nepalese events in Canada

# Getting started
1. Fork the repository and clone it on your local machine.
2. Make sure `python` is installed and environment variable is configured properly. You can verify Python is working as expected by using `python --version`. Similarly, make sure Poetry is installed. You can verify it by using command `poetry --version`
3. Go to project directory and run `poetry install` to install the required packages.
4. Go inside karyakram_backend directory and create .env by taking reference from .env.example `cp .env.example .env`. You can change the configuration as per your requirement. Everything should work as it is if you don't want to change configuration.
5. Install Docker
6. Go to project root directory and run `docker-compose --env-file=./.env up -d` to run postgres. 
7. Step 5 and 6 is optional. You can install postgres in your laptop and skip these steps. I find running it with docker much easier for development purpose.
8. Go inside karyakram_backend directory and run `poetry run uvicorn main:app` and it will run the server in localhost:8000.

# Contribution
todo

# Deployment
todo
