#!/bin/bash
# Starts the GitHub MCP server using the token from gh CLI (no hardcoded secrets)
export GITHUB_PERSONAL_ACCESS_TOKEN=$(gh auth token)
exec npx -y @modelcontextprotocol/server-github
