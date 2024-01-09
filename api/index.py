from fastapi import HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session

from uuid import UUID

from .data._db_config import get_db
from .models._todo_crud import TODOBase, TODOResponse
from .service._todos_crud import create_todo_service, get_todo_by_id_service, get_all_todos_service, full_update_todo_service, partial_update_todo_service, delete_todo_data


app = FastAPI(
    title="FastAPI Backend",
    description="This is a backend application built with FastAPI.",
    tags=["Main Route"]
)

# Get ALL TODOS
@app.get("/api/todos", response_model=list[TODOResponse])
def get_todos(db: Session = Depends(get_db)):
    try:
        return get_all_todos_service(db)
    except Exception as e:
        # Handle specific exceptions with different HTTP status codes if needed
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# Get a Single TODO item
@app.get("/api/todos/{todo_id}", response_model=TODOResponse)
def get_todo_by_id(todo_id: UUID, db: Session = Depends(get_db)):
    try:
        return get_todo_by_id_service(todo_id, db)
    except HTTPException as e:
        # If the service layer raised an HTTPException, re-raise it
        raise e
    except Exception as e:
        # Handle specific exceptions with different HTTP status codes if needed
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# Create a new TODO item
@app.post("/api/todos", response_model=TODOResponse)
def create_todo(todo: TODOBase, db: Session = Depends(get_db)):
    try:
        return create_todo_service(todo, db)
    except Exception as e:
        # Handle specific exceptions with different HTTP status codes if needed
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# Update a Single TODO item Completly


@app.put("/api/todos/{todo_id}", response_model=TODOResponse)
def update_todo(todo_id: UUID, updated_todo: TODOBase, db: Session = Depends(get_db)):
    try:
        return full_update_todo_service(todo_id, updated_todo, db)
    except Exception as e:
        # Handle specific exceptions with different HTTP status codes if needed
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# Update a Single TODO item partially
@app.patch("/api/todos/{todo_id}", response_model=TODOResponse)
def update_todo_partial(todo_id: UUID, updated_todo: TODOBase, db: Session = Depends(get_db)):
    try:
        return partial_update_todo_service(todo_id, updated_todo, db)
    except Exception as e:
        # Handle specific exceptions with different HTTP status codes if needed
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# DELETE a single TODO item
@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: UUID, db: Session = Depends(get_db)):
    try:
        return delete_todo_data(todo_id, db)
    except Exception as e:
        # Handle specific exceptions with different HTTP status codes if needed
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
