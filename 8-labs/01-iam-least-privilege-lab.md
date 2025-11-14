# Lab 1 — IAM Least Privilege (AWS + Azure)

Goal:
Create a least-privilege identity that can only read S3/Blob Storage.

## Steps — AWS
1. Create IAM Policy:
   - Allow: s3:GetObject
   - Resource: specific bucket
2. Create IAM Role or User
3. Attach policy
4. Test access with AWS CLI
5. Validate access denied to other buckets

## Steps — Azure
1. Create a custom RBAC role
2. Assign role to user/service principal
3. Limit scope to 1 storage account
4. Test via Azure CLI

## Evidence to Capture
- Policy JSON
- Failed access attempts
- Successful limited access
