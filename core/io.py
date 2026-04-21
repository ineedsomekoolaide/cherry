import os

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def read_lines(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [x.strip() for x in f if x.strip()]

def write_lines(path, lines):
    with open(path, "w") as f:
        f.write("\n".join(sorted(set(lines))))
