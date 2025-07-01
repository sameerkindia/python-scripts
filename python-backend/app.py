from flask import Flask, render_template,request, redirect
import csv

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, Sameer!</p>"s


# @app.route("/")
# def home():
#     return render_template('index.html')


# @app.route("/about")
# def about():
#     return render_template('about.html')


# @app.route("/projects")
# def projects():
#     return render_template('projects.html')


# @app.route("/skills")
# def skills():
#     return render_template('skills.html')


# @app.route("/contact")
# def contact():
#     return render_template('contact.html')

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def render_page(page_name):
    return render_template(page_name + '.html')


def save_to_database(data):
    with open('database.txt', 'a') as database:
        name = data['name']
        email = data['email']
        msg = data['message']

        database.write(f'\n{name}, {email}, {msg}')


def save_to_csv(data):
    with open('database.csv', 'a', newline='') as database:
        name = data['name']
        email = data['email']
        msg = data['message']

        csv_writer = csv.writer(database,delimiter=',', quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,msg])
        # database.write(f'\n{name}, {email}, {msg}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        # save_to_database(data)
        save_to_csv(data)
        return redirect('/thankyou')
    else:
        return 'form submit nahi hua'