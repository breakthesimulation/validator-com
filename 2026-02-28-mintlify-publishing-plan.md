# Mintlify Publishing Plan

## Current State
- 44+ articles in `/vault/Quill/validator-com-articles/`
- Need to publish to validator.com (uses Mintlify)

## Mintlify Options

### Option 1: GitHub Sync (RECOMMENDED)
Mintlify supports connecting a GitHub repo. Changes pushed to `docs/` folder auto-deploy.

**Steps:**
1. Create a GitHub repo for validator-com-docs
2. Connect to Mintlify via web dashboard
3. Push articles to `docs/` folder
4. Auto-deploys on push

**Pros:** Automatic, version control, rollback
**Cons:** Need to structure docs folder

### Option 2: Mintlify CLI
Mintlify has a CLI for local development and push:

```bash
npm install -g mintlify
mintlify login
mintlify push --docs ./docs
```

**Pros:** Push from command line
**Cons:** Requires auth, not automated

### Option 3: Mintlify API
Mintlify has a REST API but publishing endpoints may require Enterprise.

## Recommended Pipeline

1. Create GitHub repo: `montgomery-ai-labs/validator-com-docs`
2. Structure docs/ folder with articles
3. Connect repo to Mintlify in validator.com dashboard
4. Push from vault: copy articles → docs/ → git push

## Quick Proof of Concept Script

```python
#!/usr/bin/env python3
import shutil, subprocess

SOURCE = "/vault/Quill/validator-com-articles/"
DEST = "/vault/Dev/validator-com/docs/"

def sync():
    # Copy articles to docs folder
    shutil.copytree(SOURCE, DEST, dirs_exist_ok=True)
    
    # Commit and push
    subprocess.run(["git", "add", "."], cwd=DEST)
    subprocess.run(["git", "commit", "-m", "Update docs"], cwd=DEST)
    subprocess.run(["git", "push"], cwd=DEST)
    print("✅ Pushed to GitHub - Mintlify will deploy")
```

## Next Steps
1. Create GitHub repo
2. Connect to Mintlify (Seb needs to do this in validator.com dashboard)
3. Build sync script
