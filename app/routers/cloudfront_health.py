from fastapi import APIRouter, HTTPException,status
from app.logic import cloudfront
from app.logic.log import logging
from datetime import datetime


router = APIRouter(prefix="/cloudfront",tags=["cloudfront-routes"])

@router.get("/distributions")
def list_distributions():
    distributions=cloudfront.list_distribution()
    return distributions

@router.get("/distributions/{distribution_id}")
def list_bucket_objects(distribution_id:str):
    id = cloudfront.get_distribution(distribution_id)
    if not id:
        logging.error(f"[{datetime.utcnow()}]:[STATUS_CODE:{status.HTTP_404_NOT_FOUND}]: No bucket with name {distribution_id} exists.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No bucket with name {distribution_id} exists.")   
    return id