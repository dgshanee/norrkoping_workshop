import os
import sys

from multiprocessing import Pool
import subprocess


def run_command(path):
    command = "bash {}".format(path)
    subprocess.Popen(command, shell=True)

sys.stderr = open("../outputs/error", 'w')
sys.stdout = open("../outputs/output", 'w')

pool = Pool()
pool.map(run_command, [file for file in os.listdir(".") if file.endswith(".sh")])
