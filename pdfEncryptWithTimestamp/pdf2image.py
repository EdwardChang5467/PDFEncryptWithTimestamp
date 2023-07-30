import os
import sys
import fitz
from PIL import Image

def pdf2image(filename):
	#  打开PDF文件，生成一个对象
	doc = fitz.open(filename)
	print("共",doc.page_count,"页")
	for pg in range(doc.page_count):
		print("\r转换为图片",pg+1,"/",doc.page_count,end="\n")
		page = doc[pg]
		rotate = int(0)
		# 每个尺寸的缩放系数为8，这将为我们生成分辨率提高64倍的图像。一般设为2
		zoom_x = 8.0
		zoom_y = 8.0
		trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
		pm = page.get_pixmap(matrix=trans, alpha=False)
		pm.save(filename+'_tu'+'{:02}.png' .format(pg))

def image2pdf():
	# 定义文件夹路径和PDF文件名
	folder_path = './tmp/'
	pdf_filename = 'output.pdf'
	# # 将PNG文件转换为Pillow Image对象并添加到列表中
	image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]
	image_list = []
	for file_path in image_files:
		img = Image.open(file_path)
		image_list.append(img)
	# 找到所有PNG文件
	image_list[0].save(pdf_filename, "PDF" ,resolution=100.0, save_all=True, append_images=image_list[1:])
