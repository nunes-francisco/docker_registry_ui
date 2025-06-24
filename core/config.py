# class Config:
#     DOCKER_REGISTRY_URL = 'https://your-docker-registry-url'
#     DOCKER_USERNAME = 'your-username'
#     DOCKER_PASSWORD = 'your-password'
import os

class Config:
    DOCKER_REGISTRY_URL = os.getenv('DOCKER_REGISTRY_URL', 'https://registry.cscloud.biz')
    DOCKER_USERNAME = os.getenv('DOCKER_USERNAME', 'csadmin')
    DOCKER_PASSWORD = os.getenv('DOCKER_PASSWORD', 'cs@admin')
