FROM python:3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    git \
    && python -m venv /opt/venv

WORKDIR /app
COPY . .
RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


################
# PRODUCTION
################

FROM python:3.12-alpine

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONFAULTHANDLER=1

WORKDIR /app

COPY src/ .

RUN find /opt/venv \( -type d -a -name __pycache__ \) -exec rm -rf {} \+ \
    && rm -rf /opt/venv/include \
    && rm -rf /opt/venv/lib/python3.12/site-packages/tests

EXPOSE 8480
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8480/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8480", "--no-server-header"]
