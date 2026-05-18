import json
import os
import glob
import urllib.request

files = ""
for path in sorted(glob.glob("**/*.tf", recursive=True) + glob.glob("**/*.tfvars", recursive=True)):
    with open(path) as f:
        files += f"\n\n### {path}\n{f.read()}"

skills = ""
with open(".claude/skills/security.md") as f:
    skills = f.read()

prompt = f"""You are a senior DevOps engineer reviewing a Terraform PR.
Apply every check defined in the skills below. Score out of 100.
List findings with severity (BLOCK / WARN / INFO) and include an hcl fix snippet for every issue.

## Review Skills
{skills}

## Terraform Files
{files}"""

req = urllib.request.Request(
    "https://api.anthropic.com/v1/messages",
    data=json.dumps({
        "model": os.environ["CLAUDE_MODEL"],
        "max_tokens": 2048,
        "messages": [{"role": "user", "content": prompt}],
    }).encode(),
    headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
)

with urllib.request.urlopen(req) as res:
    review = json.loads(res.read())["content"][0]["text"]

with open("review.txt", "w") as f:
    f.write(review)
