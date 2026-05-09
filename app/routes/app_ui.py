from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/app", tags=["App"])


@router.get("/", response_class=HTMLResponse)
async def app_home():
    return """
    <!doctype html>
    <html>
      <head>
        <title>Nasiko Local</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 40px; max-width: 760px; }
          input, button { display: block; margin: 10px 0; padding: 10px; width: 320px; }
          .agent { border: 1px solid #ddd; padding: 16px; margin-top: 24px; }
        </style>
      </head>
      <body>
        <h1>Nasiko Local</h1>
        <p>Use the local access key and secret from orchestrator/superuser_credentials.json.</p>
        <input placeholder="Access Key" />
        <input placeholder="Access Secret" type="password" />
        <button>Sign In</button>
        <div class="agent">
          <h2>Translator Agent</h2>
          <p>Status: Active</p>
          <p>Upload ZIP path: agents/a2a-translator.zip</p>
          <button>Start Session</button>
        </div>
      </body>
    </html>
    """
