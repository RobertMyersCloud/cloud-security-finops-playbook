Multi-Cloud Architecture Patterns

Pattern 1: Identity Federation
- Central identity provider (Azure AD)
- Access granted to AWS and GCP via federation

Pattern 2: Distributed Workloads
- Compute in AWS
- Analytics in GCP
- Identity and governance in Azure

Pattern 3: Multi-Cloud DR
- Primary workload in AWS
- Backup in Azure

Pattern 4: Data Synchronization
- S3 <-> Blob <-> Cloud Storage

Pattern 5: Centralized Logging
- Send all logs to SIEM (Sentinel, Splunk)

Key Principles:
- Avoid duplicating architectures
- Keep IAM centralized
- Standardize tagging
- Apply Zero Trust across clouds
