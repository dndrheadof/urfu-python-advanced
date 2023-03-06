from typing import Optional
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field
from wtforms.validators import InputRequired, Email, ValidationError

app = Flask(__name__)


class PhoneValidator():
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min_value = min
        self.max_value = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if field.data is None or len(str(field.data)) < self.min_value or len(str(field.data)) > self.max_value:
            raise ValidationError(message=self.message)


def phone_validator(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if field.data is None or len(str(field.data)) < min or len(str(field.data)) > max:
            raise ValidationError(message=message)

    return _number_length


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(
        validators=[InputRequired(), PhoneValidator(min=7, max=11, message="Incorrect phone format")])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input: {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
