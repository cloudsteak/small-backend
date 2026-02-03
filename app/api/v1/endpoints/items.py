from typing import Any, List
from fastapi import APIRouter, HTTPException
from app.schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter()

# Mock data store
items = [
    {"id": 1, "title": "First Item", "description": "This is the first item"},
    {"id": 2, "title": "Second Item", "description": "This is the second item"},
]

@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve items.
    """
    return items[skip : skip + limit]

@router.post("/", response_model=Item)
def create_item(item_in: ItemCreate) -> Any:
    """
    Create new item.
    """
    new_item = {
        "id": len(items) + 1,
        "title": item_in.title,
        "description": item_in.description,
    }
    items.append(new_item)
    return new_item

@router.get("/{id}", response_model=Item)
def read_item(id: int) -> Any:
    """
    Get item by ID.
    """
    for item in items:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
