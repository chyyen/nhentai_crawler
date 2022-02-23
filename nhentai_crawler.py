from bs4 import BeautifulSoup as BS
import requests
import urllib.request 
import lxml
import os

Header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
file_path = ''
img_prefix = 'https://i.nhentai.net/galleries/'

def Init() :
	global code
	hentai_id = input('Enter id : ')
	url = f'https://nhentai.net/g/{hentai_id}/'
	web = requests.get(url, headers=Header)
	code = BS(web.content,'lxml')

def get_info() :
	title = code.find('h2')
	name = title.get_text()
	print(f'Hentai name : {name}')
	
def Download() :
	pages = code.find_all('div', class_='thumb-container')
	print(f'Hentai pages : {len(pages)}')
	cnt = int(1)
	for page in pages :
		link = page.a.find('img')
		id = link['data-src'].split('/')[-2]
		print(f'Downloading ... {img_prefix}{id}/{cnt}.jpg')
		open(f'{file_path}{cnt}.jpg','wb').write(requests.get(f'{img_prefix}{id}/{cnt}.jpg', headers=Header).content)
		cnt += 1

Init()
get_info()
Download()
print('Finish !')
