import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
           if (page>0):
                      print("Hi!!!!!!!!")
                      url=WebUrl
                      code=requests.get(url)
                      plain=code.text
                      s=BeautifulSoup(plain,"html.parser")
                      #for link in s.findAll('a',{'class':'removeBefore'}):
                      for link in s.findAll('a'):
                                 tet_2=link.get('href')
                                 print(tet_2)
web(1,'https://www.shein.in/promodiscount.html?url_from=ingoogle brandshein_shein05_20190122&gclid=EAIaIQobChMIpteLgIyz4AIVECQrCh29GwEpEAAYASAAEgLrMfD_BwE')


