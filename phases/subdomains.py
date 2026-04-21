from concurrent.futures import ThreadPoolExecutor
from core.runner import run, log
from core.io import write_lines
from core.dedupe import unique

def subfinder(domain):
    out, _, _ = run(["subfinder", "-silent", "-d", domain])
    return out.splitlines()

def amass(domain):
    out, _, _ = run(["amass", "enum", "-passive", "-d", domain])
    return out.splitlines()

def assetfinder(domain):
    out, _, _ = run(["assetfinder", "--subs-only", domain])
    return out.splitlines()

def run_subdomains(domain, outdir):
    log("RECON", "Starting subdomain enumeration")

    funcs = [subfinder, amass, assetfinder]

    results = []
    with ThreadPoolExecutor(max_workers=3) as ex:
        futures = [ex.submit(f, domain) for f in funcs]
        for f in futures:
            try:
                results.extend(f.result())
            except:
                pass

    subs = unique(results)

    outfile = f"{outdir}/subs.txt"
    write_lines(outfile, subs)

    log("RECON", f"Found {len(subs)} subdomains")

    return outfile
