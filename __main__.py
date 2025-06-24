from fastapi import FastAPI
from api.docker_registry import router as docker_registry_router

app = FastAPI()

app.include_router(docker_registry_router, prefix="/docker")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
