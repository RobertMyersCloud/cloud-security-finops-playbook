# Three-Tier Cloud Architecture

```text
           +----------------------+
           |        Users         |
           +-----------+----------+
                       |
                       v
          +------------------------+
          |   Web / Front-End      |
          | (ALB / App Gateway)    |
          +-----------+------------+
                       |
                       v
          +------------------------+
          |   Application Layer    |
          | (App Service / ECS)    |
          +-----------+------------+
                       |
                       v
          +------------------------+
          |     Database Layer     |
          | (RDS / Azure SQL etc.) |
          +------------------------+

Security:
- Public entry ONLY at web tier
- App + DB in private subnets
- WAF at the edge
- Secrets in Key Vault / Secrets Manager
