import subprocess

subprocess.run(["echo", "Hello from Chirayu"])
# run command in shell

result=subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("STDOut:", result.stdout)
print("STDerr:", result.stderr)