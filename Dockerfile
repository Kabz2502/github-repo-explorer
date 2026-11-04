FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY repo_explorer.py .

# Run as a non-root user
RUN useradd --create-home appuser
USER appuser

ENTRYPOINT ["python", "repo_explorer.py"]
