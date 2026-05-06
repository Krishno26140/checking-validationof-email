import re 

def check_email(email: str) -> bool:
    pattern = r"[a-zA-Z0-9_.+]+@[a-zA-Z]+\.[a-z]{3}"
    return bool(re.fullmatch(pattern, email))

def main():
    email = input("Enter your email: ").strip()

    if not email:
        print("Email cannot be empty")
        return

    if check_email(email):
        print("Email is valid")
    else:
        print("Email is not valid")

if __name__ == "__main__":
    main()