import requests

from bs4 import BeautifulSoup
from bs4.element import Tag


def test_get_douban():
    for i in range(1, 11):
        get_douban(i)


def get_douban(offset):
    """
    bs测试 获取豆瓣电影top250
    :param offset: 页码
    :return:
    """
    print()
    url = f'https://movie.douban.com/top250?start={(offset - 1) * 25}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
    }
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text)
    ol = bs.find_all('ol', attrs={'class': 'grid_view'})[0]
    li_list = ol.find_all('li')
    for li in li_list:
        # print(li)
        print('=' * 100)
        print(get_movie_info(li))


def get_movie_info(tag: Tag):
    order = tag.find('em').text
    titles = tag.find_all('span', {'class': 'title'})
    title_list = []
    for t in titles:
        title_list.append(t.text)
    title_others = tag.find_all('span', {'class': 'other'})
    for t in title_others:
        title_list.append(t.text)
    name = ''.join(title_list)
    summ_info = tag.find('p', {'class': ''}).text.strip()
    star = tag.find('div', {'class': 'star'})
    score = star.find('span', {'class': 'rating_num', 'property': 'v:average'}).text
    p_num = star.find_all('span')[-1].text
    href = tag.find('a', {'class': ''}).get('href')
    return MovieInfo(order, name, score, summ_info, p_num, href)


class MovieInfo:
    """
    影片信息
    """

    def __init__(self, order, name, score, summ_info, p_num, href):
        """
        :param order:排名
        :param name: 名称
        :param score: 评分
        :param summ_info:简介
        :param p_num: 评价人数
        :param href: 链接
        """
        self.order = order
        self.name = name
        self.score = score
        self.summ_info = summ_info
        self.p_num = p_num
        self.href = href

    def __str__(self):
        return f'排名:{self.order}\n' \
               f'影片名:{self.name}\n' \
               f'得分:{self.score}\n' \
               f'简介:{self.summ_info}\n' \
               f'评价人数:{self.p_num}\n' \
               f'链接:{self.href}'
