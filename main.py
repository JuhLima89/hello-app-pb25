from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Project CI/CD PB25"}