Identity Comparison (AWS vs Azure vs GCP)

AWS:
- Service: IAM
- Identity Types: Users, Roles, Policies, Service Accounts
- Strength: Highly granular permissions
- Weakness: No built-in Zero Trust; requires add-ons

Azure:
- Service: Entra ID
- Identity Types: Users, Groups, Roles, Workloads, Service Principals
- Strength: Zero Trust and Conditional Access built-in
- Weakness: Complex for beginners

GCP:
- Service: IAM
- Identity Types: Users, Groups, Service Accounts
- Strength: Lightweight and simple
- Weakness: Less granular than AWS

Multi-Cloud Mapping:
- Roles in all clouds control access
- Policies = AWS vs Azure RBAC vs GCP Roles
- Conditional Access only native in Azure
- Service principal = AWS role = GCP service account
