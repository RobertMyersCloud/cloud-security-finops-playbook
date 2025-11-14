Cloud Incident Response Lifecycle

Preparation:
- Enable logging: CloudTrail, GuardDuty, Defender for Cloud, Activity Logs.
- Enforce MFA and least privilege.
- Create isolation and quarantine networks.
- Establish playbooks and contacts.

Detection:
- Monitor unusual IAM activity.
- Trigger alerts for login anomalies.
- Detect privilege escalation.
- Monitor public exposure of resources.
- Use AWS GuardDuty and Azure Defender alerts.

Analysis:
- Review logs across IAM, network, compute, and storage.
- Identify source of compromise.
- Determine scope and affected resources.
- Validate whether data was accessed or modified.

Containment:
- Disable affected IAM users or roles.
- Revoke session tokens.
- Isolate compute resources.
- Apply network segmentation or NSG lockdown.

Eradication:
- Remove malicious code or resources.
- Patch vulnerabilities.
- Reset credentials, keys, secrets.
- Correct IAM misconfigurations.

Recovery:
- Redeploy clean workloads.
- Re-enable required services.
- Monitor environment for recurrence.

Lessons Learned:
- Update policies and controls.
- Enhance detection rules.
- Add more automated guardrails.
