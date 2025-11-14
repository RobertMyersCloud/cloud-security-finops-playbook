# Networking Optimization (AWS + Azure)

Networking is often overlooked — but NAT Gateway, cross-region traffic, and logging are MASSIVE cost drivers.

---

# 1. NAT Gateway → VPC Endpoint Replacement (High ROI)

NAT Gateway costs can exceed $1,000–$5,000/mo if misused.

Replace with:
- S3 Gateway Endpoint  
- DynamoDB Endpoint  
- Interface Endpoints (only when needed)

Savings: **70–90%**

---

# 2. Reduce Cross-Region Traffic

Most expensive transfer path.

Mitigate:
- Keep compute + storage in same region
- Cache via CloudFront/Azure CDN
- Avoid cross-region replication unless required

---

# 3. Private Endpoints Everywhere

Use:
- AWS PrivateLink
- Azure Private Endpoints

Benefits:
- Lower cost  
- Higher security  
- No public egress charges  

---

# 4. Load Balancer Optimization

- Remove idle ALBs  
- Combine LBs for low-traffic apps  
- Downgrade tiers where needed  
- Use NLB instead of ALB for TCP workloads  

---

# 5. Logging Optimization

CloudWatch logs → VERY expensive  
Azure Monitor logs → VERY expensive

Optimize:
- Retention period  
- Exclusion filters  
- Sampling  
- Use S3/Blob tiering  

---

# Summary

Networking optimization saves money by reducing egress and eliminating NAT gateway overuse.
