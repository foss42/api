# Deploying on Azure App Service

## Prerequisites

- Azure CLI installed (`brew install azure-cli` on macOS)
- An existing Azure Web App (Linux, Python 3.11 runtime)
- Logged in via `az login`

## Configuration Files

| File | Purpose |
|------|---------|
| `startup.sh` | Custom startup command — runs gunicorn with uvicorn workers from the `src/` directory on port 8000 |
| `.deployment` | Tells Azure's Oryx build system to install dependencies during deployment |
| `requirements.txt` | Root-level pip requirements (used automatically by Azure's build) |

## Step 1 — Configure the Web App

Replace `<app-name>` and `<resource-group>` with your actual values.

```bash
# Set the startup command
az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "startup.sh"

# Ensure the Python 3.11 runtime is set
az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --linux-fx-version "PYTHON|3.11"
```

## Step 2 — Set Environment Variables (if needed)

If your app uses any environment variables (via `pydantic-settings`), set them as App Settings:

```bash
az webapp config appsettings set \
  --name <app-name> \
  --resource-group <resource-group> \
  --settings KEY1=value1 KEY2=value2
```

## Step 3 — Deploy via ZIP Deploy (Recommended)

From the repository root:

```bash
# Create a zip of the project (excluding unnecessary files)
zip -r deploy.zip . -x ".git/*" "__pycache__/*" "*.pyc" ".env" "deploy.zip"

# Deploy
az webapp deploy \
  --name <app-name> \
  --resource-group <resource-group> \
  --src-path deploy.zip \
  --type zip
```

### Alternative: Deploy via Local Git

```bash
# Set deployment source to local git
az webapp deployment source config-local-git \
  --name <app-name> \
  --resource-group <resource-group>

# The command above returns a git remote URL. Add it:
git remote add azure <url-from-above>

# Push to deploy
git push azure main
```

### Alternative: Deploy via GitHub Actions

In the Azure Portal, go to **Deployment Center** → select **GitHub** → authorize and choose this repository. Azure will auto-generate a GitHub Actions workflow.

## Step 4 — Verify

```bash
# Check deployment logs
az webapp log tail --name <app-name> --resource-group <resource-group>

# Test the endpoint
curl https://<app-name>.azurewebsites.net/
```

## Troubleshooting

- **Port**: Azure App Service injects the `PORT` environment variable (default 8000 for Python). The `startup.sh` binds to `0.0.0.0:8000` to match.
- **Build errors**: Check build logs at `https://<app-name>.scm.azurewebsites.net/api/logs/docker`.
- **SSH into the container**: `az webapp ssh --name <app-name> --resource-group <resource-group>` to debug directly.
- **Startup logs**: `az webapp log download --name <app-name> --resource-group <resource-group>` downloads full logs as a zip.
