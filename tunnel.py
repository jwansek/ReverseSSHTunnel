import configparser
import subprocess

CONFIG = configparser.ConfigParser()
CONFIG.read("tunnel.conf")

cmd = ["ssh", "-nNTv"]

if CONFIG.has_option("server", "ssh_port"):
    cmd += ["-p", CONFIG.get("server", "ssh_port")]

for section in CONFIG.sections():
    if section.startswith("forward"):
        cmd += ["-R", "%s:%s" % (CONFIG.get(section, "to"), CONFIG.get(section, "from"))]

cmd.append(CONFIG.get("server", "host"))

print("Using command: " + " ".join(cmd))
