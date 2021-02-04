from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			contact_data = request.form.to_dict()
			edit_contact_csv(contact_data)
			return redirect('./thankyou.html')
		except:
			return 'Could not save to database.'
	else:
		return 'Something went wrong. Try again!'


def edit_contact_csv(contact_dict):
	with open('./contact_database.csv', mode='a', newline='') as test_database:
		name = contact_dict['name']
		email = contact_dict['email']
		subject = contact_dict['subject']
		message = contact_dict['message']
		csv_writer = csv.writer(test_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name, email, subject, message])