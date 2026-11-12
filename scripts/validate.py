"""Validate JSON fixture syntax without accessing external services."""

import json
from pathlib import Path


def main() -> None:
    fixtures = Path("data/fixtures")
    files = sorted(fixtures.glob("*.json"))
    for path in files:
        json.loads(path.read_text(encoding="utf-8"))
    print(f"Validated {len(files)} fictional fixture files")


if __name__ == "__main__":
    main()
