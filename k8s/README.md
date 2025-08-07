# Financial Agent Kubernetes Deployment

This directory contains Kubernetes manifests for deploying the Financial Research Agent to Docker Desktop's built-in Kubernetes cluster.

## Prerequisites

1. **Docker Desktop** with Kubernetes enabled
2. **OpenAI API Key**
3. **kubectl** configured to use Docker Desktop context

## Setup Instructions

### 1. Enable Kubernetes in Docker Desktop
- Open Docker Desktop settings
- Go to Kubernetes tab
- Enable "Enable Kubernetes"
- Click "Apply & Restart"

### 2. Verify kubectl context
```bash
kubectl config current-context
# Should show: docker-desktop
```

### 3. Build the Docker image
```bash
# Build the image locally (Docker Desktop will use it)
docker build -t financial-agent:latest .
```

### 4. Update the OpenAI API key
Edit `k8s/secret.yaml` and replace `your-openai-api-key-here` with your actual OpenAI API key.

### 5. Deploy to Kubernetes
```bash
# Apply all manifests
kubectl apply -f k8s/

# Check deployment status
kubectl get pods -n financial-agent
kubectl get services -n financial-agent
```

## Accessing the Application

### Interactive Mode (for queries)
```bash
# Connect to the running pod for interactive queries
kubectl exec -it deployment/financial-agent -n financial-agent -- bash

# Or run the application directly
kubectl exec -it deployment/financial-agent -n financial-agent -- uv run python -m financial_research_agent.main
```

### View Logs
```bash
kubectl logs deployment/financial-agent -n financial-agent -f
```

### Access Generated Reports
Reports are stored in `/tmp/financial-agent-reports` on your local machine (mounted as PersistentVolume).

## Services

- **MCP Server**: Accessible at `localhost:30000` (NodePort)
- **Reports Storage**: Persistent volume at `/tmp/financial-agent-reports`

## Cleanup

```bash
# Delete all resources
kubectl delete -f k8s/

# Or delete namespace (removes everything)
kubectl delete namespace financial-agent
```

## Troubleshooting

1. **Image not found**: Ensure you built the image locally with `docker build -t financial-agent:latest .`
2. **API Key issues**: Check the secret with `kubectl get secret openai-credentials -n financial-agent -o yaml`
3. **Pod not starting**: Check logs with `kubectl describe pod <pod-name> -n financial-agent`

## Architecture

The deployment includes:
- **Namespace**: `financial-agent` for resource isolation
- **Deployment**: Single replica of the financial agent
- **Service**: NodePort service for external access
- **ConfigMap**: Environment variables
- **Secret**: OpenAI credentials
- **PersistentVolume**: Storage for generated reports