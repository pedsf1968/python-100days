# python -m pip install -r requirements.txt
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = StringField('Coffee', validators=[DataRequired()])
    wifi = StringField('Wifi', validators=[DataRequired()])
    power = StringField('Power', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route(rule='/add', methods=['GET', 'POST'])
def add_cafe():
    add_form = CafeForm()
    if add_form.validate_on_submit():
        with open('cafe-data.csv', mode='a', newline='\n', encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow([add_form.cafe.data,
                              add_form.location.data,
                              add_form.open.data,
                              add_form.close.data,
                              add_form.coffee.data,
                              add_form.wifi.data,
                              add_form.power.data])
        return redirect('/cafes')
    return render_template('add.html', form=add_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
