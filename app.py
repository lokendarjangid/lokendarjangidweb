import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    
    data = [ # keep it in multiples of 4 for optimal design
        ('Project 1', 'Illustration', '#','portfolio-1.jpg'),
        #('Name', 'Description','link','imageName')
    ]
    
    return flask.render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    # Render the 404.html template with the 404 status code
    html404 = '<body style="background: black; font-family: Arial, Helvetica, sans-serif; display: flex; align-items: center; justify-content: center; margin-top: -50px;"><h1 style="color: white; font-size: 5rem;">404: Page Not Found :(</h1>'
    return html404, 404

if __name__ == '__main__':
    app.run(debug=True)