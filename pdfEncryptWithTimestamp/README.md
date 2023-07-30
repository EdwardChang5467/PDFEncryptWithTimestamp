# PDFEncryptWithTimestamp

## 一、功能

​       main.py实现通过时间戳生成密钥，再用生成的密钥user_key对pdf文件进行加密。

​      encrypt.py实现加密方法，采用owner_key与timestamp混合的方法生成相应的user_key

​     tmp文件夹中log.txt为日志文件，每一条记录前半部分为文件的哈希值，后半部分为生成的user_key

   pdf2image.py实现将pdf转换为图片再合并为pdf，实现了无法复制pdf内容的功能





## 二、复现

python环境为3.9.12

运行前需要先安装PyPDF2,PIL,fitz库

```pip install PyPDF2```

```pip install PIL```

`pip install fitz`



设置main.py文件中待加密文件file和encrypt.py文件中加密后文件保存路径与名称，之后运行main.py

`python main.py`

输出中会显示加密的密钥，相应的输出文件夹中能找到加密后的文件

