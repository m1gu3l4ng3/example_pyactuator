from fastapi import FastAPI
from pyactuator_example.config.app_settings import BaseSettingsApp
from pyctuator.pyctuator import Pyctuator

base_settings_app = BaseSettingsApp()

app = FastAPI(
    title=base_settings_app.app_name,
    version=base_settings_app.app_version
)

py_actuator = Pyctuator(
    app,
    "Example pyactuator",
    app_url="http://localhost:8000",
    pyctuator_endpoint_url="http://localhost:8000/pyactuator",
    registration_url=""
)



@app.get("/")
async def hello() -> dict:
    return {"hello": "world"}

@app.get("/health/liveness")
async def liveness() -> dict:
    return {"liveness": "ok"}