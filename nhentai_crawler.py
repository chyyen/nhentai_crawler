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
	global name
	title = code.find('h2')
	name = title.get_text()
	print(f'Hentai name : {name}')
	

def Download() :
	# create folder
	folder = file_path+name+'\\'
	try :
		os.mkdir(folder)
	except :
		pass

	pages = code.find_all('div', class_='thumb-container')
	print(f'Hentai pages : {len(pages)}')
	# get image url
	link = pages[0].a.find('img')
	id = link['data-src'].split('/')[-2]
	img_url = img_prefix+id+'/'
	# download
	for cnt in range(1,len(pages)+1) :
		print(f'Downloading ... {img_url}{cnt}.jpg')
		open(f'{folder}{cnt}.jpg','wb').write(requests.get(f'{img_url}{cnt}.jpg', headers=Header).content)


Init()
get_info()
Download()
print('Finish !')
