from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_segura_para_sesiones'

# Usuario fijo para el login
USER = {
    'username': 'ronald',
    'password': 'alfonso25'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER['username'] and password == USER['password']:
            session['username'] = username
            return redirect(url_for('converter'))
        else:
            return 'Credenciales incorrectas'
    return render_template('login.html')

@app.route('/converter', methods=['GET', 'POST'])
def converter():
    if 'username' not in session:
        return redirect(url_for('login'))

    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            unit = request.form['unit']
            if unit == 'km_to_miles':
                result = round(value * 0.621371, 2)
            elif unit == 'miles_to_km':
                result = round(value / 0.621371, 2)
        except ValueError:
            result = 'Entrada inválida'
    return render_template('converter.html', username=session['username'], result=result)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
