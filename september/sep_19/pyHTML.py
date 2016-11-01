#!/usr/bin/python --> SHBANG!
print 'Content-TypeL text/html\n\n' --> for html
print ''

import cgi

#for developmental purposes:
#import cgitb
#cgitb.enable()

HTML_HEADER = """
  <!DOCTYPE html>
  <html>
  <head><title> TITLE HERE </title></head>
  <body>
"""

HTML_FOOTER = """
  </body>
  </html>
"""
