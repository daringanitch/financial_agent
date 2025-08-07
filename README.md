# Financial Research Agent

This project is a financial research agent that allows users to generate financial reports and interact with them through voice chat. It is built on top of the OpenAI Agents SDK and provides a web-based interface for querying and analyzing financial data.

## 🎯 Main Function Points

* **Generate financial reports** - Comprehensive AI-powered financial analysis and research
* **Interact with reports through voice chat** - Natural language voice interaction with generated reports
* **Provide a web-based interface** - Professional Streamlit dashboard for querying and analyzing financial data
* **Offer production-ready deployment** - Complete Docker and Kubernetes setup for scalable deployment

## 🛠️ Technology Stack

* **Python** - Core programming language and runtime
* **OpenAI Agents SDK** - Multi-agent AI framework for orchestrated financial research
* **Streamlit** - Interactive web interface for financial queries and report visualization
* **Docker and Kubernetes** - Containerized deployment for production environments

## Prerequisites

### 📦 Local Development Prerequisites

- **Python 3.9+** (Python 3.10+ recommended)
- **OpenAI API Key** with sufficient credits
- **Git** for cloning the repository
- **Virtual Environment** (recommended for isolation)

### 🐳 Kubernetes Deployment Prerequisites

- **Docker Desktop** with Kubernetes enabled
- **kubectl** configured for docker-desktop context
- **OpenAI API Key** with sufficient credits
- **Git** for cloning the repository

## Local Installation

### 1. **Setup Python Environment**
Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. **Install Dependencies**
Install the necessary dependencies:
```bash
pip install -r requirements.txt
make sync
pip install openai-agents
```

### 3. **Configure OpenAI API Key**
Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your_api_key_here"
# On Windows: set OPENAI_API_KEY=your_api_key_here
```

### 4. **Generate Financial Reports**
Run the main financial research agent:
```bash
python -m financial_research_agent.main
```

### 5. **Voice Chat Interface**
To interact with reports via voice:
```bash
python -m financial_research_agent.mainvoice
```

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

### ⚡ Helm Deployment (Recommended)

For the most flexible and production-ready deployment:

```bash
# 1. Build the Docker image
docker build -t financial-agent:latest .

# 2. Install with Helm
helm install financial-agent ./helm/financial-agent \
  --set openai.apiKey="your-openai-api-key-here"

# 3. Access the web interface
kubectl port-forward -n financial-agent service/financial-agent-web 8501:8501
```

**Benefits of Helm deployment:**
- **🎛️ Configurable**: Extensive configuration options
- **🔄 Upgradeable**: Easy updates and rollbacks
- **📦 Packaged**: Professional Kubernetes package management
- **🛡️ Secure**: Proper secret and security context management

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
- **[Helm Chart](helm/financial-agent/)** - Professional Kubernetes package management
- **[Kubernetes Manifests](k8s/)** - Raw K8s configuration files and templates  
- **[Setup Instructions](k8s/README.md)** - Step-by-step deployment guide

### 🔧 Prerequisites

Ensure you have the [Kubernetes Deployment Prerequisites](#-kubernetes-deployment-prerequisites) installed and configured before proceeding.

