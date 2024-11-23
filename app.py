from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import src.main as crews

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to match your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class draft_input(BaseModel):
    title: str

class drafts(BaseModel):
    drafts: str

class post_input(BaseModel):
    drafts: str
    choice: str

class status(BaseModel):
    result: str

@app.options("/drafting")
@app.options("/posting")
async def options_route():
    return {"message": "OK"}

@app.post("/healthcheck")
def health():
    return {"Tweet-Writer Crew Health Check Succesfull"}

@app.post("/drafting", response_model=drafts)
def draft(request: draft_input):
    res = str(crews.draft(request.title))
    return drafts(drafts=res)

@app.post("/posting", response_model=status)
def post(request: post_input):
    res = str(crews.post(request.drafts, request.choice))
    return status(result=res)

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)