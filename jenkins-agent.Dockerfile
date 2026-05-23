FROM jenkins/inbound-agent:latest

USER root

# Cài Python, pip, Docker CLI
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    && curl -fsSL https://get.docker.com | sh \
    && apt-get clean

# Cài kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

USER jenkins
