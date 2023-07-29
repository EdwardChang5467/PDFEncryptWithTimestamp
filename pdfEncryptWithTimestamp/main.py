import encrypt
import os

encrypted_text_hashtable = {}

def read_txt():
	if not os.path.exists('./tmp'):
		os.mkdir('./tmp')
	file_hash = []
	encrypted_text = []
	with open('./tmp/log.txt','r') as fr:
		line = fr.readline()
		
		while(line):
			file_hash.append(line[:32])
			encrypted_text.append(line[32:].strip())
			line = fr.readline()
	fr.close()
	return file_hash, encrypted_text

def load_txt():
	file_hash, encrypted_text = read_txt()
	for h in file_hash:
		encrypted_text_hashtable[h] = encrypted_text[file_hash.index(h)]

def update_txt(new_file_hash, new_encrypted_text):
	file_hash, encrypted_text = read_txt()
	if new_file_hash not in file_hash:
		file_hash.append(new_file_hash)
		encrypted_text.append(new_encrypted_text)
	load_txt()
	encrypted_text_hashtable[new_file_hash] = new_encrypted_text
	with open('./tmp/log.txt','w') as fw:
		for h in file_hash:
			fw.write(h + encrypted_text_hashtable[h] + '\n')
		fw.close()


if __name__ == '__main__':
	file = "./tmp/test.pdf"
	hashres = encrypt.filehash_cal(file)
	text = encrypt.encryption("aaa")
	file_hash, encrypted_text = read_txt()
	update_txt(hashres, text)
	if hashres in file_hash:
		key = encrypted_text[file_hash.index(hashres)]
		print("文件密码:" + key)
	encrypt.encryptPDF(file,key)

