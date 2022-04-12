import requests
from bs4 import BeautifulSoup


class opScrapper:
    def __init__(self,champ):
        # self.headers = {
        #    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 
        #    'Accept-Encoding': 'gzip, deflate', 
        #    'Accept': '*/*', 
        #    'Connection': 'keep-alive'

        # }
        self.req  = requests.get(f'https://u.gg/lol/champions/{champ}/build')
        self.soup = BeautifulSoup(self.req.text, 'html.parser')
    # scrape all Prio skills from u.gg 
    def findSkills(self):
        skillsPrio = self.soup.find('div',{
            'class': 'content-section_content skill-priority'
        })
        labels = skillsPrio.findAll('div',{
            'class': 'champion-skill-with-label'
        })
        output = []
        for l in labels:
            output.append(l.find('img')['src'])
        return output
    # scrape Rune from u.gg
    def findRunes(self):
        activeKeystones = self.soup.find('div',{
            'class': 'perk keystone perk-active'
        })
        activePerks = self.soup.findAll('div',{
            'class': 'perk perk-active'
        })
        output = []
        output.append(activeKeystones.find('img')['src'])
        for i in range(0, 5):
            output.append(activePerks[i].find('img')['src'])
        return output

# def test():
#     o = opScrapper('zoe')
#     print(o.findRunes())
# test()