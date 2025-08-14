from flask import Flask, render_template,request

#Create a Flask application
app = Flask(__name__)

#Define a route for the root URL
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        
        return f'''
            <h1>Form Submitted Successfully!</h1>
            <p>First Name: {fname}</p>
            <p>Last Name: {lname}</p>
        '''
    return render_template('home.html', message='Login')

#Run the application
if __name__ == '__main__':
    app.run(debug=True)