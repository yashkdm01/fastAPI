from fastapi import APIRouter, Depends, status, HTTPException
import schemas, models
from database import get_db
from sqlalchemy.orm import Session
from typing import List
import hashing
from repository import user as user_repo


router = APIRouter(
    prefix= '/user',
     tags=['Users']
)



#create_user

### Using "bcrypt" library for password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @router.post("/user", response_model=schemas.User, tags=['users])
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

# @router.post("/user", response_model=schemas.User)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     hashed_password = pwd_context.hash(request.password)
#     new_user = models.User(
#         name=request.name, email=request.email, password=hashed_password
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# moved cryptContext to seperate file "hashing"

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # new_user = models.User(
    #     name=request.name, email=request.email, password= hashing.Hash.pbkdf2_sha256(request.password)
    # )
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)

    return user_repo.create_user(request, db)


#get all_users
@router.get("/", response_model= List[schemas.ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    # users = db.query(models.User).all()
    return user_repo.get_all_users(id, db)

#get user_by_id
@router.get("/{id}", response_model=schemas.ShowUser)
def get_user_by_id(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The user with id{id} not found")
    return user_repo.get_user_by_id(id, db)


