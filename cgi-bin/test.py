#!C:\Python27\python.exe
"""
runs on the server, reads form input, prints HTML;
url=http://localhost/cgi-bin/test.py
"""
import cgi

form=cgi.FieldStorage()
print "Content-type: text/html"
output="""
<title>Answer</title>
<h1>Greeting</h1>
<hr>
<p>%s</p>
<hr>
"""
if not 'user' in form:
	print output % "What the fucking name you have??!!"
else:
	print output % ("Hello,%s" % form['user'].value)