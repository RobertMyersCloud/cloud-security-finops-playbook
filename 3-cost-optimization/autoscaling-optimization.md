# Autoscaling Optimization (AWS + Azure)

Autoscaling determines operational cost efficiency.

---

# 1. Use Better Scaling Metrics

Better than CPU:
- Requests/sec
- Queue depth (SQS / Service Bus)
- Latency
- Memory
- Application KPIs (orders, sessions, etc.)

---

# 2. Target Tracking Scaling (Best Practice)

Keeps utilization at a target percentage:
- 40–60% CPU  
- 50–70% memory  
- Request-based scaling  

---

# 3. Step Scaling (When needed)

Used for:
- Large sudden spikes  
- Predictable bursts  

---

# 4. Queue-Based Scaling (Critical)

Best for:
- Worker nodes
- Batch jobs
- Event processors

Scale based on:
- Queue length
- Age of messages
- Backlog per instance  

---

# 5. Predictive Autoscaling

Use:
- AWS Predictive Scaling
- Azure VMSS Predictive Autoscale

---

# 6. Scale-to-Zero Models

Use for event-driven workloads:
- Lambda / Functions  
- Fargate tasks  
- KEDA  
- Container jobs  

---

# Summary

Using the right metrics + target tracking + queue scaling = best autoscaling results.
