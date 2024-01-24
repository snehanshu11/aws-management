from fastapi import APIRouter, HTTPException
from app.logic import s3


router = APIRouter(prefix="/health/s3",tags=["health-check"])

@router.get("/buckets")
def list_buckets():
    buckets=s3.list_buckets()
    return buckets

@router.get("/buckets/{bucket_name}")
def list_bucket_objects(bucket_name:str):
    objects = s3.list_bucket_objects(bucket_name)
    if not objects:
        raise HTTPException(status_code=404, detail=f"No bucket with name {bucket_name} exists.")
    return objects
