import base64
def encode(yuanwen):
    shuchu = base64.b64encode(bytes(yuanwen,'utf-8'))
    return(shuchu)
def decode(yuanwen):
    shuchu = base64.b64decode(yuanwen)
    shuchu = shuchu.decode()
    return(shuchu)