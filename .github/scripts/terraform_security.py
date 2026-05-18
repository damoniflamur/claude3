import json
import os
import glob
import urllib.request

SYSTEM_PROMPT = """You are a security-focused Terraform reviewer.
Apply the security skill below to the provided Terraform files and plan output.
Return ONLY security findings — no score, no cost, no best-practices.

Output format (markdown, keep it concise):

### 🔴 BLOCK
- <issue> — `<resource>` (<file>:<line if known>)
  ```hcl
  <fix snippet>
  ```

### 🟡 WARN
- <issue> — `<resource>`

If there are no findings, output exactly: ✅ No security issues found.
"""

with open(".claude/skills/security.md") as f:
    skill = f.read()

files = ""
for path in sorted(
    glob.glob("**/*.tf", recursive=True) + glob.glob("**/*.tfvars", recursive=True)
):
    with open(path) as f:
        files += f"\n\n### {path}\n{f.read()}"

plan_output = os.environ.get("PLAN_OUTPUT", "")

user_message = f"""## Security Skill
{skill}

## Terraform Files
{files}

## Terraform Plan
{plan_output if plan_output else "(plan not available)"}"""

req = urllib.request.Request(
    "https://api.anthropic.com/v1/messages",
    data=json.dumps({
        "model": os.environ["CLAUDE_MODEL"],
        "max_tokens": 1024,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_message}],
    }).encode(),
    headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
)

with urllib.request.urlopen(req) as res:
    result = json.loads(res.read())["content"][0]["text"]

with open("security.txt", "w") as f:
    f.write(result)
