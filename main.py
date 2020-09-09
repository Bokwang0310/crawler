import requests
from bs4 import BeautifulSoup

query = "안녕"  # 검색어
index = 1  # 페이지 인덱스

url = f"https://search.naver.com/search.naver?&where=news&query={query}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=27&start={(index - 1)*10 + 1}"
html = requests.get(url).text

bs = BeautifulSoup(html, "html.parser")  # BeautifulSoup 라이브러리를 통해 html 파싱
print(bs)

# tag = bs.select("ul.type01 li dl dt a._sp_each_title")[0]  # 뉴스 제목이 있는 태그 추출

# # 검색어 강조 해제
# for strong in tag.findAll("strong"):
#     strong.unwrap()

# href = tag["href"]  # 뉴스 링크
# title = "".join(tag.contents)  # 뉴스 제목
