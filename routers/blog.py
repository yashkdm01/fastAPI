from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2  # 1. Correct Relative Imports
from ..repository import blog # Import the repository logic

get_db = database.get_db

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

# 2. CREATE (Now Protected 🔒)
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

# 3. GET ALL (Protected 🔒)
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

# 4. GET BY ID (Public? Or add dependency to lock it)
@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Added 'id: int' type hint
    return blog.get_blog_by_id(id, response, db)

# 5. DELETE (Now Protected 🔒)
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

# 6. UPDATE (Now Protected 🔒)
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)