from fastapi import APIRouter,Depends,status,HTTPException,Response
from models.user import User,MFAOption
from schemas import userschema as schemas
from sqlmodel import Session,select
from db.database import get_session,init_db
from typing import List


router = APIRouter(
    prefix="/users",
    tags=['USER']
)

@router.on_event("startup")
def on_startup():
    init_db()


@router.get("/",status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_session)):
    users = db.query(User).all()
    return users


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserCreate)
def create_user(request: User, db: Session = Depends(get_session)):
    mfa_enum_value = MFAOption(request.mfa)
    new_user = request.dict()
    new_user['mfa'] = mfa_enum_value
    db_user = User(**new_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}",status_code=status.HTTP_200_OK)
def get_user(id:int,db: Session = Depends(get_session)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user

@router.delete("/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session = Depends(get_session)):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{user_id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: User, db: Session = Depends(get_session)):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    user_query.update(request.dict(),synchronize_session=False)
    db.commit()
    return user_query.first()
