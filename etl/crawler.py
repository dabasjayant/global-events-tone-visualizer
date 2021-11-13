import requests
import lxml.html as lh

def scrape(url):
  try:
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    el_list = doc.xpath('//*/p')
    response = ' '.join([x.text_content() for x in el_list])
    response = response.decode('utf-8').replace('\t', ' ').replace('\n', ' ').replace('\r', '')
    response = ' '.join(response.split())
    response = response[:5000] if len(response) > 5000 else response
  except:
    response = ''
  return response