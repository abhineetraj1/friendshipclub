import os
import shutil as sl
from flask import *
import random
from flask import request
import datetime as dt
import smtplib

app = Flask(__name__, static_folder="files")

def mail(arg1,arg):
	av=smtplib.SMTP_SSL("smtp.domain.com",port)
	av.login("youremail@domain.com","password")
	try:
		av.sendmail("friendship.club.response@gmail.com",arg1,arg)
		return "Y"
	except:
		return "X"
def web_mg(a):
	return "<script>alert('"+a+"');</script>"
def r(a):
	return open(a,"r+").read()
@app.route("/",methods=["GET","POST"])
def m():
	if (request.method=="POST"):
		name= str(dt.datetime.now()).replace(":","").replace("-","").replace(".","").replace(" ","")
		otp= random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])
		os.mkdir("acc/"+name)
		open("acc/"+name+"/otp","w+").write(otp)
		open("acc/"+name+"/mail","w+").write(request.form["email"].replace(" ",""))
		open("acc/"+name+"/1","a").write("")
		d= mail(request.form["email"].replace(" ",""),("Subject:OTP verification\nSeems like you have created your form in U KNOW ME\nYour OTP - "+otp))
		if (d == "X"):
			return "<script>alert('Enter valid email ID');</script>"+r("index.html")
		return r("otp.html").replace("f-content",name)
	else:
		return r("index.html")

@app.route("/otp",methods=["GET","POST"])
def m_2():
	if (request.method=="POST"):
		if (request.form["otp"] == r("acc/"+request.form["name"]+"/otp")):
			return r("create.html").replace("dfdfdf","127.0.0.1:5000/"+request.form["name"])
		else:
			sl.rmtree("acc/"+request.form["name"])
			return "<script>alert('Wrong otp. Try again');</script>"+r("index.html")
	else:
		return ""

@app.route("/<n>",methods=["GET","POST"])
def m_1(n):
	if (request.method=="GET"):
		if (n in os.listdir("acc")):
			return r("survey.html")+"<script>localStorage.setItem('username','"+n+"');</script>"
		else:
			return r("404.html")
	else:
		mail(r("acc/"+request.form["user"]+"/mail"),("Subject:Response from your friend\n\nName:"+request.form["nameof"]+"\nWhich is your favourite animal? - "+request.form["df1"]+"\nWhat would you like to have with me , when we will meet? - "+request.form["df2"]+"\nWhat will you check, if I will give my mobile to u? - "+request.form["df3"]+"\nDefine me in one word - "+request.form["df4"]+"\nWhere will we go , if we get a chance for trip? - "+request.form["df5"]+"\n\nHope you are enjoying our service!!"))
		return r("submit.html")

if "__main__" == __name__:
	app.run()
