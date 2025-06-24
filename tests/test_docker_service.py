import unittest
from services.docker_service import DockerService
from unittest.mock import patch

class TestDockerService(unittest.TestCase):
    @patch('services.docker_service.requests.get')
    def test_list_images(self, mock_get):
        mock_get.return_value.json.return_value = {"repositories": ["image1", "image2"]}
        docker_service = DockerService()
        images = docker_service.list_images()
        self.assertEqual(images, {"repositories": ["image1", "image2"]})

    @patch('services.docker_service.requests.delete')
    @patch('services.docker_service.requests.get')
    def test_delete_image(self, mock_get, mock_delete):
        mock_get.return_value.json.return_value = {"tags": ["latest"]}
        docker_service = DockerService()
        result = docker_service.delete_image("image1")
        self.assertEqual(result, {"message": "Image deleted successfully"})
