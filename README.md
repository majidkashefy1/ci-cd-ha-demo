       ┌─────────────┐
       │   GitHub    │
       │  (Actions)  │
       └──────┬──────┘
              │ builds image
              ▼
     ┌────────────────────┐
     │ Docker Hub Registry│
     └──────┬─────────────┘
            │ new image pushed
            ▼
    ┌────────────────────────────┐
    │ Docker Host                │
    │                            │
    │  ┌──────────────┐          │
    │  │ Watchtower   │          │  ← Pulls latest image
    │  └─────┬────────┘          │
    │        │                   │
    │ ┌──────▼─────┐   ┌───────┐ │
    │ │ app1       │   │ app2  │ │
    │ └──────┬─────┘   └───────┘ │
    │        │          ▲         │
    │     ┌──▼──────────┘         │
    │     │ NGINX LB (8080)       │
    │     └──┬────────────────────┘
    │        │
    │ ┌──────▼─────────┐
    │ │ Prometheus     │ ← collects metrics
    │ └──────┬─────────┘
    │        │
    │ ┌──────▼─────────┐
    │ │ Grafana        │ ← visualizes metrics
    │ └────────────────┘
    └────────────────────────────┘


# 🧠 CI/CD + Auto-Deployment + Monitoring Demo

A **production-style DevOps demo project** showcasing:
- Continuous Integration (GitHub Actions)
- Continuous Deployment (Watchtower)
- High Availability (NGINX load balancing)
- Real-Time Monitoring (Prometheus + Grafana + Node Exporter)

This setup demonstrates how modern teams automate deployments, maintain uptime, and monitor systems in real time.

---

## 🚀 Features

| Feature | Description |
|----------|-------------|
| ⚙️ **CI/CD Pipeline** | Automated image build & push via GitHub Actions |
| 🔄 **Auto-Redeploy** | Watchtower automatically pulls new images and redeploys |
| 🧱 **Load Balancing** | NGINX splits traffic between app replicas |
| 🧩 **High Availability** | Multiple app instances ensure no downtime |
| 📊 **Monitoring** | Prometheus + Grafana visualize metrics & uptime |
| 💡 **Node Exporter** | Collects CPU, RAM, disk, and system metrics |

---

## 🏗️ Architecture Overview

    GitHub Actions ──► Docker Hub ──► Watchtower ──► NGINX ──► Flask Apps
    │
    ▼
    Prometheus + Grafana

🟢 Each component plays a role:

- **GitHub Actions** builds and pushes Docker images
- **Watchtower** redeploys updated images automatically
- **NGINX** load balances between replicas
- **Prometheus** scrapes live metrics
- **Grafana** visualizes them beautifully

---

## 📂 Project Structure

    ci-cd-ha-monitoring-demo/
    │
    ├── .github/
    │ └── workflows/
    │ └── ci.yml # CI build & push pipeline
    │
    ├── app/
    │ ├── Dockerfile # Flask app Dockerfile
    │ └── app.py # Sample Flask app with metrics
    │
    ├── nginx/
    │ └── nginx.conf # Load balancing configuration
    │
    ├── prometheus/
    │ └── prometheus.yml # Metrics configuration
    │
    ├── docker-compose.yml # Full environment
    └── README.md

---

## ⚙️ How It Works

1. Developer pushes code → GitHub Actions builds & pushes Docker image
2. Docker Hub receives the new image
3. Watchtower detects the change → pulls & restarts containers
4. NGINX keeps serving traffic during updates (no downtime)
5. Prometheus scrapes metrics → Grafana visualizes them

---

## 🧱 Setup & Run Locally

### 1️⃣ Clone the project
```bash
git clone https://github.com/01020majid/ci-cd-ha-monitoring-demo.git
cd ci-cd-ha-monitoring-demo
```

2️⃣ Build & start containers
```bash
docker compose up -d --build
```

3️⃣ Access services
```bash
| Service    | URL                                            | Description                 |
| ---------- | ---------------------------------------------- | --------------------------- |
| Web App    | [http://localhost:8080](http://localhost:8080) | Load-balanced Flask apps    |
| Prometheus | [http://localhost:9090](http://localhost:9090) | Metrics database            |
| Grafana    | [http://localhost:3000](http://localhost:3000) | Dashboards & visualizations |


Default Grafana login:
    Username: admin
    Password: admin
    
Then add a Prometheus data source:
    URL: http://prometheus:9090
```

🧩 GitHub Actions CI Workflow

    File: .github/workflows/ci.yml

    name: CI Build and Push
    
    on:
    push:
    branches: [ "main" ]
    
    jobs:
    build:
    runs-on: ubuntu-latest
    
        steps:
          - name: Checkout code
            uses: actions/checkout@v3
    
          - name: Set up Docker Buildx
            uses: docker/setup-buildx-action@v2
    
          - name: Log in to Docker Hub
            uses: docker/login-action@v3
            with:
              username: ${{ secrets.DOCKERHUB_USERNAME }}
              password: ${{ secrets.DOCKERHUB_TOKEN }}
    
          - name: Build and Push image
            uses: docker/build-push-action@v5
            with:
              context: ./app
              file: ./app/Dockerfile
              push: true
              tags: ${{ secrets.DOCKERHUB_USERNAME }}/ci-cd-ha-demo:latest


🔄 Watchtower Configuration

    File: part of docker-compose.yml

    watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    restart: always
    environment:
      - WATCHTOWER_CLEANUP=true
      - WATCHTOWER_POLL_INTERVAL=30
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock


Watchtower automatically:
    
    Detects new images on Docker Hub
    
    Pulls and redeploys containers
    
    Cleans up old versions

📊 Monitoring Setup
    Prometheus configuration
    File: prometheus/prometheus.yml

    global:
    scrape_interval: 5s
    
    scrape_configs:
    - job_name: 'prometheus'
      static_configs:
        - targets: ['prometheus:9090']
    
      - job_name: 'node-exporter'
        static_configs:
          - targets: ['node-exporter:9100']
    
      - job_name: 'nginx'
        static_configs:
          - targets: ['nginx-lb:80']


💪 Extend This Project

    | Feature                    | Description                                    |
    | -------------------------- | ---------------------------------------------- |
    | 🕒 **Prometheus Alerts**   | Trigger notifications when containers go down  |
    | ☁️ **Deploy to Cloud**     | Run the same setup on AWS / GCP / DigitalOcean |
    | 🧠 **Add Loki**            | Include log aggregation for observability      |
    | 🔁 **Canary / Blue-Green** | Gradual rollout strategy with NGINX weights    |

🧰 Tech Stack
    
    | Tool               | Role                          |
    | ------------------ | ----------------------------- |
    | **Flask**          | Web app                       |
    | **Docker Compose** | Multi-container orchestration |
    | **NGINX**          | Load balancer                 |
    | **Prometheus**     | Metrics collection            |
    | **Grafana**        | Visualization                 |
    | **Node Exporter**  | System metrics                |
    | **Watchtower**     | Auto-deployment               |
    | **GitHub Actions** | CI/CD pipeline                |
