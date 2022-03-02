from typing import Optional
from fastapi import FastAPI
from kubernetes import client, config


## kubernetes config
config.load_kube_config()
apps_api = client.AppsV1Api()

app = FastAPI()

@app.get("/")
def read_home():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
