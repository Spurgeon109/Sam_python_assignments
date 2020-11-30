from flask import Flask
from flask import request
import bcrypt
import json
import smtplib
import random
import re


otp = ""
email = ""
h_pass = ""

def check(s):
   if not re.search('[A-Z]', s):
       print("Please mention atleast one Upper Case")
       return False
   elif not re.search('[a-z]', s):
       print("Please mention atleast one Lower Case")
       return False
   elif not re.search('[0-9]', s):
       print("Please mention atleast one digit")
       return False
   elif not re.search('[!@#$%^&*]', s):
       print("Please mention atleast one special character")
       return False
   elif  len(s) < 8:
       print("Password should be atleast 8 characters") 
   else: return True


def check_email(s):
    return re.match('[a-z.0-9]{3,}@[a-z]{2,}\.(com|in)', s)


def otpgen():
    s = ""
    for i in range(0, 7):
        s+= str(random.randint(0, 9))
    return s


def send(rec, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    pas = open('E:\pre-intern-training\python_trn\pwd.txt').read()
    s.login('yacobtalla@gmail.com', pas)
    s.sendmail('yacobtalla@gmail.com', rec, msg)
    s.quit()


app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hello</h1>
    <p>Click <a href="http://127.0.0.1:5000/auth">Here</a> this link to sign up or sign in page</p>
    '''

@app.route('/auth')
def auth():
    return '''    
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <title>Login Page</title>
      <style>
         /* Basics */
         html, body {
         width: 100%;
         height: 100%;
         font-family: "Helvetica Neue", Helvetica, sans-serif;
         color: #444;
         -webkit-font-smoothing: antialiased;
         background: #f0f0f0;
         }
         #container {
         position: fixed;
         width: 340px;
         height: 280px;
         top: 50%;
         left: 50%;
         margin-top: -140px;
         margin-left: -170px;
         background: #fff;
         border-radius: 3px;
         border: 1px solid #ccc;
         box-shadow: 0 1px 2px rgba(0, 0, 0, .1);
         }
         form {
         margin: 0 auto;
         margin-top: 20px;
         }
         label {
         color: #555;
         display: inline-block;
         margin-left: 18px;
         padding-top: 10px;
         font-size: 14px;
         }
         p a {
         font-size: 11px;
         color: #aaa;
         float: right;
         margin-top: -13px;
         margin-right: 20px;
         -webkit-transition: all .4s ease;
         -moz-transition: all .4s ease;
         transition: all .4s ease;
         }
         p a:hover {
         color: #555;
         }
         input {
         font-family: "Helvetica Neue", Helvetica, sans-serif;
         font-size: 12px;
         outline: none;
         }
         input[type=text],
         input[type=password] ,input[type=time]{
         color: #777;
         padding-left: 10px;
         margin: 10px;
         margin-top: 12px;
         margin-left: 18px;
         width: 290px;
         height: 35px;
         border: 1px solid #c7d0d2;
         border-radius: 2px;
         box-shadow: inset 0 1.5px 3px rgba(190, 190, 190, .4), 0 0 0 5px #f5f7f8;
         -webkit-transition: all .4s ease;
         -moz-transition: all .4s ease;
         transition: all .4s ease;
         }
         input[type=text]:hover,
         input[type=password]:hover,input[type=time]:hover {
         border: 1px solid #b6bfc0;
         box-shadow: inset 0 1.5px 3px rgba(190, 190, 190, .7), 0 0 0 5px #f5f7f8;
         }
         input[type=text]:focus,
         input[type=password]:focus,input[type=time]:focus {
         border: 1px solid #a8c9e4;
         box-shadow: inset 0 1.5px 3px rgba(190, 190, 190, .4), 0 0 0 5px #e6f2f9;
         }
         #lower {
         background: #ecf2f5;
         width: 100%;
         height: 69px;
         margin-top: 20px;
         box-shadow: inset 0 1px 1px #fff;
         border-top: 1px solid #ccc;
         border-bottom-right-radius: 3px;
         border-bottom-left-radius: 3px;
         }
         input[type=checkbox] {
         margin-left: 20px;
         margin-top: 30px;
         }
         .check {
         margin-left: 3px;
         font-size: 11px;
         color: #444;
         text-shadow: 0 1px 0 #fff;
         }
         input[type=submit] {
         float: right;
         margin-right: 20px;
         margin-top: 20px;
         width: 80px;
         height: 30px;
         font-size: 14px;
         font-weight: bold;
         color: #fff;
         background-color: #acd6ef; /*IE fallback*/
         background-image: -webkit-gradient(linear, left top, left bottom, from(#acd6ef), to(#6ec2e8));
         background-image: -moz-linear-gradient(top left 90deg, #acd6ef 0%, #6ec2e8 100%);
         background-image: linear-gradient(top left 90deg, #acd6ef 0%, #6ec2e8 100%);
         border-radius: 30px;
         border: 1px solid #66add6;
         box-shadow: 0 1px 2px rgba(0, 0, 0, .3), inset 0 1px 0 rgba(255, 255, 255, .5);
         cursor: pointer;
         }
         input[type=submit]:hover {
         background-image: -webkit-gradient(linear, left top, left bottom, from(#b6e2ff), to(#6ec2e8));
         background-image: -moz-linear-gradient(top left 90deg, #b6e2ff 0%, #6ec2e8 100%);
         background-image: linear-gradient(top left 90deg, #b6e2ff 0%, #6ec2e8 100%);
         }
         input[type=submit]:active {
         background-image: -webkit-gradient(linear, left top, left bottom, from(#6ec2e8), to(#b6e2ff));
         background-image: -moz-linear-gradient(top left 90deg, #6ec2e8 0%, #b6e2ff 100%);
         background-image: linear-gradient(top left 90deg, #6ec2e8 0%, #b6e2ff 100%);
         }
      </style>
   </head>
   <body>
      <!-- Begin Page Content -->
      <h1>To sign up please click the signup button and ignore the rest</h1>
      <div id="container">
         <form action="/authenticate" method="post">
            <label for="loginmsg" style="color:hsla(0,100%,50%,0.5); font-family:"Helvetica Neue",Helvetica,sans-serif;"></label>
            <label for="username">Username:</label>
            <input type="text" id="username" name="user_id">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password">
            <input type="submit" value="SignIn" name = "In">
            <input type="submit" value="SignUp" name = "Up">
         </form>
      </div>
      <!--/ container-->
      <!-- End Page Content -->
   </body>
</html>'''


@app.route('/authenticate', methods = ['POST', 'GET'])
def authen():
    d =  request.form.to_dict()
    if d.__contains__("Up") :
        return '''
        <head>
          <style>
          #container {
         position: fixed;
         width: 340px;
         height: 280px;
         top: 50%;
         left: 50%;
         margin-top: -140px;
         margin-left: -170px;
         background: #fff;
         border-radius: 3px;
         border: 1px solid #ccc;
         box-shadow: 0 1px 2px rgba(0, 0, 0, .1);
         }
          </style>
        </head>
        <div id="container" >
        <form action = "/signup" method="Post">
        <label for="loginmsg" style="color:hsla(0,100%,50%,0.5); font-family:"Helvetica Neue",Helvetica,sans-serif;"></label>
        <label for="First Name">First Name:</label>
        <input type = "text" id="fname" name="fname"><br>
        <label for="Last Name">Last Name:</label>
        <input type = "text" id="lname" name="lname"><br>
        <label for="User Name">User Name:</label>
        <input type = "text" id="uname" name="uname"><br>
        <label for="Email Id">Email Id:</label>
        <input type = "text" id="em" name="email"><br>
        <label for="Password">Password:</label>
        <input type = "password" id="ps" name="pass"><br>
        <input type = "submit" name="submit" value="submit">
        </form>
        </div>
        '''
    else:
        global email, h_pass
        email, h_pass = request.form['user_id'], request.form['password']
        f = open(r'E:\pre-intern-training\python_trn\Flask\user_pass.txt', 'r').readlines()
        for i in f:
            arr = i.split(" ")
            if arr[0] == email:
                if bcrypt.checkpw(h_pass.encode("utf8"), arr[1].encode("utf8")):
                    return "<h1>Successful Sign In</h1>"
                else:
                    return "<h1>Enter Correct Password</h1>"
            else:
                return "<h1>Invalid Password</h1>"
            
        
        


@app.route('/signup', methods = ['POST'])
def signup():
    global email, h_pass
    email, h_pass = request.form['email'], bcrypt.hashpw(request.form['pass'].encode("utf8"), bcrypt.gensalt())
    if check(request.form['pass']) and check_email(email):
      global otp
      msg = otpgen()
      otp = msg
      rec = request.form['email']
      send(rec, msg)
      return '''
             <form action="/val-otp" method="post">
             An OTP has been sent to your email. Please enter it.
             <input type = "text" id="otp" name="otp">
             <input type = "submit" value="submit otp" name="sotp">
             </form>
             '''
    else:
        return "<h1>Choose a strong password or enter a invalid email</h1>"

@app.route('/val-otp', methods = ['POST'])
def valotp():
    if otp == request.form['otp']:
        f = open('user_pass.txt', 'a+', newline='\n')
        f.seek(len(f.read()))
        if f.tell() == 0:
            f.write(email+" ")
            f.write(h_pass.decode())
            f.write('\n')
            f.close()
        else:
            f.write(email+" ")
            f.write(h_pass.decode())
            f.write('\n')
            f.close()
        return "<h1> Your account has been Successfully created</h1>"
    else:
         return "<h1>SignUp Failed</h1>"
    
        

if __name__ == "__main__":
    app.run()