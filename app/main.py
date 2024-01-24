from fastapi import FastAPI
from app.routers import s3health, cloudfront_health


app = FastAPI()

app.include_router(s3health.router)
app.include_router(cloudfront_health.router)