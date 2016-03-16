# -*- coding: UTF-8 -*-
from urlparse import urlparse
def app(environ, start_response):
      ##data = b"Hello, World!\n"
      query = environ['QUERY_STRING']
      data = query.split('&')
      start_response("200 OK", [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(len(data)))
      ])
      return iter([data])