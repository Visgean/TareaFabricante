#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os

from flask import Flask, render_template, request, Response


app = Flask(__name__)
app.debug = False

@app.route('/', methods = ['GET', 'POST'])
def generator():
	if request.method == 'POST':
		filename = request.form["filename"] + request.form["extension"] 
		size = request.form["size"]
		
		try:
			size = int(float(size)*829*1293)
		except:
			size = 1000000
		
		data = os.urandom(size)
		response = Response(data, mimetype="application/octet-stream")
		response.headers.add('Content-Disposition', 'attachment',
                    		filename=filename)
		return response
	
	else:
		return render_template("base.html")

if __name__ == '__main__':
	app.run()