import json
import os
import re
import glob
import urllib.request

# Agent definition → system prompt (strip YAML frontmatter)
with open(".claude/agents/terraform-reviewer.md") as f:
    raw = f.read()
system_prompt = re.sub(r"^---.*?---\s*", "", raw, flags=re.DOTALL).strip()

# All skills
skills = ""
for path in sorted(glob.glob(".claude/skills/*.md")):
    with open(path) as f:
        skills += f"\n\n---\n{f.read()}"

# Terraform files
files = ""
for path in sorted(glob.glob("**/*.tf", recursive=True) + glob.glob("**/*.tfvars", recursive=True)):
    with open(path) as f:
        files += f"\n\n### {path}\n{f.read()}"

user_message = f"""## Skills
{skills}

## Terraform Files
{files}"""

req = urllib.request.Request(
    "https://api.anthropic.com/v1/messages",
    data=json.dumps({
        "model": os.environ["CLAUDE_MODEL"],
        "max_tokens": 2048,
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
    review = json.loads(res.read())["content"][0]["text"]

with open("review.txt", "w") as f:
    f.write(review)
