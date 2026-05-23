#!/usr/bin/env python3
import os, json, subprocess, datetime

def get_open_swarm_status():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sw_root = "/home/administrador/.hermes/openswarm"
    log = "/home/administrador/openswarm.log"
    # gather log tail
    last_lines = ""
    try:
        with open(log, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            last_lines = "".join(lines[-200:]) if lines else ""
    except Exception as e:
        last_lines = f"Error reading log: {e}"
    # agents present
    agents = []
    try:
        for name in os.listdir(sw_root):
            p = os.path.join(sw_root, name)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, "run_utils.py")):
                agents.append(name)
    except Exception as e:
        agents = [f"error reading agents: {e}"]
    # open swarm process check
    try:
        ps = subprocess.check_output(["bash","-lc","ps -eo pid,etime,cmd | grep run_utils.py | grep -v grep"]).decode("utf-8","ignore").strip()
    except Exception:
        ps = ""
    return {
        "timestamp": now,
        "agents_found": agents,
        "log_last_200": last_lines,
        "ps_run_utils": ps
    }


def write_report(path):
    s = get_open_swarm_status()
    with open(path, "w", encoding="utf-8") as f:
        f.write("OpenSwarm Status Report\n")
        f.write("======================\n\n")
        for k, v in s.items():
            f.write(f"{k}: {v}\n\n")


def main():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = "/home/administrador/openswarm_reports"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"open_swarm_status_{ts}.txt")
    write_report(path)
    print(path)

if __name__ == "__main__":
    main()
