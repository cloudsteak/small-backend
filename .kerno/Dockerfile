FROM python:3.11-slim

WORKDIR /app

# Copy application code
COPY . .

# Install FastAPI and uvicorn, plus any additional requirements
RUN pip install --no-cache-dir fastapi uvicorn[standard] python-jose[cryptography] passlib[bcrypt] pydantic pydantic-settings && \
    if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Expose port 8000 (FastAPI default)
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
