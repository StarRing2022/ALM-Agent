import requests  # 向页面发送请求
from bs4 import BeautifulSoup as BS  # 解析页面
import random

def get_news():
	"""爬取微博热搜排行榜数据"""
	# 目标地址
	url = 'https://s.weibo.com/top/summary?cate=realtimehot'
	# 请求头
	header = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
		'Host': 's.weibo.com',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
		'Accept-Encoding': 'gzip, deflate, br',
		# 定期更换Cookie
		'Cookie': 'UOR=passport.weibo.com,s.weibo.com,www.baidu.com; Apache=7551475425663.209.1647609689873; SINAGLOBAL=7551475425663.209.1647609689873; ULV=1647609689909:1:1:1:7551475425663.209.1647609689873:; _s_tentry=passport.weibo.com; SUB=_2AkMVaAhvf8NxqwJRmf0QyWjgb41-yQ3EieKjNPm0JRMxHRl-yT9jqhQFtRB6PugmgMvPC2fUVQ7R-4Ysb5J1lFblsZE1; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WW1y17H9-xuF5ihOrnFNVWk; ALF=1671407688'
	}
	r = requests.get(url, headers=header)  # 发送请求
	soup = BS(r.text, 'html.parser')
	items = soup.find('section', {'class': 'list'})
	newstextlst = []
	newstext = ""
	
	for li in items.find_all('li'):
		try:
			view_count = li.find('em').text
		except:
			view_count = ""
		
		# 标题
		text = li.find('span').text
		text = text.strip().replace(view_count, "")+"。"
		newstextlst.append(text)
	
	random_index = random.randint(0,len(newstextlst)-1)
	newstext = newstextlst[random_index]

	return newstextlst,newstext



# if __name__ == '__main__':
# 	newstextlst,newstext = get_news()
# 	print(newstextlst)
# 	print(newstext)