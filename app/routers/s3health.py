from fastapi import APIRouter, HTTPException,status
from app.logic import s3
from app.logic.log import logging
from datetime import datetime


router = APIRouter(prefix="/s3",tags=["s3-routes"])

@router.get("/buckets")
def list_buckets():
    buckets=s3.list_buckets()
    return buckets

@router.get("/buckets/{bucket_name}")
def list_bucket_objects(bucket_name:str):
    objects = s3.list_bucket_objects(bucket_name)
    if not objects:
        logging.error(f"[{datetime.utcnow()}]:[STATUS_CODE:{status.HTTP_404_NOT_FOUND}]: No bucket with name {bucket_name} exists.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No bucket with name {bucket_name} exists.")   
    return objects
