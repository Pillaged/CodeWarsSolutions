def rot13(message):
    m2 = ""
    for char in message:
        pholder = ord(char)
        if 122>= pholder >= 110 or 90>=pholder>=78:
            pholder -= 13
        elif 110>pholder>=97 or 78>pholder>=65:
            pholder += 13
        m2 += (chr(pholder))
    return m2
