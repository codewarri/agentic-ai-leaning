from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Daily Tasks API",
    description="API to retrieve daily tasks",
    version="1.0.0"
)

# ----------------------------
# Pydantic Models
# ----------------------------

class Task(BaseModel):
    id: int = Field(..., description="Unique identifier for the task")
    title: str = Field(..., description="Short title of the task")
    description: str = Field(..., description="Detailed description of the task")
    completed: bool = Field(..., description="Completion status of the task")

# ----------------------------
# Sample Data (Mock Database)
# ----------------------------

tasks_db = [
    Task(id=1, title="Morning workout", description="30 minutes cardio", completed=False),
    Task(id=2, title="Read book", description="Read 20 pages of a book", completed=False),
    Task(id=3, title="Code practice", description="Solve 2 coding problems", completed=True),
]

# ----------------------------
# GET Endpoint
# ----------------------------

@app.get(
    "/tasks",
    response_model=List[Task],
    summary="Get Daily Tasks",
    description="Retrieve the full list of daily tasks",
    tags=["Tasks"]
)
def get_tasks():
    """
    Returns the list of daily tasks.
    """
    return tasks_db
