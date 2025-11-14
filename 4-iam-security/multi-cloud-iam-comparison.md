# Multi-Cloud IAM Comparison (AWS vs Azure)

This file compares IAM models across AWS and Azure.

---

# AWS Identity Model
- IAM  
- IAM Identity Center  
- Resource-level policies  
- AssumeRole pattern  
- Action-based permissions  

---

# Azure Identity Model
- Entra ID (central plane)
- Subscription/RG/Resource scopes  
- RBAC  
- Conditional Access  
- PIM (Just-in-Time)  

---

# Key Differences
AWS = Action-based  
Azure = Role-based  

AWS = AssumeRole  
Azure = Role Assignment  

AWS = Federate into accounts  
Azure = Tenant-based access control  

---

# Summary
AWS and Azure operate differently, but both follow Zero Trust principles.
