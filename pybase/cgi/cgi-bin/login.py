#! /usr/bin/python3


import cgi
import json

reshtml="""content-type:application/json\n\n
%s"""

form = cgi.FieldStorage()
userName = form.getvalue('userName')
pwd = form.getvalue('pwd')

result = {'login':'faild'}

if userName == 'wang' and pwd == '123456':
    result['login'] = 'ok'


print(reshtml % json.dumps(result))

