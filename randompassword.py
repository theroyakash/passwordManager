import secrets
import string

# secure random string
def generate(size:int, ascii_letters=True, digits = True, punctuation = True):
    if (ascii_letters and digits and punctuation):
        chars = string.ascii_letters + string.digits + string.punctuation
    elif (ascii_letters and digits and not punctuation):
        chars = string.ascii_letters + string.digits + string.punctuation
    elif (ascii_letters and not digits and not punctuation):
        chars = string.ascii_letters
    elif (ascii_letters and not digits and punctuation):
        chars = string.ascii_letters + string.punctuation

    secure_str = ''.join((secrets.choice(chars) for i in range(size)))

    return secure_str