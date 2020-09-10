import requests
from bs4 import BeautifulSoup

query = "안녕"  # 검색어
index = 1  # 페이지 인덱스

url = f"https://search.naver.com/search.naver?&where=news&query={query}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=27&start={(index - 1)*10 + 1}"
response = requests.get(url).text

# BeautifulSoup 라이브러리를 통해 html 파싱
newsHTML = BeautifulSoup(response, "html.parser")

# 뉴스 제목이 있는 태그 추출
tags = newsHTML.select(
    "ul.type01 li dl dt a._sp_each_title")

uselessAttrs = ["class", "onclick", "title"]

for tag in tags:
    # 깔끔한 태그 위한 속성 제거
    for uselessAttr in uselessAttrs:
        del tag[uselessAttr]

    # 검색어 키워드 강조 해제
    for strong in tag.findAll("strong"):
        strong.unwrap()

fileName = "index.html"

# 기본 html 파일 생성
with open(fileName, "w") as file:
    file.write("""<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Baero</title>
  </head>
  <body></body>
</html>
""")


with open(fileName, "r+") as file:
    baseHTML = BeautifulSoup(file.read(), "html.parser")

    for idx, tag in enumerate(tags):
        p = baseHTML.new_tag("p", id=idx + 1)
        p.append(tag)
        baseHTML.body.append(p)

    file.seek(0)
    file.write(baseHTML.prettify())
    file.truncate()
