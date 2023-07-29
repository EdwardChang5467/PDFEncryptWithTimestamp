import datetime
import hashlib  # 待加密信息
import PyPDF2

# 计算文件hash
def filehash_cal(filepath):
    file = open(filepath, "rb")
    md = hashlib.md5()
    md.update(file.read())
    hash_res = md.hexdigest()
    return hash_res

#加密方法
def encryption(pwd):
    """
    加密
    时间戳（16位）每个数字加6后转为16进制，共16位
    pwd加密为16为
    pwd16位在奇数位置，时间戳加密在偶数位
    :param pwd:
    :return:
    """
    time_stamp_int = int(datetime.datetime.now().timestamp() * 10 ** 6)
    time_stamp_str_lst = list(str(time_stamp_int))
    time_stamp_str_lst = list(map(lambda x: hex(int(x) + 6).__str__().replace('0x', ''), time_stamp_str_lst))
    hl = hashlib.md5()
    hl.update(pwd.encode("utf-8"))
    pwd_hl_lst = list(hl.hexdigest()[8:-8])
    result = ['0'] * 32
    result[0::2] = pwd_hl_lst
    result[1::2] = time_stamp_str_lst
    return ''.join(result)

#解密方法
def decrypt(pwd):
    assert len(pwd) == 32
    pwd_lst = list(pwd)
    time_stamp_str_lst = pwd_lst[1::2]
    time_stamp = int(int(''.join(list(map(lambda x: str(int(x, 16) - 6), time_stamp_str_lst)))) / 10 ** 6)
    pwd_de = ''.join(pwd_lst[0::2])
    return pwd_de, time_stamp

#将pdf加密
def encryptPDF(file,userpwd):
    pdf_reader = PyPDF2.PdfReader(file)
    pdf_writer = PyPDF2.PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    pdf_writer.encrypt(str(userpwd))
    with open('./encrypted.pdf', 'wb') as out_file:
        pdf_writer.write(out_file)


#测试加密与解密
# print(datetime.datetime.now())
# print(datetime.datetime.now().timestamp().__str__())
# pwd = encryption("aaa")
# print(pwd)
# pwd_de, time_stamp = decrypt(pwd)

# print(pwd_de, time_stamp)