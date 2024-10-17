from pydantic import BaseModel
from Models.Post import Post
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

async def create_post(post: PostBase, db: Session):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

async def read_post(post_id: int, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

async def delete_post(post_id: int, db: Session):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}