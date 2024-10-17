from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from Service import PostService
from database import get_db

router = APIRouter()

@router.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostService.PostBase, db: Session = Depends(get_db)):
    return await PostService.create_post(post, db)

@router.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: Session = Depends(get_db)):
    return await PostService.read_post(post_id, db)

@router.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    return await PostService.delete_post(post_id, db)