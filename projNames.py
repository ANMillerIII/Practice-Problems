from bs4 import BeautifulSoup
import re

class Parser:
    def parseSite(self):
        projectNames = []
        with open('MAPS.html') as a:
            soup = BeautifulSoup(a, 'html.parser')
            lines = soup.findAll('td', text=re.compile('^[A-Z]'))
            projectNames = []
            for projectName in lines:
                projectName = str(projectName)
                helper = projectName.replace('<td>', '').replace('</td>', '')
                projectNames.append(projectName)
            return print(projectNames)

if __name__=="__main__":
    Parser.parseSite(None)