import uuid 
from typing import Optional 
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks, status
from sqlalchemy.orm import Session

from db.database import get_db
from models.job import StoryJob
from schemas.job import StoryjobResonse

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.get(path="/{job_id}", response_model=StoryjobResonse)
def get_job_status(job_id: str,db: Session = Depends(get_db)):

     job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
     if not job:  
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=(f"job NOT FOUND !!!"))
     return job