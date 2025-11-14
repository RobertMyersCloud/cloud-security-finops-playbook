```markdown
# Architecture – AWS Auto-Remediation Bot

This bot monitors S3 bucket permission changes and fixes them automatically.

---

## Flow Diagram


    S3 Bucket Config Change
               |
               v
       CloudTrail Event
               |
               v
        EventBridge Rule
               |
               v
     Lambda Auto-Remediator
               |
               v
    - Detect public bucket
    - Enforce Block Public Access
    - Log + notify
