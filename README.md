
# Nasiko Agent Request Layer

Nasiko Agent Request Layer is a small FastAPI service that receives agent
requests, checks a cache, applies a simple rate limit, and then routes the
request to an agent processor.

## Features

- Request gateway for agent calls
- In-memory response caching
- Per-agent rate limiting
- Health and metrics endpoints
- Simple structure that can later be connected to real agent services or queues

## Project Structure

```text
app/
  main.py                     FastAPI app setup and router registration
  routes/
    gateway.py                Main request endpoint
    health.py                 Health-check endpoint
    metrics.py                Cache and rate-limit metrics endpoints
  middleware/
    cache.py                  In-memory cache helper
    rate_limiter.py           Per-agent request limiter
  services/
    agent_router.py           Placeholder agent processing logic
requirements.txt             Python dependencies
README.md                    Project guide
```

## How It Works

1. A client sends a `POST` request to `/gateway/request`.
2. The gateway reads the `agent` and `query` from the request body.
3. It checks whether the response already exists in the in-memory cache.
4. If cached, it returns the cached response.
5. If not cached, it checks the per-agent rate limit.
6. If the agent is over the limit, the request is marked as queued.
7. Otherwise, the request is processed and the response is cached.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the app at:

```text
http://127.0.0.1:8000
```

Interactive API docs:

```text
http://127.0.0.1:8000/docs
```

## Local Agent Deployment Demo

This repository includes a lightweight local demo that matches the first-agent
deployment flow:

```bash
cat orchestrator/superuser_credentials.json
uvicorn app.main:app --host 127.0.0.1 --port 9100 --reload
```

Then open:

```text
http://localhost:9100/app/
```

Use these local demo credentials:

```text
Access Key: local-admin-key
Access Secret: local-admin-secret
```

The demo translator package is available at:

```text
agents/a2a-translator.zip
```

Verify the local translator endpoint:

```bash
curl http://localhost:9100/agents/translator/health
```

Test the local router:

```bash
curl "http://localhost:9100/router/route?query=translate this to French"
```

## API Endpoints

### Root

```http
GET /
```

Returns a basic running message.

### Gateway

```http
POST /gateway/request
```

Example body:

```json
{
  "agent": "translator-agent",
  "query": "Translate hello to Hindi"
}
```

Example response:

```json
{
  "source": "agent",
  "response": "Processed by translator-agent: Translate hello to Hindi"
}
```

### Health

```http
GET /health/
```

Returns:

```json
{
  "status": "healthy"
}
```

### Metrics

```http
GET /metrics/cache
GET /metrics/rate-limit
```

## Current Limitations

- Cache and rate-limit data are stored in memory, so they reset when the server
  restarts.
- `process_agent_request()` is currently a placeholder and does not call a real
  AI agent yet.
- The queued response is only a status response; there is no real background
  queue connected yet.

## Push to GitHub

Create an empty GitHub repository first, then run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git branch -M main
git push -u origin main
```

If the remote already exists, update it with:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```
