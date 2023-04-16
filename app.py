import os
import shutil as sl
from flask import *
import random
from flask import request
import datetime as dt
import smtplib
import os
from flask import render_template

app = Flask(__name__, static_folder="files", template_folder=os.getcwd())

#Creating function to send OTP to mail
def mail(arg1,arg):
	av=smtplib.SMTP_SSL("smtp.domain.com",port)
	av.login("youremail@domain.com","password")
	try:
		av.sendmail("yourmail@domain.com",arg1,arg)
		return "Y"
	except:
		return "X"

@app.route("/",methods=["GET","POST"])
def m():
	if (request.method=="POST"):
		name= str(dt.datetime.now()).replace(":","").replace("-","").replace(".","").replace(" ","")
		#Getting random value for OTP
		otp= random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])+random.choice(["a","b","c","d","e","f","g","9","8","5","3"])
		os.mkdir("acc/"+name)
		open("acc/"+name+"/otp","w+").write(otp)
		open("acc/"+name+"/mail","w+").write(request.form["email"].replace(" ",""))
		open("acc/"+name+"/1","a").write("")
		d= mail(request.form["email"].replace(" ",""),("Subject:OTP verification\nSeems like you have created your form in U KNOW ME\nYour OTP - "+otp))
		if (d == "X"):
			return render_template("index.html", msg="Enter valid email ID")
		return render_template("otp.html", fcontent=name)
	else:
		return render_template("index.html", msg="none")

@app.route("/otp",methods=["POST"])
def m_2():
	#Verifying OTP and creating webpage
	if (request.form["otp"] == r("acc/"+request.form["name"]+"/otp")):
		return render_template("create.html", dfdfd="127.0.0.1:5000/"+request.form["name"])
	else:
		sl.rmtree("acc/"+request.form["name"])
		return render_template("index.html",msg="Wrong OTP, try again")

@app.route("/<n>",methods=["GET","POST"])
def m_1(n):
	if (request.method=="GET"):
		#Checking is user exists
		if (n in os.listdir("acc")):
			return render_template("survey.html", username=n)
		else:
			return render_template("404.html")
	else:
		mail(r("acc/"+request.form["user"]+"/mail"),("Subject:Response from your friend\n\nName:"+request.form["nameof"]+"\nWhich is your favourite animal? - "+request.form["df1"]+"\nWhat would you like to have with me , when we will meet? - "+request.form["df2"]+"\nWhat will you check, if I will give my mobile to u? - "+request.form["df3"]+"\nDefine me in one word - "+request.form["df4"]+"\nWhere will we go , if we get a chance for trip? - "+request.form["df5"]+"\n\nHope you are enjoying our service!!"))
		return render_template("submit.html")

if "__main__" == __name__:
	app.run()
