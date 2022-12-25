import random
import string


def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters +
                       string.digits + string.punctuation, k=length))
    return password


print("Password: ", generate_password(10))
print("Password: ", generate_password(16))
print("Password: ", generate_password(20))
print("Password: ", generate_password(24))
print("Password: ", generate_password(30))
