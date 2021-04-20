

def get_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


def main():
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = get_name(email)
        correct_name = input(f"Is your name {name}?\n "
                             "(Y/N)")
        if correct_name.upper() != "Y" and correct_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
