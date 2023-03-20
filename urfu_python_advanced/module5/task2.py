from flask import Flask, request
import subprocess
import shlex
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field
from wtforms.validators import InputRequired, Email, ValidationError, NumberRange


app = Flask(__name__)


class RunCodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[NumberRange(min=1, max=30)])


@app.route('/runcode', methods=["POST"])
def run_code():
    form = RunCodeForm()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        cmd = ["prlimit", "--nproc=1:1", "python", "-c", code]

        r = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        try:
            output, errors = r.communicate(timeout=timeout)
            if errors:
                return errors
            return output
        except:
            r.kill()
            raise ValueError("Timeout reached")

    return f"Invalid input: {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
