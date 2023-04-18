def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        new_email = email.replace('@' + old_domain, '@' + new_domain)
        return new_email
    return email

# Example usage
email =input( "enter your email : ")
old_domain =input("enter your old domain eg:gmail.com: ")
new_domain =input( "enter your new domain eg:loyolacollege.edu : ")
new_email = replace_domain(email, old_domain, new_domain)
print(new_email)

