from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard page route"""
    return render_template('dashboard.html')

@app.route('/story')
def story():
    """Story page route - redirects to story1"""
    from flask import redirect
    return redirect(url_for('story1'))

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/story1')
def story1():
    """Story 1 page route"""
    return render_template('story1.html')

@app.route('/story2')
def story2():
    """Story 2 page route"""
    return render_template('story2.html')

@app.route('/story3')
def story3():
    """Story 3 page route"""
    return render_template('story3.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
