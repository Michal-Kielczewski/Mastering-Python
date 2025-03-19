def is_even(num):
    return num % 2 == 0


def slugyify(phrase):
    phrase = phrase.lower().strip().replace(" ", "-")
    return phrase

print(slugyify("Hello World"))