# Use Python 3.11 as base image (compatible with the project)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    portaudio19-dev \
    libasound2-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN pip install uv

# Copy project files
COPY pyproject.toml uv.lock README.md ./
COPY src/ ./src/
COPY financial_research_agent/ ./financial_research_agent/
COPY Makefile ./
COPY web_app.py ./
COPY .streamlit/ ./.streamlit/

# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Install Streamlit for web interface
RUN uv add streamlit

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Expose ports for MCP server and web interface
EXPOSE 8000 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Default command - run the main financial research application
CMD ["uv", "run", "python", "-m", "financial_research_agent.main"]