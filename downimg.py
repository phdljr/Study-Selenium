from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

for num in range(1, 2):
    url = f"https://tr.hangame.com/guide/characterinfo.asp?num={num}&ctype=0"
    html = urlopen(url)
    soup = bs(html, "html.parser")
    print(soup)


# characters = ["chowon", "bigbo"]

# for character in characters:
#     url = f"https://tr-image.game.onstove.com/webapp/pc/character/assets/images/character/{character}/img_character.png"

#     with urlopen(url) as f:
#         with open('./images/' + character + '.jpg', 'wb') as h:
#             img = f.read()
#             h.write(img)