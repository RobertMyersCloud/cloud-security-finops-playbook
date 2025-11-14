# FinOps Cost Allocation & Optimization Flow

```text
+--------------------------+
|  Cloud Resources         |
| (VMs, DB, Storage, etc.) |
+------------+-------------+
             |
             v
+--------------------------+
| Tagging & Metadata       |
| - Owner                  |
| - App                    |
| - Environment            |
| - Cost Center            |
+------------+-------------+
             |
             v
+---------------------------+
| Billing / Cost Data       |
| (CUR, Azure Cost Export)  |
+------------+--------------+
             |
             v
+---------------------------+
| Dashboards & Reports      |
| - Power BI                |
| - Cost Explorer           |
+------------+--------------+
             |
             v
+---------------------------+
| Optimization Decisions    |
| - Rightsizing             |
| - Schedules               |
| - Storage Tiering         |
| - Anomaly Review          |
+------------+--------------+
             |
             v
+---------------------------+
| Actions & Guardrails      |
| - Automation              |
| - Budgets / Alerts        |
| - Policy-as-Code          |
+---------------------------+


