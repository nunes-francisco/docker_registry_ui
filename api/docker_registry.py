from fastapi import APIRouter, HTTPException
from services.docker_service import DockerService

router = APIRouter()
docker_service = DockerService()

@router.get("/images")
def get_images():
    try:
        images = docker_service.list_images()
        return images
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/images/{image_name}")
def delete_image(image_name: str):
    try:
        result = docker_service.delete_image(image_name)
        return result
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
