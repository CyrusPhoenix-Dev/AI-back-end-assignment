from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return { "name": "This is a CRUD API", "version": "1.0", "endpoints": ["/GET"] }
@app.get("/health")
async def get_status():
    return { "status": "ok"}