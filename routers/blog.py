from fastapi import APIRouter, Depends, Response, status, HTTPException
import schemas, models, database
from database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


#create blog
@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def get_blog_by_id(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{'detail': f'Blog with id {id} not found'}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id-{id} is not available",
        )
    return blog


#get all_blogs
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog


#get_blog_by_id
@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def get_blog_by_id(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{'detail': f'Blog with id {id} not found'}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id-{id} is not available",
        )
    return blog


#update_blog
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update(
        # {"title": "radha", "body":'krishna'}
        # {"title": request.title, "body": request.body}
        request.dict()
    )
    db.commit()
    return "updated"


#delete_blog
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = (
        db.query(models.Blog)
        .filter(models.Blog.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    return {"done deletion"}