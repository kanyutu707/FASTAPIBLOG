from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from Controller import PostController, AuthController
from database import engine, Base
from Controller.AuthController import get_current_active_user

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Include routers
app.include_router(AuthController.router)

# Secure PostController routes
app.include_router(
    PostController.router,
    dependencies=[Depends(get_current_active_user)]
)

# Root endpoint (optional)
@app.get("/")
async def root():
    return {"message": "Welcome to the secured API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)