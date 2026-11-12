#!/usr/bin/env sh
set -eu
command -v uv >/dev/null 2>&1 || { echo "Install uv first: https://docs.astral.sh/uv/" >&2; exit 1; }
uv sync --project apps/concierge-api --extra dev
cp .env.example .env 2>/dev/null || true
echo "Foundation environment ready. No external credentials are required."
