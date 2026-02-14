import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask import Flask, render_template
import json

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
    from flask import redirect, url_for
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

def handler(event, context):
    """Netlify function handler"""
    # Create a mock request environment
    environ = {
        'REQUEST_METHOD': event.get('httpMethod', 'GET'),
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': event.get('queryStringParameters', ''),
        'SERVER_NAME': 'netlify.com',
        'SERVER_PORT': '443',
        'wsgi.url_scheme': 'https',
        'wsgi.input': '',
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }

    # Start response
    headers = {}
    def start_response(status, response_headers):
        nonlocal headers
        headers = dict(response_headers)

    # Get response from Flask app
    response = app(environ, start_response)
    
    # Return response in Netlify format
    return {
        'statusCode': int(status.split(' ')[0]) if status else 200,
        'headers': headers,
        'body': ''.join(response)
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
