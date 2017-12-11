import os, subprocess, logging

def log_cmd_output(message, cmd, cwd=None):
    logging.info(message)
    print("$ " + (" ".join(cmd)))
    print(cmd_output(cmd, cwd))

def cmd_output(cmd, cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    return subprocess.check_output(cmd, cwd=cwd).strip().decode("UTF-8")

