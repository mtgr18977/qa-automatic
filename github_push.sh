#!/bin/bash
ORG_OR_USER="${1:-mtgr18977}"
REPO_NAME="${2:-qa-automation-playwright-py_recreated}"
DESCRIPTION="Playwright (Python) + pytest QA starter"

set -e
git init
git add .
git commit -m "Initial commit - QA automation starter"

if command -v gh >/dev/null 2>&1; then
  gh repo create "$ORG_OR_USER/$REPO_NAME" --public --description "$DESCRIPTION" --source=. --remote=origin --push
else
  echo "gh CLI not found. Create a repo manually at https://github.com/new and set remote:"
  echo "git remote add origin git@github.com:$ORG_OR_USER/$REPO_NAME.git"
  echo "git push -u origin main"
fi
