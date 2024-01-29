# Alfie Ford - 120088076
#
# This is the main program for the project which handles the serving of the web-app
# It calls the other function which are stored in seperate files for ease of development and maintainance.

#Import flask (webapp framework)
from flask import Flask, render_template, request, current_app, redirect, url_for

#Import the other modules from other files in the project
import ciphers
import userauth as uauth

#Global
accntname = ""
accntpoints = ""

#Create a flask instance
app = Flask(__name__)


#Setup the page first seen when you access [localhost:8080/] on my machine
#This is the login page for the app.
@app.route('/', methods=['POST','GET'])
def login():
    #Check if the user has submitted the login page form
    if request.method == 'GET':
        #return the page
        if request.args.get('uname') == None and request.args.get('passwd') == None:
            return render_template('index.html')
        #If one field is empty out of the two return the page asking for the correct details
        elif request.args.get('uname') == '' or request.args.get('passwd') == '':
            errormess = "Please fill in both fields"
            return render_template('index.html',error=errormess)
        #Otherwise collect the username and password from the form and check it.
        else:
            #Read in the username and password from the form.
            uname = request.args.get('uname')
            passwd = request.args.get('passwd')
            #Send the details to the function in [userauth.py] for checking
            global accntname,accntpoints,challcode
            res,accntname,accntpoints = uauth.checkuserdetails(uname,passwd)
            print(res,accntname) #Debug
            #If the function comes bath as authorised redirect the user to [launchpad.html]
            if res == "AUTHORISED":
                #return render_template("launchpad.html",name=accountname, points=accntpoints)
                return redirect("/launchpad")
            #If the password is incorrect tell the user and ask them to re-enter their details
            elif res == "INC-PASSWD":
                errormess = "Incorrect Password - Try Again"
                return render_template("index.html",error=errormess)
            #Otherwise tell the user the details supplied were incorrect and get them to do it again.
            else:
                errormess = "Incorrect Details - Try Again"
                return render_template("index.html",error=errormess)
    return render_template("index.html")
@app.route('/launchpad', methods=["GET"])
def launchpad():
    if request.method == "GET":
        return render_template("launchpad.html",name=accntname,points=accntpoints)

@app.route('/caesercipher',methods=["GET"])
def caesercipher():
    correctanswer = ""
    challcode = ""
    challcode,correctanswer = ciphers.caesarcipher()
    if request.method == "GET":
        if request.args.get('answerattempt') == None: #If the answer field is empty render the page
            return render_template("caeser.html",name=accntname,points=accntpoints,code=challcode)
        else:
            attemptanswer = request.args.get('answerattempt')
            if attemptanswer == correctanswer:
                return render_template("launchpad.html",name=accntname,points=accntpoints)
            else:
                return render_template("caeser.html",name=accntname,points=accntpoints,code=challcode)

@app.route('/movingkeycipher',methods=["GET"])
def movingkeycipher():
    return render_template("movingkey.html",name=accntname,points=accntpoints)

@app.route('/superenciphercipher',methods=["GET"])
def superenciphercipher():
    return render_template("superencipher.html",name=accntname,points=accntpoints)


#This is a quirk of flask that you have to setup each file as a seperate webpage and is only included to make the html see the css and images etc.
#Setup the background image
@app.route('/background')
def background():
    return current_app.send_static_file('background.png')
#Setup the style.css file for the html pages.
@app.route('/style.css')
def css():
    return current_app.send_static_file('style.css')
@app.route('/script.js')
def script():
    return current_app.send_static_file('script.js')
#Favicon for the site
@app.route('/favicon')
def faviconico():
    return current_app.send_static_file('favicon.png')
#Caeser Encode Img for tutorial
@app.route('/caeserencodeimg')
def caeserencodeimg():
    return current_app.send_static_file('caeserencode.png')

#Start the server on port 8080 of my local machine
if(__name__ == "__main__"):
	app.run(debug=True, port="8080")