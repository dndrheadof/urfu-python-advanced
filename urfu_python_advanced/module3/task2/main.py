import re


def decrypt(text: str):
    while text.count("..") > 0:
        if set(text) == {"."}:
            text = text.replace(".", "")
        text = re.sub(".\.\.", "", text)

    return text.replace(".", "")
