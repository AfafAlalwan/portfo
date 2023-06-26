
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database,delimiter=',',quotechar=';',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('thank_you.html')
        except:
            return render_template('sth_wrong.html')
    else:
        return render_template('sth_wrong.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(page_name)


if __name__ == '__main__':
    app.run(debug=True) 

