from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

# stage 1
@app.get("/")
async def root():
    return { "name": "This is a CRUD API", "version": "1.0", "endpoints": ["/GET"] }
@app.get("/health")
async def get_status():
    return { "status": "ok"}
# stage 2
tasks = [
    {"id": 1, "title": "Learn FastAPI basics", "done": False},
    {"id": 2, "title": "Build CRUD endpoints", "done": False},
    {"id": 3, "title": "Test with Swagger UI", "done": True},
]
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
# stage 3
class Item(BaseModel):
    id: int
    title: str 
    done: bool 
class ItemCreate(BaseModel):
    title: str

Items: list[Item] = [
    Item(id=1, title="Learn FastAPI basics", done=False),
    Item(id=2, title="Build CRUD endpoints", done=False),
    Item(id=3, title="Test with Swagger UI", done=True),
]
@app.post("/items/", status_code=201)
async def create_item(item: ItemCreate):
    if not item.title.strip():
        return {'error':'bad request'}
     
    maxId = max(item.id for item in Items) + 1
    newItem = Item(id=maxId,title=item.title,done=False)
    Items.append(newItem)
    return Items
