# Alfie Ford - 120088076
#
# This is the main program for the project

#Import flask (webapp framework)
from flask import Flask, render_template, request

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
        if(request.args.get('uname') == None and (request.args.get('passwd')) == None):
            return render_template('index')
        elif(request.args.get('uname') == '' or request.args.get('passwd') == ''):
            return "<html><body> <h1>Check your username and password has been entered.</h1></body></html>"
        else:
            uname = request.args.get('uname')
            passwd = request.args.get('passwd')
            checkuserdetails()
            print(uname,passwd)
            return render_template("launchpad")
    return render_template('index')
    



#Start the server
if(__name__ == "__main__"):
	app.run(debug=True, port="8080")