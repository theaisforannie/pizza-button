from flask import Flask, render_template
app = Flask(__name__)

STATE = "ready"

@app.route('/')
def welcome():
    global STATE
    return render_template('pizza_form.html', state = STATE)

@app.route('/pizza_request', methods = ['POST'])
def request_pizza():
    global STATE
    STATE = "requested"
    # call to twilio goes here
    return render_template('pizza_form.html', state = STATE)

@app.route('/MomAuth_yes')
def ordered():
    global STATE
    STATE = "ordered"
    # order goes to dominos!
    return STATE 

@app.route('/MomAuth_no')
def rejected():
    global STATE
    STATE = "rejected"
    # womp womp
    return STATE

if __name__ == '__main__':
    app.debug = True
    app.run()
