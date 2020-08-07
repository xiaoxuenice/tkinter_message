import  hashlib
def pd(password,jiami):
        salt = "1234^&*fa;56~!@#$%=[]ef9acvd'\/,./ZXCYWQET"
        def md5hex(ascii_str):
            return hashlib.md5(ascii_str.encode('ascii')).hexdigest()
        hash2 = md5hex(md5hex(password) + salt)
        print("woshiyanzheng de {} ".format(hash2))
        if str(hash2) == str(jiami):
            return "ok"
        else:
            return 'error'
def  sc(password):
    salt = "1234^&*fa;56~!@#$%=[]ef9acvd'\/,./ZXCYWQET"
    def md5hex(ascii_str):
        return hashlib.md5(ascii_str.encode('ascii')).hexdigest()
    hash2 = md5hex(md5hex(password) + salt)
    print("woshi shengchengde {}".format(hash2))
    return hash2