from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import get_db
from typing import List

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)
 
def get_all(db: Session):
    blog = db.query(models.Blog).all()
    return blog

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body= request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog_by_id(id, response: Response,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{'detail': f'Blog with id {id} not found'}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id-{id} is not available",
        )
    return blog

def update_blog(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with id{id} not fonud")
    blog.update(request.dict())
    db.commit() 
    return 'updated'


def delete_blog(id, db: Session):
    blog = (
        db.query(models.Blog)
        .filter(models.Blog.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    return {"done deletion"}