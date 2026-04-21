import sys
import os

from core.tools import check_tools
from core.runner import log
from core.io import ensure_dir

from phases.subdomains import run_subdomains
from phases.hosts import run_hosts
from phases.intel import run_intel


def main(domain):
    if not domain:
        log("ERROR", "No domain provided")
        return

    base = f"assessment_{domain}"
    ensure_dir(base)

    log("SYSTEM", f"Starting assessment for: {domain}")

    # -------------------------
    # TOOL VALIDATION
    # -------------------------
    if not check_tools():
        log("ERROR", "Missing required tools — aborting")
        return

    # -------------------------
    # PHASE 1: SUBDOMAINS
    # -------------------------
    subs_file = run_subdomains(domain, base)
    if not subs_file:
        log("ERROR", "Subdomain phase failed")
        return

    # -------------------------
    # PHASE 2: LIVE HOSTS
    # -------------------------
    live_file = run_hosts(subs_file, base)
    if not live_file:
        log("ERROR", "Host discovery failed")
        return

    # -------------------------
    # PHASE 3: INTEL
    # -------------------------
    intel_file = run_intel(live_file, base)

    log("SYSTEM", "Assessment complete")
    log("OUTPUT", base)

    return base


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <domain>")
        sys.exit(1)

    main(sys.argv[1])
