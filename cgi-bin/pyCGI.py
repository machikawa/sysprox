#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import sys
import io
 
if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    print('Content-Type: text/html; charset=UTF-8\n')
    html_body = """
    <!DOCTYPE html> 
    <html>
        <head>
        </haed>
        <body>
        <h1>Your input is "%s"</h1>
        </body>
    </html>
    """
 
    form = cgi.FieldStorage()
    text = form.getvalue('text', '')
 
    print(html_body % (text))
