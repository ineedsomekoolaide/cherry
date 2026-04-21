from core.runner import run, log
from core.io import read_lines, write_lines
import shutil

def run_httpx(subs):
    out, err, code = run([
        "httpx",
        "-silent",
        "-no-color"
    ])
    return out.splitlines()

def run_httprobe(subs):
    out, _, _ = run(["httprobe"])
    return out.splitlines()

def run_hosts(subs_file, outdir):
    subs = read_lines(subs_file)

    if not subs:
        log("ERROR", "No subdomains to probe")
        return None

    log("HOSTS", "Probing live hosts")

    if shutil.which("httpx"):
        live = run_httpx(subs)
    elif shutil.which("httprobe"):
        log("HOSTS", "Falling back to httprobe")
        live = run_httprobe(subs)
    else:
        log("ERROR", "No probing tools available")
        return None

    outfile = f"{outdir}/live.txt"
    write_lines(outfile, live)

    log("HOSTS", f"{len(live)} live hosts")

    return outfile
