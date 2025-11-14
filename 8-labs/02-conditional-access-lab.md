# Lab 2 — Zero Trust Conditional Access (Azure)

Goal:
Require MFA + compliant device + block legacy authentication.

## Steps
1. Azure Entra → Security → Conditional Access.
2. New Policy:
   - Users: test group
   - Cloud apps: All
3. Conditions:
   - Device platform: Windows
   - Locations: All
   - Client apps: Block legacy
4. Access Controls:
   - Require MFA
   - Require compliant device

## Evidence
- Policy screenshot
- MFA prompt screen
- Blocked login from non-compliant device
