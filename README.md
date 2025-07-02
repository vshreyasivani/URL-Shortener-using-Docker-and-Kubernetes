# PES2UG22CS620_633_640_646_Load-Balanced-URL-Shortener-using-Docker-Kubernetes
# Project Overview

This project is a scalable and containerized URL shortener service that allows users to submit long URLs and get a shortened version. The system is designed using Docker and Kubernetes, with a load balancer to distribute incoming traffic efficiently across multiple instances of the service.

The URL mappings are stored in an in-memory key-value store running in a separate container. The system is built to handle high availability and scalability with auto-scaling and monitoring features.

# Features

Shorten URLs: Accept long URLs via an API and generate short URLs.

Redirection Service: Redirect users from short URLs to the original long URLs.

Containerized Deployment: Packaged into a Docker container for portability.

Kubernetes Orchestration: Managed using Kubernetes with multiple instances for load balancing.

Scalability: Configured with Horizontal Pod Autoscaler (HPA) to scale based on CPU usage.

Load Balancing: Uses Ingress Controller / LoadBalancer to distribute traffic efficiently.

Monitoring: Logs and metrics collection to observe system performance.

# Technologies Used

Backend: Python (Flask) 

Database: Redis (In-memory key-value store) 

Containerization: Docker

Orchestration & Scaling: Kubernetes

Networking: Kubernetes LoadBalancer, ClusterIP

Monitoring & Logging: Kubernetes logging tools


# Kubernetes Components

1. Deployment & Services

URL Shortener Pod (Runs multiple instances of the app)

Key-Value Store Pod (Stores shortened URLs)

ClusterIP Service (Exposes Redis internally)

LoadBalancer (Exposes URL shortener to external users)

2. Scaling & Monitoring

Horizontal Pod Autoscaler (HPA)

Ingress Controller for Load Balancing

Logging using kubectl logs and monitoring tools

# Future Enhancements

Persistent Storage: Use a database like PostgreSQL or MongoDB instead of Redis.

CI/CD Pipeline: Automate testing and deployment using GitHub Actions / Jenkins.

Enhanced Security: Implement JWT authentication and rate limiting.

Cloud Deployment: Deploy on AWS EKS, Google GKE, or Azure AKS.

# Contributors

Taranjot Singh Dhingra - PES2UG22CS620 
Tushar Swami - PES2UG22CS633
V Shreya Sivani - PES2UG22CS640
Varshith Sagar GV - PES2UG22CS646



