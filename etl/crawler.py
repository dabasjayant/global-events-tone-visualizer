import requests
import lxml.html as lh

def scrape(url):
  page = requests.get(url)
  if not page.content == '':
    doc = lh.fromstring(page.content)
    el_list = doc.xpath('//*/p')
    response = ' '.join([x.text_content() for x in el_list])
  else:
    response = ''
  return response