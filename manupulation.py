# Problem 1
def process_email(email):
    cleaned_email = email.strip()
    cleaned_email = cleaned_email.lower()
    username, domain = cleaned_email.split("@")
    return(username, domain)

#emails = ["  MAHIR22@YaHoo.COM", "FArzNA@gMAIL.com  "]
#for e in emails:
    #print(process_email(e))

# problem 2
cards = ["1234567812345678", "9876543298765432", "1111222233334444"]
masked_version = ["*" * 12 + card[-4:] for card in cards]
print(masked_version)