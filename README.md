🧠 CI/CD Pipeline Flow
┌────────────┐       ┌────────────┐       ┌──────────────┐
│ Developer  │  git  │ GitHub     │  CI   │ Docker Hub   │
│  commits   │ ───▶  │ Actions    │ ───▶  │ Registry     │
└────────────┘       └────────────┘       └──────────────┘
│
▼
┌────────────┐
│  Server /  │
│  Docker 🐳  │
└────────────┘
