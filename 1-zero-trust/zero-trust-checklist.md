# Zero Trust Checklist

A practical, industry-aligned Zero Trust checklist mapped across identity, devices, networks, applications, data, and infrastructure.  
This version includes maturity guidance and implementation notes used by real security teams.

---

## Identity (Primary Control Plane)

- [ ] MFA enforced for all accounts  
- [ ] Conditional Access policies in place  
- [ ] Passwordless supported or planned  
- [ ] No standing global admin privileges  
- [ ] Privileged Identity Management (JIT/JEA)  
- [ ] Access reviews conducted regularly  
- [ ] Service accounts replaced with managed identities  
- [ ] Separate admin accounts (no dual-purpose identities)  
- [ ] Strong session controls & token lifetime settings  

---

## Devices

- [ ] Device compliance policies defined (Windows/Linux/macOS)  
- [ ] Unmanaged devices restricted or blocked  
- [ ] Endpoint security required (EDR/AV)  
- [ ] Device health evaluated at sign-in  
- [ ] OS patching cadence enforced  
- [ ] Compromised devices trigger Conditional Access blocks  

---

## Network

- [ ] Micro-segmentation implemented  
- [ ] No ANY-ANY firewall rules  
- [ ] Private endpoints for sensitive workloads  
- [ ] Admin access via secure jump hosts/bastions  
- [ ] All traffic encrypted  
- [ ] East-West traffic monitored  

---

## Apps

- [ ] SSO for all SaaS and internal apps  
- [ ] OAuth permission reviews  
- [ ] Shadow IT monitoring implemented  
- [ ] App-to-app authentication via managed identities  
- [ ] Sensitive apps require step-up authentication  

---

## Data

- [ ] Data classification & labeling in place  
- [ ] Encryption in transit and at rest  
- [ ] DLP policies enforced  
- [ ] Access to sensitive data logged  
- [ ] Data minimization principles applied  

---

## Infrastructure

- [ ] CIS/NIST baselines for cloud resources  
- [ ] Logging enabled for all cloud services  
- [ ] Vulnerability management program active  
- [ ] Infrastructure drift detection  
- [ ] Production access restricted & monitored  
- [ ] Secrets management (no plaintext credentials)  

---

## Monitoring & Response

- [ ] SIEM integrated with identity, endpoint, and cloud logs  
- [ ] Alerts for anomalous sign-ins and privileged activity  
- [ ] Incident response playbooks maintained  
- [ ] Threat intelligence integrated  
- [ ] Regular tabletop exercises conducted  

---

## Governance & Policy

- [ ] Zero Trust policies published and approved  
- [ ] Exception process defined  
- [ ] Quarterly control reviews  
- [ ] Risk register used to track Zero Trust gaps  
- [ ] Cloud baselines documented  

---

## Maturity Model (Crawl → Walk → Run)

### **Crawl**
- MFA everywhere  
- Logging enabled  
- Basic identity cleanup  
- First segmentation policies  

### **Walk**
- Conditional Access  
- PIM/JIT  
- Endpoint compliance  
- DLP  
- SIEM with real alerts  

### **Run**
- Continuous Access Evaluation  
- Automated remediation (SOAR)  
- Full identity governance  
- Advanced segmentation  
- Data access governance at scale  

---

## How to Use This Checklist

Teams typically add:
- Status (Not Started / In Progress / Complete)  
- Owner (Security, IAM, Cloud Ops)  
- Notes / Risks / Dependencies  

This document can feed a formal **Zero Trust roadmap**.

---

## Summary

This checklist supports Zero Trust assessments and guides real-world security architecture decisions across cloud identity, access, devices, and governance.

