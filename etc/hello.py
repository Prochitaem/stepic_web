# -*- coding: UTF-8 -*-
def app(environ, start_response):
      ##data = b"Hello, World!\n"
      query = environ['QUERY_STRING']
      data = query.split('&')
      for i in range(len(data)):
          data[i] += chr(13)
      start_response("200 OK", [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(len(data)))
      ])
      return iter([data])