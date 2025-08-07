# Financial Research Agent

This project allows you to generate financial reports and interact with them through voice chat.

## Prerequisites

Ensure you have Python 10+ installed. It is recommended to create and activate a virtual environment before proceeding.

Then unsure to set up you python environement:

   `python -m venv .venv`<br>
   `source .venv/bin/activate`

## Installation

1. **Install requirements:**
   To install the necessary dependencies, use the following command:

   ```bash
   pip install -r requirements.txt

2. **Install dependencies:**
Install dependencies: After installing the requirements, run the following command to synchronize the project dependencies:

   ```bash
   make sync

3. **Install OpenAI agents:**
To install the openai-agents package, run:
    ```bash
    pip install openai-agents

4- **Generate the financial report:**
Set your OpenAI key first:
   
      $env:OPENAI_API_KEY="your_api_key_here"
Then use the following command:

    python -m financial_research_agent.main

5- **Chat with voice to interact with the report:**
To interact with the financial report via voice, run:

    python -m financial_research_agent.mainvoice

## 🐳 Docker & Kubernetes Deployment

For a production-ready deployment with web interface, use our Docker and Kubernetes setup:

### 🚀 Quick Deploy to Docker Desktop

```bash
# 1. Build the Docker image
docker build -t financial-agent:latest .

# 2. Configure your OpenAI API key
cp k8s/secret.yaml.template k8s/secret.yaml
# Edit k8s/secret.yaml and add your API key

# 3. Deploy to Kubernetes
kubectl apply -f k8s/

# 4. Access the web interface
kubectl port-forward -n financial-agent $(kubectl get pods -n financial-agent -l app=financial-agent-web -o jsonpath='{.items[0].metadata.name}') 8501:8501
```

Then open: **http://localhost:8501**

### 🌐 Web Interface Features

- **📊 Interactive Dashboard**: Professional Streamlit interface
- **🔍 Query Input**: Natural language financial research
- **📌 Example Queries**: Pre-built common analyses
- **⚡ Real-time Analysis**: Powered by OpenAI's latest models
- **📄 Report Generation**: Comprehensive markdown reports
- **📋 Report History**: Access previous analyses

### 📚 Detailed Documentation

For complete setup instructions, troubleshooting, and advanced configuration:
- **[Docker & Kubernetes Guide](README_DOCKER.md)** - Comprehensive deployment documentation
- **[Kubernetes Manifests](k8s/)** - All K8s configuration files and templates
- **[Setup Instructions](k8s/README.md)** - Step-by-step deployment guide

### 🔧 Requirements

- Docker Desktop with Kubernetes enabled
- OpenAI API key with sufficient credits
- kubectl configured for docker-desktop context

