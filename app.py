from flask import Flask, render_template, json, request

app = Flask(__name__)


# Home Page
@app.route('/')
def main():
    return render_template("index.html")

#Go to home page
@app.route('/showHome')
def showHome():
    return render_template('/aichatbox/index.html')

# User - Sign Up Page ()
@app.route('/showSignUp')
def showSignUp():
    return render_template('/aichatbox/signup.html')

# User - Sign In Page ()
@app.route('/showSignIn')
def showLogIn():
    return render_template('/aichatbox/signIn.html')


# User - Manage Bot (1)
@app.route('/showManageBot')
def showManageBot():
    return render_template('/01aichatboxadmin/index3.html')

# User - Manage Bot (3)
@app.route('/showAnswerQuestion')
def showAnswerQuestion():
    return render_template('/03aichatbotUI/index.html')
    # return render_template('/aichatbox/answerQuestion.html')



















@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run(port=5000, host='203.250.77.79')
    # app.run(port=5002, host='192.168.1.131')
