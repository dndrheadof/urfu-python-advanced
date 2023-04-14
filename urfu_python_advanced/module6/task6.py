from flask import Flask, url_for

app = Flask(__name__)


@app.route("/hello_world")
def hello_world():
    return "Привет, мир"


@app.route("/goodbye_world")
def goodbye_world():
    return "Пока, мир"


@app.route("/what")
def what():
    return "ЧТОООООО"


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


# Ссылка из самого задания
# https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app/13318415#13318415
@app.errorhandler(404)
def routes(err):
    html = ""
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))

    for link, name in links:
        html += f'<a href="{link}">{name}</a><br>'
    return f"Данной страницы не существует, попробуйте:<br>{html}"


if __name__ == "__main__":
    app.run()
