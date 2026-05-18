import json
import os
import re
import glob
import urllib.request
from pathlib import Path

# Load agent from .claude/agents/ — first match wins
agent_files = sorted(glob.glob(".claude/agents/*.md"))
if not agent_files:
    raise FileNotFoundError("No agent found in .claude/agents/")
with open(agent_files[0]) as f:
    raw = f.read()
system_prompt = re.sub(r"^---.*?---\s*", "", raw, flags=re.DOTALL).strip()

# Current terraform files
files = ""
for path in sorted(glob.glob("**/*.tf", recursive=True) + glob.glob("**/*.tfvars", recursive=True)):
    with open(path) as f:
        files += f"\n\n### {path}\n{f.read()}"

# Review findings from the PR comment
review = os.environ["PR_REVIEW"]

user_message = f"""The following review findings were raised on this Terraform PR.
Apply fixes for every BLOCK and WARN finding. Leave INFO findings as-is.

## Review Findings
{review}

## Current Terraform Files
{files}

Return ONLY a JSON object — no markdown, no explanation:
{{
  "files": [
    {{"path": "relative/path/to/file.tf", "content": "...complete fixed file content..."}}
  ],
  "summary": "One sentence describing what was fixed."
}}

Only include files that need changes. The content must be the complete file, not a diff."""

req = urllib.request.Request(
    "https://api.anthropic.com/v1/messages",
    data=json.dumps({
        "model": os.environ["CLAUDE_MODEL"],
        "max_tokens": 4096,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_message}],
    }).encode(),
    headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
)

with urllib.request.urlopen(req) as res:
    response_text = json.loads(res.read())["content"][0]["text"]

# Strip markdown code fences if Claude wrapped the JSON
response_text = re.sub(r"^```(?:json)?\s*|\s*```$", "", response_text.strip())

result = json.loads(response_text)

for file_entry in result["files"]:
    path = Path(file_entry["path"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(file_entry["content"])
    print(f"Fixed: {path}")

# Write summary for the PR description
Path("fix_summary.txt").write_text(result.get("summary", "Auto-fix applied."))
