# bytes str unicode区别

# 接受str bytes 总返回str的函数
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

if __name__ == "__main__":
    print(to_str("str1"))
    print(to_bytes("str1"))    
    print(to_str(to_bytes("str1")))