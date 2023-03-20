import subprocess
import os
from flask import Flask


def start_server(port: int):
    command = ['lsof', '-i', f':{port}']
    r = subprocess.Popen(command, stdout=subprocess.PIPE)
    try:
        output, errors = r.communicate()
        result = output.decode().split('\n')
        if len(result):
            os.kill(int(result[1].split()[1]), 9)
        app = Flask(__name__)
        app.run(port=port)
    except Exception:
        r.kill()


start_server(8000)
