# Financial Research Agent Helm Chart

A Helm chart for deploying the Financial Research Agent with web interface on Kubernetes.

## Overview

This Helm chart deploys a complete Financial Research Agent system including:
- **CLI Interface**: Command-line financial research agent
- **Web Interface**: Professional Streamlit dashboard  
- **Persistent Storage**: Report storage and data persistence
- **Security**: Proper secret management and security contexts
- **Configurability**: Extensive configuration options via values.yaml

## Prerequisites

- Kubernetes 1.19+
- Helm 3.0+
- Docker Desktop with Kubernetes enabled (for local deployment)
- OpenAI API key with sufficient credits

## Quick Start

### 1. Install Helm Chart

```bash
# Clone the repository
git clone https://github.com/daringanitch/financial_agent.git
cd financial_agent

# Build the Docker image
docker build -t financial-agent:latest .

# Install with Helm
helm install my-financial-agent ./helm/financial-agent \
  --set openai.apiKey="your-openai-api-key-here"
```

### 2. Access the Web Interface

```bash
# Port forward to access web UI
kubectl port-forward -n financial-agent service/my-financial-agent-web 8501:8501
```

Then open: **http://localhost:8501**

### 3. Use CLI Interface

```bash
# Interactive financial research
kubectl exec -it -n financial-agent deployment/my-financial-agent -- uv run python -m financial_research_agent.main
```

## Configuration

### Required Configuration

```yaml
openai:
  apiKey: "your-openai-api-key-here"  # REQUIRED
```

### Common Configurations

```yaml
# Enable/disable components
financialAgent:
  enabled: true
webInterface:
  enabled: true
  
# Resource limits
financialAgent:
  resources:
    limits:
      cpu: 500m
      memory: 1Gi
    requests:
      cpu: 250m
      memory: 512Mi

# Service configuration
webInterface:
  service:
    type: NodePort
    nodePort: 30001
    
# Storage configuration
persistence:
  enabled: true
  reports:
    size: 1Gi
    storageClass: "hostpath"
```

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `openai.apiKey` | string | `""` | **REQUIRED** OpenAI API key |
| `openai.orgId` | string | `""` | Optional OpenAI organization ID |
| `openai.projectId` | string | `""` | Optional OpenAI project ID |
| `financialAgent.enabled` | bool | `true` | Enable CLI agent deployment |
| `webInterface.enabled` | bool | `true` | Enable web interface deployment |
| `webInterface.service.type` | string | `"NodePort"` | Service type for web interface |
| `webInterface.service.nodePort` | int | `30001` | NodePort for web access |
| `persistence.enabled` | bool | `true` | Enable persistent storage |
| `persistence.reports.size` | string | `"1Gi"` | Size of reports storage |

## Installation Examples

### Basic Installation
```bash
helm install financial-agent ./helm/financial-agent \
  --set openai.apiKey="sk-..."
```

### Custom Configuration
```bash
helm install financial-agent ./helm/financial-agent \
  --set openai.apiKey="sk-..." \
  --set webInterface.service.nodePort=30002 \
  --set persistence.reports.size="2Gi"
```

### With Custom Values File
```bash
# Create custom-values.yaml
cat > custom-values.yaml <<EOF
openai:
  apiKey: "sk-..."
  orgId: "org-..."
  
webInterface:
  service:
    nodePort: 30002
    
persistence:
  reports:
    size: "2Gi"
EOF

helm install financial-agent ./helm/financial-agent -f custom-values.yaml
```

## Upgrading

```bash
# Upgrade with new values
helm upgrade financial-agent ./helm/financial-agent \
  --set openai.apiKey="sk-..."
  
# Upgrade with values file
helm upgrade financial-agent ./helm/financial-agent -f values.yaml
```

## Uninstalling

```bash
# Uninstall the release
helm uninstall financial-agent

# Clean up namespace (optional)
kubectl delete namespace financial-agent
```

## Troubleshooting

### Check Pod Status
```bash
kubectl get pods -n financial-agent
kubectl describe pod -n financial-agent <pod-name>
```

### View Logs
```bash
kubectl logs -n financial-agent deployment/financial-agent
kubectl logs -n financial-agent deployment/financial-agent-web
```

### Port Forwarding Issues
```bash
# Check services
kubectl get svc -n financial-agent

# Direct pod port forward
kubectl port-forward -n financial-agent pod/<pod-name> 8501:8501
```

### Common Issues

1. **OpenAI API Key Missing**: Set `openai.apiKey` in values
2. **Image Not Found**: Build image locally: `docker build -t financial-agent:latest .`
3. **Port Conflicts**: Change `webInterface.service.nodePort` value
4. **Storage Issues**: Check `persistence.reports.storageClass` configuration

## Advanced Configuration

### Custom Image
```yaml
image:
  repository: my-registry/financial-agent
  tag: "v1.0.0"
  pullPolicy: Always
```

### Security Context
```yaml
securityContext:
  runAsUser: 1001
  runAsGroup: 1001
  
podSecurityContext:
  runAsNonRoot: true
  runAsUser: 1001
```

### Node Affinity
```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64"]
```

## Support

For issues and questions:
- GitHub: https://github.com/daringanitch/financial_agent
- Documentation: [README_DOCKER.md](../../README_DOCKER.md)