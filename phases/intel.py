from core.io import read_lines, write_lines

def simple_scoring(host):
    score = 0

    if "admin" in host:
        score += 5
    if "dev" in host or "staging" in host:
        score += 3
    if "api" in host:
        score += 4

    return score

def run_intel(live_file, outdir):
    hosts = read_lines(live_file)

    scored = [(h, simple_scoring(h)) for h in hosts]
    scored.sort(key=lambda x: x[1], reverse=True)

    outfile = f"{outdir}/priority.txt"

    write_lines(outfile, [f"{h} | score={s}" for h, s in scored])

    return outfile
