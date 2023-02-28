import re


def decrypt(text: str):
    while ".." in text:
        text = re.sub(".\.{2}", "", text, count=1)

    return text.replace(".", "")
