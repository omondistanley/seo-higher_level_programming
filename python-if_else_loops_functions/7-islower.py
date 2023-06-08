#!/usr/bin/python3
def islower(c):
    asciiCode = ord(c)
    if asciiCode >= 97 and asciiCode < 123:
        return (True)
    else:
        return (False)
