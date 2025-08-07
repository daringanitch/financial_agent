# Financial Research Agent - Docker & Kubernetes Deployment

A comprehensive multi-agent financial research system with both command-line and web interfaces, deployed on Docker Desktop's Kubernetes cluster.

## 🎯 Overview

This project provides:
- **Multi-Agent Financial Research**: Planner, Search, Writer, Verifier agents working together
- **Web Interface**: Clean Streamlit dashboard for interactive financial analysis  
- **Command Line Interface**: Direct terminal access for quick queries
- **Kubernetes Deployment**: Production-ready containerized deployment
- **Persistent Storage**: Generated reports saved and accessible
- **Voice Support**: Audio interaction capabilities (future enhancement)

## 🚀 Quick Start

### Prerequisites
- Docker Desktop with Kubernetes enabled
- OpenAI API key
- kubectl configured for docker-desktop context

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd financial_agent

# Copy and configure the secret
cp k8s/secret.yaml.template k8s/secret.yaml
# Edit k8s/secret.yaml and add your OpenAI API key
```

### 2. Deploy to Kubernetes
```bash
# Build the Docker image
docker build -t financial-agent:latest .

# Deploy to Kubernetes
kubectl apply -f k8s/

# Check deployment status
kubectl get pods -n financial-agent
```

### 3. Access the Web Interface
```bash
# Port forward to access web UI
kubectl port-forward -n financial-agent $(kubectl get pods -n financial-agent -l app=financial-agent-web -o jsonpath='{.items[0].metadata.name}') 8501:8501
```

Then open: **http://localhost:8501**

## 💻 Usage

### Web Interface Features
- **📊 Interactive Dashboard**: Clean, professional interface
- **🔍 Query Input**: Natural language financial research queries
- **📌 Example Queries**: Pre-built queries for common analyses
- **⚡ Real-time Analysis**: Powered by OpenAI's latest models
- **📄 Report Generation**: Comprehensive markdown reports
- **📋 Report History**: Access previously generated analyses
- **🔧 Configuration Status**: Monitor API key and system status

### Example Queries
- "Analyze Apple's most recent quarter"
- "Write a report on Tesla's financial performance"
- "Research Microsoft's competitive position in cloud services"
- "Evaluate Amazon's e-commerce growth trends"

### Command Line Access
```bash
# Interactive financial research
echo "Analyze Apple's most recent quarter" | kubectl exec -i deployment/financial-agent -n financial-agent -- uv run python -m financial_research_agent.main

# Shell access
kubectl exec -it deployment/financial-agent -n financial-agent -- bash
```

## 🏗️ Architecture

### Multi-Agent System
1. **Planner Agent**: Converts queries into structured search terms
2. **Search Agent**: Web search using OpenAI's WebSearchTool
3. **Specialist Agents**: 
   - Fundamentals analyst
   - Risk analyst  
   - Verifier for quality control
4. **Writer Agent**: Synthesizes research into comprehensive reports
5. **Manager**: Orchestrates the entire pipeline

### Container Architecture
- **Base**: Python 3.11-slim with audio libraries
- **Package Manager**: uv for fast dependency resolution
- **Web Framework**: Streamlit for the dashboard
- **Agent Framework**: OpenAI Agents SDK
- **Storage**: Persistent volumes for reports

### Kubernetes Resources
- **Namespace**: `financial-agent` for resource isolation
- **Deployments**: Separate containers for CLI and web interfaces
- **Services**: NodePort services for external access
- **ConfigMaps**: Environment variables and configuration
- **Secrets**: Secure OpenAI API key storage
- **PersistentVolumes**: Report storage and data persistence

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_ORG_ID`: OpenAI organization ID (optional)
- `OPENAI_PROJECT_ID`: OpenAI project ID (optional)
- `OPENAI_AGENTS_DISABLE_TRACING`: Disable tracing (default: false)

### Models Used
- **Planner**: `gpt-4o-mini` for efficient query planning
- **Writer**: `gpt-4o` for high-quality report generation
- **Verifier**: `gpt-4o` for comprehensive fact-checking
- **Voice**: `gpt-4o-mini` for voice interactions

## 📁 Project Structure

```
financial_agent/
├── financial_research_agent/    # Core agent implementations
│   ├── agents/                 # Individual agent definitions
│   ├── main.py                 # CLI entry point
│   ├── mainvoice.py           # Voice interface
│   └── manager.py             # Agent orchestration
├── src/agents/                # OpenAI Agents SDK
├── k8s/                       # Kubernetes manifests
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── web-deployment.yaml
│   ├── service.yaml
│   ├── web-service.yaml
│   ├── configmap.yaml
│   ├── pv-pvc.yaml
│   └── secret.yaml.template
├── web_app.py                 # Streamlit web interface
├── .streamlit/                # Streamlit configuration
├── Dockerfile                 # Container definition
└── README_DOCKER.md          # This file
```

## 🔍 Monitoring & Debugging

### Check Status
```bash
# All resources
kubectl get all -n financial-agent

# Pod logs
kubectl logs deployment/financial-agent -n financial-agent -f
kubectl logs deployment/financial-agent-web -n financial-agent -f

# Pod details
kubectl describe pods -n financial-agent
```

### Generated Reports
Reports are saved to persistent storage and accessible at:
```bash
# Inside pods
ls /tmp/financial-agent-reports/

# On host (Docker Desktop)
ls /tmp/financial-agent-reports/
```

## 🧹 Cleanup

```bash
# Remove everything
kubectl delete namespace financial-agent

# Or scale down to save resources
kubectl scale deployment financial-agent --replicas=0 -n financial-agent
kubectl scale deployment financial-agent-web --replicas=0 -n financial-agent
```

## 🔒 Security Notes

- API keys are stored in Kubernetes secrets
- Containers run as non-root user
- Network policies can be added for production
- Resource limits prevent resource exhaustion
- No sensitive data in container images

## 🛠️ Development

### Local Development
```bash
# Install dependencies
uv sync --all-extras --all-packages --group dev

# Run linting
make lint

# Run tests  
make tests

# Type checking
make mypy
```

### Building Images
```bash
# Build with latest updates
docker build -t financial-agent:latest .

# Multi-architecture build (future)
docker buildx build --platform linux/amd64,linux/arm64 -t financial-agent:latest .
```

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Add tests
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check pod logs: `kubectl logs -n financial-agent <pod-name>`
- Verify OpenAI API key and credits
- Ensure Docker Desktop Kubernetes is enabled
- Check network connectivity and port forwarding