```python
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

def is_bucket_public(bucket_name):
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl.get("Grants", []):
            uri = grant.get("Grantee", {}).get("URI", "")
            if "AllUsers" in uri or "AuthenticatedUsers" in uri:
                logger.info(f"Bucket {bucket_name} is public.")
                return True
        return False
    except Exception as e:
        logger.error(f"Error checking ACL for bucket {bucket_name}: {e}")
        return False

def block_public_access(bucket_name):
    try:
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": True,
                "IgnorePublicAcls": True,
                "BlockPublicPolicy": True,
                "RestrictPublicBuckets": True
            }
        )
        logger.info(f"Blocked public access for {bucket_name}")
    except Exception as e:
        logger.error(f"Error applying remediation: {e}")

def lambda_handler(event, context):
    logger.info("Event received: %s", json.dumps(event))

    detail = event.get("detail", {})
    bucket_name = detail.get("requestParameters", {}).get("bucketName")

    if not bucket_name:
        return {"result": "no bucket found"}

    if is_bucket_public(bucket_name):
        block_public_access(bucket_name)
        return {"result": "remediated", "bucket": bucket_name}

    return {"result": "not public", "bucket": bucket_name}
