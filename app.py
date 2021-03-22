from flask import Flask, render_template

app = Flask('flaskwp1')
# webcode = open('webcode.html').read() - not needed

@app.route('/')
def webprint():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run()
