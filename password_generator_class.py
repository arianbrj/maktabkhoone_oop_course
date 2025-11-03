from abc import ABC
from abc import abstractmethod
import random
import string

class Password(ABC):
    @property
    @abstractmethod
    def generate_password(self):
        pass

class NumberPassword(Password):
    def generate_password(self):
        digits = string.digits
        return "".join(random.choice(digits) for _ in range(20))


class LetterPassword(Password):
    def generate_password(self):
        chars = string.ascii_letters
        return "".join(random.choice(chars) for _ in range(20))


class MixedPassword(Password):
    def generate_password(self):
        characters = string.digits + string.ascii_letters + "!@#$%^*()_+-/.?\}{[]}><~:;`|"
        return "".join(random.choice(characters) for _ in range(11))

# a = NumberPassword()
# print(a.generate_password())

# b = LetterPassword()
# print(b.generate_password())

# c = MixedPassword()
# print(c.generate_password())

print(MixedPassword().generate_password())
# print(len(string.digits + string.ascii_letters + "!@#$%^*()_+-/.?\}{[]}><~:;`|"))
