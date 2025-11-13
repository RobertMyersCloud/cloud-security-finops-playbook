# Zero Trust Overview

Zero Trust is a security framework built on the principle: **“Never trust, always verify.”**  
Traditional networks assumed trust based on location (inside the perimeter). Zero Trust eliminates that assumption entirely.

This document summarizes the core pillars, concepts, and cloud-security relevance of Zero Trust.

---

## What Zero Trust Solves
Modern environments face:
- Remote users
- Cloud-hosted applications
- Increased identity-based attacks
- Hybrid environments
- Lateral movement risk

Zero Trust reduces the blast radius of breaches and ensures every user, device, and request is verified.

---

## Core Principles

### 1. Verify Explicitly
Always authenticate and authorize based on:
- Identity
- Device health
- Location
- Data sensitivity
- Risk signals
- Real-time context

### 2. Use Least Privilege Access
- JIT (Just-in-Time) access  
- JEA (Just Enough Access)  
- Privileged Identity Management  
- Role-based & attribute-based access controls  
- Removal of standing admin privileges  

### 3. Assume Breach
Design your environment *as if attackers are already inside*:
- Micro-segmentation
- Logging & monitoring
- Lateral movement prevention
- Strong containment boundaries

---

## Zero Trust Pillars (Microsoft Model)

1. **Identity**  
   The primary control plane — users, service accounts, workloads.

2. **Devices**  
   Ensure only compliant and secure devices can access resources.

3. **Apps**  
   Enforce secure access to SaaS, PaaS, and local applications.

4. **Infrastructure**  
   Secure cloud resources, servers, containers, and workloads.

5. **Network**  
   Micro-segmentation, least-privilege routing, encrypted traffic.

6. **Data**  
   Classification, labeling, encryption, access monitoring.

---

## Why Zero Trust Matters in Cloud Security Roles

- Identity is now the #1 attack vector.
- Cloud removes the traditional perimeter.
- Multi-cloud = increased attack surface.
- FinOps & cost governance rely on controlled, secure access.
- Cloud governance frameworks (AWS CAF, Azure CAF) assume Zero Trust foundations.

---

## How My Background Aligns
My Navy and federal background maps directly to Zero Trust:
- Verification of identity (SCIF access)
- Access control and clearance levels
- Insider threat prevention
- Audit and compliance mindset
- Risk mitigation and incident response
- Enforcing least privilege through DoD directives

---

## Summary
Zero Trust is the security backbone of all modern cloud environments.  
This folder contains my working knowledge, checklists, and architecture guides that reflect how I apply Zero Trust principles to cloud environments.
