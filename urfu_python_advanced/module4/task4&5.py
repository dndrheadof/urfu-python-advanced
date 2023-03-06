from flask import Flask, request
import subprocess
import shlex

app = Flask(__name__)


@app.route("/uptime")
def uptime():
    result = subprocess.run("uptime", capture_output=True)
    return str(result.stdout).split()[3][:-1]


@app.route('/ps', methods=["GET"])
def ps():
    args: list[str] = request.args.getlist('arg')

    command_args = shlex.quote("".join(args))
    result = subprocess.run(f'ps {command_args}',
                            shell=True, capture_output=True, )

    return f"<pre>{result.stdout}</pre>"


if __name__ == "__main__":
    app.run()
