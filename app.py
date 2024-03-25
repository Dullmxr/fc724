from flask import Flask, redirect, render_template, url_for

from form import DataCollectionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace 'your_secret_key' with a real secret key


# Route for the welcome page
@app.route('/')
def welcome():
    # Assuming welcome.html is in the 'templates' directory
    return render_template('welcome.html')

# Route for the information page
@app.route('/information')
def information():
    # Assuming information.html is in the 'templates' directory
    return render_template('information.html')

@app.route('/collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()
    if form.is_submitted():
        # Process form data here
        with open('submissions.txt', 'a') as file:
            file.write(f'Name: {form.name.data}, Email: {form.email.data}, student_number: {form.student_number.data}, grades: {form.grades.data}, suggestions_for_improvement: {form.suggestions_for_improvement.data}, satisfaction: {form.satisfaction.data}\n')
        return redirect(url_for('welcome'))  # Redirect to a new page on successful submission
    return render_template('collection.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

