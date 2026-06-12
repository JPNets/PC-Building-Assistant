import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

def load_json(filename: str):
    path = DATA_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_build(build: dict, filename: str):
    out = ROOT / "saved_builds"
    out.mkdir(exist_ok=True)
    path = out / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(build, f, indent=2)
    return str(path)
