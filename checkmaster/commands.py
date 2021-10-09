import subprocess


def run_command(command) -> subprocess.CompletedProcess:
    return  subprocess.run(
        command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

