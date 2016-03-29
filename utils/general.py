import string
import random


def generate_random_string(string_length):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(string_length))

if __name__ == "__main__":
    print generate_random_string(10)
