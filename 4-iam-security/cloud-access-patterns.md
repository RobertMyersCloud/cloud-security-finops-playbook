# Cloud Access Patterns

Common identity access patterns in AWS & Azure.

---

# 1. Federated Access (SSO)
Use:
- Azure Entra ID  
- AWS IAM Identity Center  
- Okta  

Benefits:
- No local passwords  
- Central identity store  
- Unified access revocation  

---

# 2. Assume Role (AWS)
Pattern:
User → SSO → Assume Role → Short-lived credentials

Highly secure, no long-lived keys.

---

# 3. Managed Identities (Azure)
Used for:
- VMs  
- Functions  
- Containers  
- Automation  

Removes need for secrets.

---

# 4. Service Identity Patterns
AWS:
- IAM Roles for EC2  
- IAM Roles for Lambda  
- ECS Task Roles  
- EKS IRSA (K8s)  

Azure:
- System-assigned MI  
- User-assigned MI  

---

# Summary
Federated identities + short-lived credentials = secure access patterns.
