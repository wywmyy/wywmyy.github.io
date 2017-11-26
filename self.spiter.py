import urllib.request
import os
import re
import random
def open_url(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
	proxies = ['112.114.99.50:8118','115.209.179.186:37433','61.135.217.7:80']
	proxy = random.choice(proxies)
	proxy_support = urllib.request.ProxyHandler({'http':proxy})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	response = urllib.request.urlopen(req)
	html = response.read().decode('utf-8')
	return html

def find_imgs(url):
	html = open_url(url)
	p = re.compile(r'<span>(.+)</span>')
	img_addr = p.findall(html)
	return img_addr

def save_file(folder, img_addr):
	os.mkdir(folder)
	os.chdir(folder)
	lenth = len(img_addr)
	for i in range(lenth):
		duanzi_content = img_addr[i]
		i = str(i)
		filename = i+'.text'
		with open(filename, 'w+') as f:
			f.write(duanzi_content)
		

url = 'https://www.qiushibaike.com/textnew/page/1/?s=4865261'
folder = 'duanzi'
html = open_url(url)
img_addr = find_imgs(url)
save_file(folder,img_addr)



	
	
