with open("words.txt") as F:
    words = list(filter(lambda x: len(x) > 3, F.read().split("\n")))


def is_strong_password(password):
    return not any([word.lower() in password.lower() for word in words])


print(is_strong_password("$mfKeBishopfn32_vjerf"))  # False
print(is_strong_password("K@JKLD()*U@LKJASD0-9"))  # True
