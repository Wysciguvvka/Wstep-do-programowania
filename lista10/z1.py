import re

if __name__ == '__main__':
    email = "python2020@gusun_tomail.com"
    match = re.search(r'^(.*)(usun_to)(.*)$', email)
    print(match.group(1) + match.group(3))
