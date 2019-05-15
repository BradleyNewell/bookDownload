from urllib.request import urlopen
from bs4 import BeautifulSoup
import io


# To download a different book you can change the string below to your desired book
html = urlopen("https://www.gutenberg.org/files/2600/2600-0.txt")
bs = BeautifulSoup(html.read(), "html.parser")
text = bs.get_text
text = str(text)
# Changing the name of "WarandPeace.txt" will change the name of the file you wish to save the book as.
with io.open("WarandPeace.txt", mode="w", encoding="utf-8") as file:
    file.write(text)
file.close()
