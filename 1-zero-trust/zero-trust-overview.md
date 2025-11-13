# Zero Trust Overview

Zero Trust is a security framework built on the principle **“Never trust, always verify.”**  
It shifts security from perimeter-based assumptions to continuous identity, device, and risk evaluation across every access request.

This overview reflects guidance from **NIST SP 800-207**, Microsoft, AWS, and modern cloud-security design.

---

## Why Zero Trust Exists

Traditional castle-and-moat security breaks down in modern environments due to:
- Remote/hybrid workforce
- Multi-cloud adoption
- Identity-based attacks
- Lateral movement threats
- SaaS & external integrations
- Increasing insider risk

Zero Trust reduces attack surface by evaluating *every* authentication and authorization event.

---

## Core Principles (Industry Standard)

### **1. Verify Explicitly**
Continuously validate:
- User identity
- Device compliance
- Location
- Risk score
- Data sensitivity
- Real-time context

### **2. Least Privilege Access**
- JIT (Just-In-Time)
- JEA (Just Enough Access)
- RBAC/ABAC
- Scoped permissions
- Removal of standing privileges

### **3. Assume Breach**
Operate as if attackers are already present:
- Micro-segmentation
- Continuous monitoring
- Lateral movement prevention
- Containment and isolation controls

---

## Zero Trust Pillars (Microsoft Model)

1. **Identity** – authentication, authorization, lifecycle management  
2. **Devices** – compliance, health, endpoint security  
3. **Network** – segmentation, encryption, access control  
4. **Applications** – SSO, app registration, OAuth governance  
5. **Infrastructure** – secure configuration, workload protection  
6. **Data** – classification, labeling, encryption, DLP  

---

## Standards & Reference Models

This Zero Trust approach aligns with:

- **NIST SP 800-207 – Zero Trust Architecture**
- **Microsoft Zero Trust Framework**
- **AWS Zero Trust Guiding Principles**
- **Google BeyondCorp Model**

Referencing these standards signals that the implementation is vendor-neutral and aligned with industry best practices.

---

## Zero Trust as a Journey (Crawl → Walk → Run)

Zero Trust is implemented in stages:

### **Crawl**
- MFA everywhere  
- Logging enabled  
- Basic segmentation  
- Initial identity cleanup  

### **Walk**
- Conditional Access  
- Device compliance enforcement  
- Privileged Identity Management  
- DLP policies  
- Centralized SIEM  

### **Run**
- Continuous Access Evaluation  
- Automated remediation (SOAR)  
- Identity Governance at scale  
- Advanced segmentation  
- Data-centric access controls  

---

## Common Zero Trust Use Cases

- Protecting privileged/admin accounts  
- Securing access to financial or sensitive systems  
- Reducing lateral movement across workloads  
- Third-party vendor access  
- Remote access without VPN reliance  
- Protecting regulated data (HIPAA, CJIS, PCI, etc.)  

---

## How My Background Aligns

My Navy, Federal, and Aerospace experience maps directly to Zero Trust:
- Identity vetting (SCIF, clearance, background checks)
- Access control across secure facilities
- Enforcing least privilege & separation of duties
- Incident response & risk mitigation
- Compliance with strict federal standards
- Operational security (OPSEC) & insider threat awareness

---

## Summary

Zero Trust is the foundation of modern cloud security.  
This overview serves as the conceptual backbone for architecture, governance, IAM, and real-world cloud security practices documented in this repo.
