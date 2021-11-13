import requests
import lxml.html as lh

def scrape(url):
  try:
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    el_list = doc.xpath('//*/p')
    response = ' '.join([x.text_content() for x in el_list]).replace('\n', ' ')
  except:
    response = ''
  return response