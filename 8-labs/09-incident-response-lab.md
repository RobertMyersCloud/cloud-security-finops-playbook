# Lab 9 — Incident Response Simulation

Goal:
Simulate a compromised identity scenario.

## Steps
1. Create IAM user with access key.
2. Trigger suspicious activity:
   - Failed logins
   - API calls from new IP
3. Alerts:
   - GuardDuty → IAM anomaly
   - Defender → brute force
4. Response:
   - Disable key
   - Rotate credentials
   - Lock identity
   - Review logs

## Evidence
- IR alert screenshot
