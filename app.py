from fastapi import FastAPI
from pydantic import BaseModel  # pylint: disable=no-name-in-module
import src.main as crew

app = FastAPI()

class crew_input(BaseModel):
    title: str

class output(BaseModel):
    report:str

@app.post("/health")
def health():
    return {"Health Check Success"}

@app.post("/drafting", response_model=output)
def draft(request: crew_input):
    res = str(crew.run(request.title))
    return output(report=res)
