import subprocess
import os

def run_log(cmd, log_file):
    with open(log_file, "a") as f:
        f.write(f"--- Running: {cmd} ---\n")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            f.write(result.stdout)
            f.write(result.stderr)
            f.write(f"--- Exit Code: {result.returncode} ---\n\n")
        except Exception as e:
            f.write(f"Error: {str(e)}\n\n")

log_path = r"c:\Users\gandh\udbhav\career-risk\layoff\debug_log.txt"
if os.path.exists(log_path):
    os.remove(log_path)

run_log("python --version", log_path)
run_log("node --version", log_path)
run_log("npm --version", log_path)
run_log("pip --version", log_path)
run_log("dir", log_path)
run_log("pip install -r backend/requirements.txt", log_path)
run_log("npm install", log_path)
