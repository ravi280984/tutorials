"""Validate relative file links in repository Markdown documents."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIPPED_PREFIXES = ("http://", "https://", "mailto:", "#")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and ".venv" not in path.parts
    )


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>").split("#", maxsplit=1)[0]
    if not target or target.lower().startswith(SKIPPED_PREFIXES):
        return None
    return (source.parent / unquote(target)).resolve()


def main() -> int:
    failures: list[str] = []
    files = markdown_files()

    for source in files:
        content = source.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            target = local_target(source, match.group(1))
            if target is not None and not target.exists():
                source_name = source.relative_to(ROOT)
                failures.append(f"{source_name}: missing {match.group(1)}")

    if failures:
        print("Broken local links:")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print(f"Checked {len(files)} Markdown files: all local links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
