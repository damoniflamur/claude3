import json
import os
import re
import glob
import urllib.request

# Agent definition → system prompt (strip YAML frontmatter)
with open(".claude/agents/terraform-reviewer.md") as f:
    raw = f.read()
system_prompt = re.sub(r"^---.*?---\s*", "", raw, flags=re.DOTALL).strip()

# Terraform files
files = ""
for path in sorted(glob.glob("**/*.tf", recursive=True) + glob.glob("**/*.tfvars", recursive=True)):
    with open(path) as f:
        files += f"\n\n### {path}\n{f.read()}"

# Skills selected by PR labels — defaults to security
SKILL_MAP = {
    "security": ".claude/skills/security.md",
    "cost": ".claude/skills/cost.md",
    "best-practices": ".claude/skills/best-practices.md",
}
labels = [l.strip() for l in os.environ.get("PR_LABELS", "").split(",") if l.strip()]
skill_files = [SKILL_MAP[l] for l in labels if l in SKILL_MAP] or [SKILL_MAP["security"]]

skills = ""
for path in skill_files:
    with open(path) as f:
        skills += f"\n\n---\n{f.read()}"

user_message = f"""## Review Skills
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
