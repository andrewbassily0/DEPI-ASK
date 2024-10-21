# Python App Dockerization and Deployment with Jenkins and Ansible

## Overview

This project demonstrates how to Dockerize a Python application, set up a Jenkins pipeline to automate the Docker build process, and use Ansible for deployment on a local VM. 

## Table of Contents

- Prerequisites
- Project Structure
- Dockerizing the Python App
- Jenkins Pipeline Setup 
- Ansible Configuration
- Usage
- Troubleshooting
- License

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your local machine and Jenkins server.
- Jenkins installed with the required plugins, including Docker Pipeline, Ansible Plugin, and Git Plugin.
- Ansible installed on the Jenkins server.
- Access to a local VM for deployment.

## Project Structure

The project has the following structure:

- **deploy/**: Contains the Ansible playbook and inventory files for deployment.
- **app.py**: The main application file.
- **requirements.txt**: Check Requirements.txt
- **Dockerfile**: Defines how to build the Docker image.
- **Jenkinsfile**: Specifies the Jenkins pipeline for automated builds and deployment.

## Dockerizing the Python App

The project includes a Dockerfile that describes how to create a Docker image for the Python application. It sets up the necessary environment, installs dependencies, and specifies how to run the application.

## Jenkins Pipeline Setup

The project uses a Jenkins pipeline to automate the following tasks:

1. Checkout the latest code from the Git repository.
2. Build the Docker image using the provided Dockerfile.
3. Push the Docker image to a Docker registry (e.g., Docker Hub).
4. Use Ansible to deploy the application to a local VM.

Ensure that Jenkins is configured to use Docker and has the necessary credentials for both the Docker registry and SSH access to the VM.

## Ansible Configuration

The Ansible setup consists of an inventory file that defines the target VM and a playbook that handles the installation of Docker and the deployment of the application. The playbook pulls the Docker image from the registry and runs it on the specified VM.

## Usage

To use the project, trigger the Jenkins pipeline either manually or through a webhook from your Git repository. Once the pipeline runs successfully, the application will be deployed, and you can access it via the specified port on the VM.

## Troubleshooting

If you encounter issues, consider the following:

- Check for permission issues if Jenkins cannot run Docker commands.
- Verify SSH connectivity and ensure the correct SSH key is being used for Ansible.
- Ensure the Docker image is pushed to the Docker registry without errors.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
