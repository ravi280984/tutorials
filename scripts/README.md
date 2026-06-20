# Repository scripts

This directory is for maintenance and validation utilities used across the repository. Tutorial applications belong in `demos/`.

## Available scripts

### Check Markdown links

```powershell
python scripts/check_links.py
```

The script validates relative links and local image references. External URLs are intentionally not requested, keeping the check fast and deterministic.
