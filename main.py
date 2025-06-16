from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/services/selection')
def selection():
    return render_template('selection.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/diagnostics')
def diagnostics():
    return render_template('diagnostics.html')

@app.route('/expert')
def expert():
    return render_template('expert.html')

@app.route('/expert007')
def expert007():
    return render_template('expert007.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/disk')
def disk():
    return render_template('disk.html')

@app.route('/consultation')
def consultation():
    return render_template('consultation.html')  # Создайте этот файл




if __name__ == '__main__':
    app.run(debug=True)