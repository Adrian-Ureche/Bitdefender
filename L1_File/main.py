from fileinput import filename
from typing import Optional

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import uvicorn


app = FastAPI()


@app.post("/AddFiles")
async def create_file(file: UploadFile) -> dict[str, str]:
    return {"filename", file.filename}


if __name__ == '__main__':
    uvicorn.run(app)
