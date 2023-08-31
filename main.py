import subprocess

python_files = ['rece_gui.py', 'doct_gui.py']

processes = []
for file in python_files:
    cmd = ['python', file]
    process = subprocess.Popen(cmd)
    processes.append(process)

for process in processes:
    process.wait()