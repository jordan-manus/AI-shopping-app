from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' %name


@app.route('/login', methods=['POST', 'GET'])
def login():
    # call database to verify if user is present

    #if not present in DB, redirect to register account

    #else return valid token and redirect to homepage



# allows the user to register a brand new account
@app.route('/register', methods=['POST'])
def register():
    pass


# allows the user to create/edit their initial questionnaire 
@app.route('/questionnaire', methods=['POST', 'PUT'])
def questionnaire():
    pass


# allows the user to create and retrieve items from DB
@app.route('/items', methods=['POST', 'GET'])
def items():
    pass


if __name__ == '__main__':
    app.run(debug=True)