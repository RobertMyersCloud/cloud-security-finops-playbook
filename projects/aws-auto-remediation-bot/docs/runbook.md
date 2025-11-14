# Runbook – S3 Public Access Auto-Remediation

## Purpose
Explains how the auto-remediation bot prevents public S3 buckets and restores secure settings.

---

## When It Triggers
- Bucket ACL becomes public  
- Public Access Block disabled  
- New bucket created (optional)

---

## What It Does
1. EventBridge receives S3 change event  
2. Lambda evaluates bucket  
3. If public → Block Public Access  
4. Logs activity to CloudWatch  
5. (Optional) Notifies security  

---

## Incident Response Mapping

| Phase | How This Bot Helps |
|-------|---------------------|
| Detection | Real-time via CloudTrail |
| Containment | Automatically blocks access |
| Eradication | Removes insecure settings |
| Recovery | Restores compliant config |
| Lessons Learned | Logs show root cause |

---
