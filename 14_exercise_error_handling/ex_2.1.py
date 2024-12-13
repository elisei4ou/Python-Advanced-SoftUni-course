import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAtSymbolError(Exception):
    pass


class NameMustContainOnlyCharsNumbersUnderscoresError(Exception):
    pass


email = input()

LEN_NAME = 4
DOMAINS = ("com", "bg", "org", "net")
pattern = r"\w+"

while email != "End":

    if email.count("@") > 1:
        raise MustContainOnlyOneAtSymbolError("Email must contain only one '@' symbol!")

    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    elif len(email.split("@")[0]) < 4:
        raise NameTooShortError("Name must be more than 4 characters!")

    elif email.split(".")[-1] not in DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")

    elif len(re.findall(pattern, email.split("@")[0])) > 1:
        raise NameMustContainOnlyCharsNumbersUnderscoresError(
            "Name must contain only characters, numbers and underscores!"
        )

    print("Email is valid")
    email = input()
