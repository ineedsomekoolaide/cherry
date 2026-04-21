import shutil
from .runner import log

REQUIRED_TOOLS = [
    "subfinder",
    "amass",
    "assetfinder",
    "httpx"
]

OPTIONAL_TOOLS = [
    "httprobe",
    "naabu"
]

def check_tools():
    missing = []

    for tool in REQUIRED_TOOLS:
        if not shutil.which(tool):
            missing.append(tool)

    if missing:
        log("ERROR", f"Missing tools: {', '.join(missing)}")
        return False

    return True
