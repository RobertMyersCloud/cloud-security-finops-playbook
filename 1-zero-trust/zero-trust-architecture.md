# Zero Trust Architecture

This document provides the architectural view of Zero Trust as defined by NIST SP 800-207 and major cloud vendors.  
It focuses on identity, segmentation, access policies, and continuous evaluation — the pillars of modern cloud defense.

---

## High-Level Architecture Flow

User → Identity Provider (IdP) → Device Evaluation → Conditional Access → Application → Data  
Every step is logged, evaluated, and re-evaluated continuously.

---

## Core Architectural Concepts

### **1. Identity as the Control Plane**
Identity is the primary security boundary.

Key patterns:
- Centralized identity provider (Entra ID / AWS IAM Identity Center)
- Strong authentication (MFA, FIDO2, passwordless)
- Just-In-Time privileged elevation
- Role- and attribute-based access control (RBAC/ABAC)
- Identity lifecycle management

---

### **2. Micro-Segmentation**
Lateral movement is the #1 failure of old perimeters.  
Zero Trust uses segmentation at multiple layers:

- Application segmentation  
- User segmentation  
- Environment segmentation (Prod vs Dev/Test)  
- Workload-based segmentation  
- Network isolation using NSGs, firewalls, and routing restrictions  

Default stance: **deny-by-default**.

---

### **3. Device Posture Enforcement**
Access decisions incorporate device trust:

- OS version  
- Patch status  
- EDR/AV state  
- Health certificate  
- Compliance policies  
- Jailbreak/root detection  

Zero Trust means **identity alone is not enough**.

---

### **4. Continuous Access Evaluation**
Authorization is re-checked automatically when:
- Risk score increases  
- User location changes  
- Token age exceeds threshold  
- Suspicious behavior detected  
- Device becomes non-compliant  

This prevents “set it and forget it” sessions.

---

### **5. Least Privilege Everywhere**
Zero Trust applies least privilege at all layers:

- No standing admin privileges  
- JIT/JEA workflows  
- Scoped admin roles  
- API permission minimization  
- Access reviews and certifications  
- Privileged Identity Management  

---

### **6. Telemetry, Logging, and Visibility**
Zero Trust requires full end-to-end visibility:

- Identity logs (sign-in, risk events)
- Conditional Access logs
- Network logs (firewalls, flow logs)
- Device logs
- Application logs
- Data access logs
- Privileged activity logs

All feeds into a **SIEM** or **SOAR** system.

---

## Policy Decision & Enforcement (NIST SP 800-207)

Zero Trust separates **decision** from **enforcement**:

### **Policy Decision Point (PDP)**
Evaluates:
- Identity  
- Device  
- Policy  
- Risk  
- Context  

Examples:
- Conditional Access engine  
- Identity provider risk engine  
- Cloud Access Security Broker (CASB)  

### **Policy Enforcement Point (PEP)**
Applies the decision and enforces access rules.

Examples:
- Application gateway  
- API gateway  
- Reverse proxy  
- Firewall  
- Workload identity boundary  

---

## Practical Controls in Cloud Environments

Zero Trust architecture uses multiple cloud-native controls:

- Conditional Access / SCPs / IAM policies  
- Private endpoints  
- RBAC/ABAC  
- Network Security Groups (NSGs)  
- Managed Identities  
- Logging/monitoring agents  
- DLP policies  
- Key Vault / KMS for secrets  

---

## Tradeoffs & Considerations

- **Complexity:** More components → need for governance & automation  
- **User Experience:** Poorly tuned policies can over-restrict users  
- **Legacy Dependencies:** Older apps may need compensating controls  
- **Cultural Shift:** Requires org-wide acceptance of least privilege  
- **Visibility:** Must have complete logging before enforcing strict controls  

---

## Example Zero Trust Access Scenario (Cloud)

1. User attempts access  
2. IdP checks:
   - MFA  
   - Device compliance  
   - Location  
   - Risk signals  
3. Conditional Access evaluates:
   - Resource sensitivity  
   - User role  
   - Session risk  
4. Access granted with least privilege  
5. Continuous monitoring evaluates activity  
6. If risk increases, access is revoked or revalidated  
7. All activity logged for audit and incident response  

---

## Summary

This architecture reflects modern Zero Trust as implemented across Azure, AWS, and hybrid environments.  
It demonstrates identity-centric security, continuous verification, segmented workloads, and policy-driven access decisions — the core of cloud security architecture.
