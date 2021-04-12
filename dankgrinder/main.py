import subprocess
from webserver import keep_alive

keep_alive()
subprocess.Popen([r"./dankgrinder"])
