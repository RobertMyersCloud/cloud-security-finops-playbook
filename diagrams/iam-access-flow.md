```markdown
# IAM Access Flow
+------------------+
|   Principal      |
| (User/Service)   |
+--------+---------+
         |
         v
+------------------+
|  Resource/API    |
|  Request         |
+--------+---------+
         |
         v
+------------------------------+
|  Authorization Evaluation    |
|------------------------------|
| 1. Who are you?              |
|    - Identity / Role         |
| 2. What action?              |
|    - read/write/delete       |
| 3. Which resource?           |
| 4. Policies?                 |
|    - IAM / RBAC / SCP        |
+--------+---------------------+
         |
   +-----+------------------+
   |                        |
   v                        v
Allow                 Access Denied
   |                        |
   v                        v
+-------------+       +-------------+
| Access      |       | Blocked     |
| Granted     |       |             |
+-------------+       +-------------+
