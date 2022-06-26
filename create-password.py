import crypt, getpass
password = (crypt.crypt(getpass.getpass(),
    crypt.mksalt(crypt.METHOD_SHA512)))
f = open("newuser.pass", "w")
f.write(password)
f.close()
