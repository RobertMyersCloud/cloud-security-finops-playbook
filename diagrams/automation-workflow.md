# Automation and Auto-Remediation Workflow

Event happens in cloud
(example: S3 bucket made public)
           |
           v
+---------------------------+
|  Event Source             |
|  - CloudTrail / Logs      |
|  - Config / Policy        |
+------------+--------------+
             |
             v
+---------------------------+
|  Event Bus / Rule Engine  |
|  - EventBridge / Logic    |
+------------+--------------+
             |
             v
+---------------------------+
|  Automation Function      |
|  - Lambda / Function App  |
|  - Runbook / Workflow     |
+------------+--------------+
             |
   +---------+--------------------------+
   |                                    |
Remediation Action               Notification
- Lock down resource              - Email / Teams
- Revert config                   - Ticket / SIEM
- Tag / move resource
