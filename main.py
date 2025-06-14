from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')  # Страница со всеми услугами

@app.route('/services/selection')
def selection():
    return render_template('selection.html')  # Детальная страница услуги

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Страница контактов

@app.route('/diagnostics')
def diagnostics():
    return render_template('diagnostics.html')  # Страница выездной диагностики

@app.route('/expert')
def expert():
    return render_template('expert.html')  # Страница эксперта диагностики

@app.route('/expert007')
def expert007():
    return render_template('expert007.html')  # Страница эксперта о себе
@app.route('/reviews')
def reviews():
    return render_template('reviews.html')  # Страница эксперта о себе

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')  # Страница эксперта о себе

@app.route('/disk')
def disk():
    return render_template('disk.html')  # Страница эксперта о себе


if __name__ == '__main__':
    app.run(debug=True)