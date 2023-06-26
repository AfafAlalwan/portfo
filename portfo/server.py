
from flask import Flask, render_template, request, make_response
import csv
import credentials
import smtplib
from email.message import EmailMessage

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

def send_email(data):
    try:        
        email = EmailMessage()
        email['from'] = data['name']
        email['to'] = credentials.email_receiver
        email['subject'] = data['subject']
        message = data['message']
        contact_email = data['email']
        email.set_content(f'{message}\n contact email: {contact_email}')
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls() 
            smtp.login(credentials.email_sender, credentials.password)
            smtp.send_message(email)
    except:
        return render_template('sth_wrong.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            send_email(data)
            return render_template('thank_you.html')
        except:
            return render_template('sth_wrong.html')
    else:
        return render_template('sth_wrong.html')
    
@app.route('/get_cv', methods=['POST', 'GET'])
def get_cv():
    if request.method == 'GET':
        try:
            response = make_response(open('static\pdf\CV-Afaf-Alalwan.pdf', 'rb').read())
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'attachment; filename=CV-AfafAlalwan.pdf'

            return response
        except:
            return render_template('sth_wrong.html')
    else:
        return render_template('sth_wrong.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(page_name)


if __name__ == '__main__':
    app.run(debug=True) 

