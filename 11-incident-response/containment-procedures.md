Containment Procedures

Identity Containment:
- Disable affected accounts.
- Revoke session tokens.
- Rotate access keys and passwords.
- Remove high-risk roles or permissions.

Network Containment:
- Move resources to quarantine network.
- Apply deny-all NSG or security group rules.
- Block outbound internet access.

Compute Containment:
- Snapshot current state.
- Stop instance to prevent further damage.
- Remove IAM role permissions.

Storage Containment:
- Lock bucket or container ACLs.
- Enable object-level versioning.
- Restrict public access immediately.
