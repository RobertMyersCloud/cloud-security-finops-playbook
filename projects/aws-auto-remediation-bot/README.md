# AWS Auto-Remediation Bot (S3 Public Access)

This security project automatically detects when an S3 bucket becomes public and immediately remediates it.

This shows:
- Cloud security automation (EventBridge + Lambda)
- IAM least privilege design
- Infrastructure drift correction
- Real-world security engineering skills

This bot:
1. Detects public S3 bucket changes (ACL / policies).
2. Blocks public access.
3. Logs the remediation.
4. (Optional) Sends notifications.

This project connects directly to:
- Zero Trust
- Cloud Governance
- Incident Response
- IAM & Security
- Automation Playbooks

Below you will find:
- Architecture diagram
- Lambda function code
- EventBridge rule example
- IAM policy
- Sample AWS event
- Documentation
