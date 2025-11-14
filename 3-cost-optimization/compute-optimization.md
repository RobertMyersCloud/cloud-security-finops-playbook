# Compute Optimization (AWS + Azure)

Compute is usually 50–70% of total cloud spend. Proper optimization can reduce cost 25–55% depending on environment maturity.

---

# 1. Rightsizing (Highest ROI)

Evaluate:
- CPU utilization
- Memory utilization
- I/O performance
- Network throughput
- Peak vs average usage

Downsize when average utilization <40–50%.

Tools:
- AWS Compute Optimizer
- Azure Advisor
- Dynatrace / Datadog

---

# 2. ARM Architectures (Massive Savings)

Use **Graviton (AWS)** or **Ampere (Azure)**.

Benefits:
- 20–40% lower cost
- Better performance per dollar
- Ideal for:
  - APIs  
  - Containers  
  - Serverless backends  
  - Node.js / Python workloads  

---

# 3. Burstable Instances (T-Series / B-Series)

Use for:
- Development environments
- Low-load websites
- Small internal apps
- Intermittent workloads

Savings: **30–60%**

Instances:
- AWS: t3, t4g
- Azure: B1/B2/B4 series

---

# 4. Savings Plans / Reserved Instances

Rules:
- Cover **baseline** with SP/RIs  
- Leave burst capacity on-demand  
- Monitor utilization monthly  
- Never overcommit >80% baseline  

---

# 5. Spot Instances (70–90% Cheaper)

Best for:
- Containers
- Batch jobs
- ETL
- CI/CD runners
- Stateless compute

Avoid for:
- Stateful DBs
- Critical workloads without fallback

Best practice:
- Use **Spot Fleets** or **Divided ASG pools** (50% on-demand / 50% spot)

---

# 6. Placement, Spread & Cost Patterns (AWS)

### Spread Placement:
High resiliency, higher cost.

### Cluster Placement:
Low latency, high performance.

### Cost-Optimized Mix:
Combine:
- On-demand for baseline
- Spot for burst
- RI/SP for consistent loads

---

# 7. Scheduled Compute Shutdown

Turn off after hours:
- Dev
- Test
- QA
- Analytics

Savings: **40–60%**

---

# Summary

Modern CPUs + rightsizing + spot + proper scaling = the highest compute savings.
