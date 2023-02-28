import sys
import re


def decrypt(text: str):
    while text.count("..") > 0:
        if set(text) == {"."}:
            text = text.replace(".", "")
        text = re.sub("\w\.\.", "", text)

    return text.replace(".", "")


if __name__ == "__main__":
    data = sys.stdin.read()
    result = decrypt(data.rstrip())
    print(result)
