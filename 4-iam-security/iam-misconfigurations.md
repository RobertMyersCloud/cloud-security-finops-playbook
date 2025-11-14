# Common IAM Misconfigurations

Most cloud breaches occur due to IAM mistakes.

---

# 1. Wildcard Permissions (“*”)
Never:
- "Action": "*"
- "Resource": "*"

---

# 2. Unrestricted Trust Policies (AWS)
Never:
- Principal: "*"

Restrict to specific IAM identities or accounts.

---

# 3. No MFA for Admin Roles
Require MFA on:
- Admin  
- Security  
- Root/Owner  

---

# 4. Stale Access Keys
Delete keys unused > 60–90 days.

---

# 5. Shared Admin Accounts
Never share:
- break-glass  
- admin  
- privileged identities  

---

# 6. Service Accounts with Human Privileges
Service identities should NEVER:
- log into console  
- have admin roles  

---

# Summary
Misconfigurations are the #1 real-world cloud attack vector.
