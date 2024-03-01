from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Just start developement of quiz management system with fastapi."}

