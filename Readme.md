# DevOps Case Study Platform

This repository covers the DevOps platform implementation, demonstrating Jenkins CI/CD pipeline, Kubernetes deployment, IaC provisioning, and full-stack monitoring.

---

## 📂 Project Structure

```text
devops-casestudy/
├── DevOps_CaseStudy_Report_VoCongHuan.pdf   # Comprehensive project report
├── docker-compose.yml                      # Infrastructure stack (Jenkins + Monitoring)
├── Jenkinsfile                             # Multi-stage CI/CD pipeline definition
├── jenkins-agent.Dockerfile               # Custom agent (Python3, Docker CLI, kubectl)
├── ansible/
│   └── setup-devops-env.yml                # Ansible playbook for environment provisioning
├── flask_app/
│   ├── app.py                              # Flask application with /metrics endpoint
│   ├── test_app.py                         # Unit tests for the application
│   ├── requirements.txt                    # Python dependencies
│   └── Dockerfile                          # Multi-stage build for Flask app
├── k8s/
│   ├── deployment.yaml                     # K8s Deployment (2 replicas, Rolling Update)
│   └── service.yaml                        # K8s Service (NodePort: 30080)
└── monitoring/
    ├── prometheus.yml                      # Scrape configurations for Flask & Jenkins
    ├── loki-config.yml                     # Grafana Loki configuration (WAL + compactor)
    ├── promtail-config.yml                 # Promtail configuration for pod log collection
    └── grafana/
        ├── provisioning/
        │   ├── datasources/datasources.yml # Automated datasource setup
        │   └── dashboards/dashboards.yml  # Automated dashboard provisioning
        └── dashboards/
            ├── flask-dashboard.json        # Grafana Dashboard for Flask Metrics
            └── jenkins-dashboard.json       # Grafana Dashboard for Jenkins Metrics
