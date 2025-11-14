# Least Privilege Policies (AWS + Azure)

Least privilege = minimum necessary permissions.

---

# AWS Policy Best Practices
- Deny-by-default  
- Explicitly allow only required actions  
- Restrict resource ARN scope  
- Use conditional access:
  - MFA required  
  - Specific IP  
  - Specific tags  
  - Specific services  

---

# Azure RBAC Best Practices
- Use built-in roles when possible  
- Avoid Owner assignment  
- Assign roles at lowest possible scope:
  - Resource  
  - Resource Group  
  - Subscription  

---

# Permission Boundaries (AWS)
Use to prevent privilege escalation.

---

# Role Design Pattern
- Admin  
- Operator  
- Read-only  
- Automation  
- Break-glass  

---

# Summary
Least privilege prevents data breaches and minimizes blast radius.
