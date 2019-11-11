import re
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('driver/chromedriver', chrome_options=options)


link_genre = {'GN0100': '발라드', 'GN0200': '댄스', 'GN0300': '랩/힙합', 'GN0400': 'R&B', 'GN0500': '인디음악',
              'GN0600': '록/메탈', 'GN0700': '트로트', 'GN0800': '포크/블루스'}


def music_link():
    # 한페이지 더 크롤링해야함
    for genre in link_genre:
        make_list('https://www.melon.com/genre/song_list.htm?gnrCode=' + genre + '&steadyYn=Y', genre)
        make_list('https://www.melon.com/genre/song_list.htm?gnrCode='+genre+'&steadyYn=Y#params%5BgnrCode%5D='+genre+
                  '&params%5BdtlGnrCode%5D=&params%5BorderBy%5D=NEW&params%5BsteadyYn%5D=Y&po=pageObj&startIndex=51',
                  genre)


def make_list(link, genre):
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rank01")))

    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    link_list = soup.find('div', class_='service_list_song').findAll("a", href=re.compile(
        "^javascript:melon.link.goSongDetail\('"))

    for link in link_list:
        print(link.attrs['href'][36:-3])
        crawing(link.attrs['href'][36:-3], genre)


def crawing(link, genre):
    driver.get('https://www.melon.com/song/detail.htm?songId=' + link)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "bg_album_frame")))
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    img_url = soup.find('a', class_='image_typeAll').find('img').attrs['src']
    urllib.request.urlretrieve(img_url, 'imgs/'+link+".jpg")

    title_raw = soup.find('div', class_='song_name').contents[2]
    title = title_raw.replace('\t', '').replace('\n', '')

    meta = soup.find('div', class_='meta').findAll('dd')
    years = meta[1].text[0:4]

    like = int(soup.find('span', id='d_like_count').text.replace(',', ''))
    print(int(link), title, years, link_genre[genre], like)


music_link()
driver.quit()
