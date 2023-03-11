from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')#, active_tab='home')

@app.route('/proyects')
def about():
    return render_template('proyects.html')#, active_tab='proyects')

if __name__ == '__main__':
    app.run(debug=True)
