Security Automation Playbooks

Use Case: Auto-Remediate Public S3 Bucket (AWS)
1. Detect public ACL change with Config or EventBridge.
2. Automatically block public access.
3. Notify security via SNS.

Use Case: Auto-Enforce MFA
1. Detect users without MFA.
2. Trigger workflow to enforce MFA.
3. Disable console access after violation threshold.

Use Case: Security Group Hardening
1. Detect port 22 or 3389 exposed to the internet.
2. Replace inbound rule with restricted IP range.
3. Notify user or owner.

Azure Automation:
- Auto-enforce NSG rules
- Auto-enable Defender for Cloud
- Auto-enable Activity Logs
- Auto-disable public IPs
