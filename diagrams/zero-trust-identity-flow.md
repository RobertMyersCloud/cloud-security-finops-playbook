# Zero Trust Identity Flow

User login request
        |
        v
+-------------------------+
|   Identity Provider     |
|   (Entra ID / IdP)      |
+-------------------------+
        |
        | 1. Check credentials
        | 2. Evaluate Conditional Access
        |    - User risk
        |    - Sign-in risk
        |    - Device compliance
        |    - Location / network
        |
        v
+-------------------------+
|   Access Decision       |
+-------------------------+
        |
   +----+-----------------------------+
   |                                  |
Allow with conditions          Block / Require MFA
   |                                  |
   v                                  v
+------------------+            +-----------------+
| Access token /   |            |   Access Denied |
| session granted  |            +-----------------+
+--------+---------+
         |
         v
+--------------------------+
| App / API / Cloud        |
| (AWS, Azure, SaaS)       |
+--------------------------+
