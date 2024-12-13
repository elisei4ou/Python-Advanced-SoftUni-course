class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainsOnlyOneAtSymbolError(Exception):
    pass


class InvalidMailErrors(Exception):
    pass


class NameNOTContainDot(Exception):
    pass


email = input()
domains = ["com", "bg", "org", "net"]
mails = ["gmail", "abv", "yahoo"]

while email != "End":

    try:
        name = email[:email.index("@")]
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if "." in name:
            raise NameNOTContainDot("Name can't contain '.'(Dot)")
    except ValueError:
        pass

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if email.count("@") > 1:
        raise MustContainsOnlyOneAtSymbolError("Email must contain only one '@' symbol")

    if email[email.index("@") + 1:email.index(".")] not in mails:
        raise InvalidMailErrors("Mail is not in the valid ones")

    if email.split(".")[-1] not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()