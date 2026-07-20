from fastapi import FastAPI

tasks = [
    {"id": 1, "title": "Learn FastAPI basics", "done": False},
    {"id": 2, "title": "Build CRUD endpoints", "done": False},
    {"id": 3, "title": "Test with Swagger UI", "done": True},
]

app = FastAPI()


@app.get("/")
async def root():
    return { "name": "This is a CRUD API", "version": "1.0", "endpoints": ["/GET"] }
@app.get("/health")
async def get_status():
    return { "status": "ok"}

@app.get("/tasks/{url_id}")
def get_task(url_id):
    if url_id.isdigit():
        for task in tasks:
            if task["id"] == int(url_id):
                return task
    error = f"'Task {url_id} not found"
    return {"error": error }
        
@app.get("/tasks")
def get_tasks():
    return tasks
