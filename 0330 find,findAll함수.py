#fild, fidAll 함수
from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div class="menu">
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</div>
<div class="content">
    <h1>Hello, World!</h1>
    <p>This is an example of using Beautifulsoup.</p>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# find() 메서드 사용 예시
div_menu = soup.find('div', {'class': 'menu'})
print(div_menu.text)
links = div_menu.find_all('a')


# find_all() 메서드 사용 예시
#links = soup.find_all('a')
for link in links:
    #print(link.get('href')) #링크를 가져올 수 있다는 건 링크로 들어가서 또 웹크롤링 가
    print(link.text)
