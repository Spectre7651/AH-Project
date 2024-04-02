# Alfie Ford - 120088076
#
# This is the main program for the project which handles the serving of the web-app
# It calls the other functions which are stored in seperate files for ease of development and maintainance.

#Import flask (webapp framework)
from flask import Flask, render_template, request, current_app, redirect, url_for

#Import the other modules from other files in the project
import ciphers
import usermanagement as uman

#Global variables so they can be accessed in every function without passing them in.
global accntname,accntpoints,challcode,auname
accntname = ""
accntpoints = ""
challcode = ""
auname = ""

#Create a flask instance called app
app = Flask(__name__)


#Setup the page first seen when you access [localhost:8080/] on my machine
#This is the login page for the app.
@app.route('/', methods=['POST','GET'])
def login():
    #Check if the user has submitted the login page form
    if request.method == 'POST':
        #return the page
        if request.form['uname'] == None and request.form['passwd'] == None:
            return render_template('index.html')
        #If one field is empty out of the two return the page asking for the correct details
        elif request.form['uname'] == '' or request.form['passwd'] == '':
            errormess = "Please fill in both fields"
            return render_template('index.html',error=errormess)
        #Otherwise collect the username and password from the form and check it.
        else:
            #Read in the username and password from the form.
            uname = request.form['uname']
            passwd = request.form['passwd']
            #Send the details to the function in [userauth.py] for checking
            global accntname,accntpoints,challcode,auname
            res,accntname,accntpoints,auname = uman.checkuserdetails(uname,passwd)

            #Debug
            print(res,accntname)
            print("£££££",auname) 

            #If the function comes back as authorised redirect the user to [launchpad.html]
            if res == "AUTHORISED":
                return redirect("/launchpad")
            #If the password is incorrect tell the user and ask them to re-enter their details
            elif res == "INC-PASSWD":
                errormess = "Incorrect Password - Try Again"
                return render_template("index.html",error=errormess)
            #Otherwise tell the user the details supplied were incorrect and get them to do it again.
            else:
                errormess = "Account Not Found - Try Again"
                return render_template("index.html",error=errormess)
    return render_template("index.html")

#This is the page that will be loaded after a successful login
@app.route('/launchpad', methods=["GET"])
def launchpad():
    if request.method == "GET":
        position = uman.leaderboard(auname)
        return render_template("launchpad.html",name=accntname,points=uman.getpoints(auname),leaderboardmessage=position)

#This is the code for the Caesar cipher challenge page 
@app.route('/caesarcipher',methods=["GET"])
def caesarcipher():
    #This sets up and grabs the code to be broken and the correct answer from [ciphers.py]
    correctanswer = ""
    challcode = ""
    challcode,correctanswer = ciphers.Caesarcipher()
    if request.method == "GET":
        #This checks is the answer field is empty and if so renders the whole page with the tutorial first
        if request.args.get('answerattempt') == None:
            return render_template("caesar.html",name=accntname,points=uman.getpoints(auname),code=challcode, error="")

        #Otherwise the answer field has been filled in so we need to check if the answer is correct
        else:
            attemptanswer = request.args.get('answerattempt')
            #If the answer is correct then redirect to the [win.html] page and fill in the info needed
            if str(attemptanswer).upper() == str(correctanswer):
                print(f"Correct Answer for Caesar Cipher {attemptanswer}")
                #Add 1000 points to the users account
                uman.addpoints(auname,1000)
                return render_template("win.html",name=accntname,points=uman.getpoints(auname),challengename="Caesar Cipher",challengepoints="1000")
            #Otherwise the answer is incorrect so the page is reloaded and auto hides the tutorial for the user
            else:
                #Debug
                print(f"Incorrect Answer for Caesar Cipher {attemptanswer}")
                
                errormess = "Incorrect Try Again"
                return render_template("caesar.html",name=accntname,points=uman.getpoints(auname),code=challcode,error="True",errormess=errormess)

@app.route('/movingkeycipher',methods=["GET"])
def movingkeycipher():
    #This is the same structure as the Caesar cipher but with the different challenge code and page
    correctanswer = ""
    challcode = ""
    challcode,correctanswer = ciphers.movingkeycipher()
    if request.method == "GET":
        if request.args.get('answerattempt') == None:
            return render_template("movingkey.html",name=accntname,points=uman.getpoints(auname),code=challcode, error="")
        else:
            attemptanswer = request.args.get('answerattempt')
            if str(attemptanswer).upper() == str(correctanswer):
                print(f"Correct Answer for Moving Key Cipher {attemptanswer}")
                uman.addpoints(auname,2500)
                return render_template("win.html",name=accntname,points=uman.getpoints(auname),challengename="Moving Key Cipher",challengepoints="2500")
            else:
                print(f"Incorrect Answer for Moving Key Cipher {attemptanswer}")
                errormess = "Incorrect Try Again"
                return render_template("movingkey.html",name=accntname,points=uman.getpoints(auname),code=challcode,error="True",errormess=errormess)


@app.route('/superenciphercipher',methods=["GET"])
def superenciphercipher():
    #This sets up and grabs the code to be broken and the correct answer from [ciphers.py]
    correctanswer = ""
    challcode = ""
    challcode,correctanswer = ciphers.superencipherment()
    if request.method == "GET":
        #This checks is the answer field is empty and if so renders the whole page with the tutorial first
        if request.args.get('answerattempt') == None:
            return render_template("superencipher.html",name=accntname,points=uman.getpoints(auname),code=challcode, error="")
        #Otherwise the answer field has been filled in so we need to check if the answer is correct
        else:
            attemptanswer = request.args.get('answerattempt')
            #If the answer is correct then redirect to the [win.html] page and fill in the info needed
            if str(attemptanswer).upper() == str(correctanswer):
                print(f"Correct Answer for SuperEncipherment Cipher {attemptanswer}")
                #Add 1000 points to the users account
                uman.addpoints(auname,1000)
                return render_template("win.html",name=accntname,points=uman.getpoints(auname),challengename="Caesar Cipher",challengepoints="1000")
            #Otherwise the answer is incorrect so the page is reloaded and auto hides the tutorial for the user
            else:
                #Debug
                print(f"Incorrect Answer for SuperEncipherment Cipher {attemptanswer}")

                errormess = "Incorrect Try Again"
                return render_template("superencipher.html",name=accntname,points=uman.getpoints(auname),code=challcode,error="True",errormess=errormess)



#This is a quirk of flask that you have to setup each file as a seperate webpage and is only included to make the html see the css and images etc.

#Setup the background image
@app.route('/background')
def background():
    return current_app.send_static_file('background.png')

#Setup the style.css file for the html pages.
@app.route('/style.css')
def css():
    return current_app.send_static_file('style.css')

#Setup the script.js file for javascript access
@app.route('/script.js')
def script():
    return current_app.send_static_file('script.js')

#Favicon for the site
@app.route('/favicon')
def faviconico():
    return current_app.send_static_file('favicon.png')

#Caesar Encode Img for tutorial
@app.route('/caesarencodeimg')
def caesarencodeimg():
    return current_app.send_static_file('caesarencode.png')

#The Image for the launchpad caesar section
@app.route('/caesarwheelimg')
def caesarwheelimg():
    return current_app.send_static_file('caesarwheel.png')

#The image for the moving key launchpad
@app.route('/movingkeyimg')
def movingkeyimg():
    return current_app.send_static_file('enigma.jpg')

#The note I made to give the crib to the user
@app.route('/cribnote')
def cribnote():
    return current_app.send_static_file('cribnote.png')

#Start the server on port 8080 of my local machine when app.py is ran
if(__name__ == "__main__"):
	app.run(debug=True, port="8080")
