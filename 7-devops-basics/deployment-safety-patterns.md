# Deployment Safety Patterns

Used to reduce the risk of production outages.

## 1. Blue/Green Deployments
Two identical environments:
- Blue = current
- Green = new version

Switch traffic when stable.

## 2. Canary Deployments
Release to a small % of users first.

## 3. Feature Flags
Turn features on/off without deployments.

## 4. Rollback Patterns
Automated rollback on:
- health check failures
- error spikes
- failed policies
