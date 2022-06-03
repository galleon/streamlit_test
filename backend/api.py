from fastapi import Depends, FastAPI, File, Form, Query, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image
from pydantic import BaseModel, Field, SecretStr
from pydantic.dataclasses import dataclass

from typing import List, Optional, Tuple

from random import random

DEFAULT_DETR_TAGS = []

# Push that in a configuration file

app = FastAPI()  # root_path="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/viroid")
def viroid(sequence: str):
    return {"prob": random()}


@app.post("/equation")
async def equation(file: Optional[UploadFile] = None):

    if not file:
        return {"ok": False}

    tick = time.time()

    image = Image.open(file.file)


    # do something smart with the image an return it

    return {"latex": "\\frac{a}{b}"}
