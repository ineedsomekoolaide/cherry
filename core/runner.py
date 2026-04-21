import subprocess
from datetime import datetime

def log(tag, msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [{tag}] {msg}")

def run(cmd, outfile=None, timeout=300):
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )

        if outfile:
            with open(outfile, "w") as f:
                f.write(result.stdout)

        return result.stdout, result.stderr, result.returncode

    except subprocess.TimeoutExpired:
        log("ERROR", f"Timeout: {' '.join(cmd)}")
        return "", "timeout", 1
