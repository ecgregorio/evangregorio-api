from datetime import datetime, timezone

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Base, User

app = FastAPI()

# CORS middleware
app.add_middleware(
	CORSMiddleware,
	allow_origins=[
		"https://evangregorio.me",
		"https://staging.evangregorio.me"
	],
	allow_credentials=False,
	allow_methods=["GET", "POST"],
	allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.get("/")
def read_root():
	return {
		"message": (
			"Hi! You've entered Evan Gregorio's personal web domain. "
			"It may be barren right now, but soon he will be releasing "
			"some really cool stuff! "
			"Check out my feature page at https://evangregorio.me !"
        	)
	    }

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
	user = User(name=name, email=email)
	db.add(user)
	db.commit()
	db.refresh(user)
	return user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
	users = db.query(User).all()
	return users

# GET stats endpoint
@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
	user_count = db.query(User).count()
 
	return {
		"user_count": user_count,
		"api_status": "ok",
		"generated_at": datetime.now(timezone.utc).isoformat(),
	}