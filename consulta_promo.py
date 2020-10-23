import requests

class ConsultaPromo():
  def __init__(self):
    self._url = 'http://demosynthesis.cloudapp.net:58086/engine/evaluate'

  def consultar_promocao(self, xml):
    payload = {'request': xml}
    resp = {}
    resp = requests.get(self._url, params=payload)


    print(resp.text)

    
