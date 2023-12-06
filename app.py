# Alfie Ford - 120088076
#
# This is the main program for the project

#Import flask (webapp framework)
from flask import Flask, render_template, request, current_app

#Import the other modules from other files
import ciphers
import userauth as uauth

#Create a flask instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    #render_template('index.html')
    #Check if the user has submitted the login page form
    if request.method == 'GET':
        if request.args.get('uname') == None and request.args.get('passwd') == None:
            return render_template('index.html')
        elif request.args.get('uname') == '' or request.args.get('passwd') == '':
            return render_template('index.html')
        else:
            uname = request.args.get('uname')
            passwd = request.args.get('passwd')
            res,accountname = uauth.checkuserdetails(uname,passwd)
            print(res,accountname)
            if res == "AUTHORISED":
                return render_template("launchpad.html",name=accountname)
            elif res == "INC-PASSWD":
                errormess = "Incorrect Password - Try Again"
                return render_template("index.html",error=errormess)
            else:
                errormess = "Incorrect Details - Try Again"
                return render_template("index.html",error=errormess)
            
    return render_template('index.html')
#This serves the css and images from the static folder
@app.route('/background')
def background():
    return current_app.send_static_file('background.png')
@app.route('/style.css')
def css():
    return current_app.send_static_file('style.css')


#Start the server
if(__name__ == "__main__"):
	app.run(debug=True, port="8080")