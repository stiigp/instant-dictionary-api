import justpy as jp
from api import Api
from documentation import Doc


jp.Route('/api', Api.serve)
jp.Route('/documentation', Doc.serve)
jp.justpy(port=8001)
