import requests
from core.config import Config

class DockerService:
    def __init__(self):
        self.base_url = Config.DOCKER_REGISTRY_URL
        self.auth = (Config.DOCKER_USERNAME, Config.DOCKER_PASSWORD)

    def list_images(self):
        response = requests.get(f"{self.base_url}/v2/_catalog", auth=self.auth)
        response.raise_for_status()
        return response.json()

    def delete_image(self, image_name: str):
        tags_response = requests.get(f"{self.base_url}/v2/{image_name}/tags/list", auth=self.auth)
        tags_response.raise_for_status()
        tags = tags_response.json().get("tags", [])

        for tag in tags:
            delete_response = requests.delete(f"{self.base_url}/v2/{image_name}/manifests/{tag}", auth=self.auth)
            delete_response.raise_for_status()
        
        return {"message": "Image deleted successfully"}
