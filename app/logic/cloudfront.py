import boto3
from datetime import datetime
from .log import logging


client = boto3.client('cloudfront')


def list_distribution():
    response = client.list_distributions(
        MaxItems='4'
    )
    DistributionList=[]
    for i in range(0,4):
        DistributionList.append(response["DistributionList"]["Items"][i]["ARN"])
    return DistributionList

def get_distribution(distributionid:str):
    try:
        response = client.get_distribution(
            Id = distributionid
        )
    except Exception:
        logging.error(f"[{datetime.utcnow()}]: Exception occured while getting distribution details:{distributionid} not found.")
    #return {"Id": response["Distribution"]["Id"],"comment": response["Distribution"]["DistributionConfig"]["Comment"]}
    return response