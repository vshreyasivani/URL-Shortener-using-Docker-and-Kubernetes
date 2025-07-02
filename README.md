# 🚀 Load-Balanced URL Shortener using Docker & Kubernetes

## 📘 Project Overview

A scalable and containerized **URL shortener service** built using **Python (Flask)**, **Redis**, **Docker**, and **Kubernetes**. It supports shortening long URLs, redirection, and scaling with real-time monitoring and load balancing.

The system is architected for **high availability**, **horizontal scalability**, and **cloud-native deployment**, with auto-scaling enabled using HPA and load balancing via LoadBalancer.

---

## ✅ Features

- **Shorten URLs:** Accepts long URLs via an API and returns shortened links.
- **Redirection:** Redirects from short to original URLs.
- **Containerized:** Fully Dockerized for portability and consistent environments.
- **Kubernetes Orchestration:** Runs as multiple pods for high availability.
- **Auto-Scaling:** Scales pods dynamically using Horizontal Pod Autoscaler.
- **Load Balancing:** Traffic distributed using LoadBalancer.
- **Monitoring & Logging:** Observe performance via Kubernetes-native tools.

---

## 🛠️ Tech Stack

| Layer             | Tech Used               |
|------------------|--------------------------|
| Backend           | Python (Flask)           |
| Storage           | Redis (in-memory)        |
| Containerization  | Docker                   |
| Orchestration     | Kubernetes               |
| Networking        | ClusterIP, LoadBalancer  |
| Monitoring        | kubectl logs, HPA        |

---

## ☸️ Kubernetes Components

- **Deployments & Services:**
  - `url-shortener` Deployment (Flask App)
  - `redis` Deployment (Key-Value Store)
  - `ClusterIP` Service for internal Redis access
  - `LoadBalancer` for external access

- **Scaling & Monitoring:**
  - `Horizontal Pod Autoscaler` for Flask app
  - `kubectl logs` for log inspection
  - `load_test.py` for triggering auto-scaling

---

## ▶️ How to Run the Project

### 🔧 Option 1: Local with Docker Compose

```bash
docker-compose up -d --build
docker-compose ps
```

Test shortening a URL:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"url":"https://en.wikipedia.org/wiki/Artificial_intelligence"}' \
http://localhost:5000/shorten
```

---

### ☁️ Option 2: Kubernetes with Minikube

#### 1. Start Minikube and Setup Docker Env

```bash
minikube start
eval $(minikube docker-env)
docker build -t url-shortener:latest .
```

#### 2. Deploy to Kubernetes

```bash
kubectl apply -f k8s/redis-deployment.yaml
kubectl apply -f k8s/redis-service.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/url-shortener-deployment.yaml
kubectl apply -f k8s/url-shortener-service.yaml
```

#### 3. Verify Deployments

```bash
kubectl get pods
kubectl get services
```

#### 4. Access the Application

```bash
minikube service url-shortener-service
```

Use the given URL to shorten:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"url":"https://en.wikipedia.org/wiki/Artificial_intelligence"}' \
http://<minikube-url>/shorten
```

---

### 📈 Enable Auto-Scaling (HPA)

```bash
kubectl apply -f k8s/hpa.yaml
kubectl get hpa
```

(Optional) Load test to trigger HPA:

```bash
kubectl port-forward service/url-shortener-service 8080:80
# App is now accessible at http://localhost:8080

python load_test.py
kubectl get hpa -w
```

---

## 🚀 Future Enhancements

- 💾 **Persistent DB**: Replace Redis with PostgreSQL or MongoDB.
- 🔁 **CI/CD Pipeline**: Integrate with GitHub Actions or Jenkins.
- 🔐 **Security**: Add JWT authentication and rate limiting.
- ☁️ **Cloud Native**: Deploy to AWS EKS, GCP GKE, or Azure AKS.

---

