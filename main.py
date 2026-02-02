from fastapi import FastAPI
import models
from database import engine
from sqlalchemy.orm import Session
from typing import List
from routers import blog, user
from routers import authentication



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)











###################################################################################
# moved all routes to specific route files for better heirarchy and clean code 

# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1) ##### hardcoded id 
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


#get all_blogs
# @app.get("/blog", response_model=List[schemas.ShowBlog], tags=['blogs'])
# def get_all(db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).all()
#     return blog


# @app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
# def get_blog_by_id(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return{'detail': f'Blog with id {id} not found'}
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with id-{id} is not available",
#         )
#     return blog


###############################################


# @app.put("/blog/{id}/update/", status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).update(
#         # {"title": "radha", "body":'krishna'}
#         # {"title": request.title, "body": request.body}
#         request.dict()
#     )
#     db.commit()
#     return "updated"


# @app.put("/blog/{id}/update/", status_code=status.HTTP_202_ACCEPTED)
# def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with id{id} not fonud")
#     blog.update(request.dict())
#     db.commit()
#     return 'updated'

###############################################


# @app.delete("/blog/{id}/delete/", status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def delete_blog(id, db: Session = Depends(get_db)):
#     blog = (
#         db.query(models.Blog)
#         .filter(models.Blog.id == id)
#         .delete(synchronize_session=False)
#     )
#     db.commit()
#     return {"done deletion"}


############################################################ USER MODEL #############################################################

### Using "bcrypt" library for password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post("/user", response_model=schemas.User)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     hashed_password = pwd_context.hash(request.password)
#     new_user = models.User(
#         name=request.name, email=request.email, password=hashed_password
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


### Using "pbkdf2_sha256" library for password hashing

# pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# @app.post("/user", response_model=schemas.User)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     hashed_password = pwd_context.hash(request.password)
#     new_user = models.User(
#         name=request.name, email=request.email, password=hashed_password
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

##########################
# moved cryptContext to seperate file "hashing"

# @app.post("/user", response_model=schemas.ShowUser, tags=['users'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(
#         name=request.name, email=request.email, password= hashing.Hash.pbkdf2_sha256(request.password)
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# @app.get("/user", response_model= List[schemas.ShowUser], tags=['users'])
# def get_all_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=['users'])
# def get_user_by_id(id, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The user with id{id} not found")
#     return user
