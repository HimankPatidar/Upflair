from flask import Flask, render_template, url_for,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('sign.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/userdata')
def userdata():
    return render_template('userdata.html')

@app.route('/submitdata', methods=['GET','POST'])
def submitdata():   
    if request.method == "POST" :
        profession = request.form['profession'] 
        name = request.form['name'] 
        email = request.form['email'] 
        password = request.form['password'] 
        my_data = {
            "user_profession" : profession,
            "user_name" : name,
            "user_email" : email,
            "user_password" : password
        }
        return my_data
        # return render_template('submitdata.html', my_data=my_data)
if __name__ == '__main__':
    app.run(debug=True)
