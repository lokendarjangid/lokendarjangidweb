from flask import Flask, render_template

app = Flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    
    data = [ # keep it in multiples of 4 for optimal design
        ('AI Virtual Mouse', 'Mouse movements control using hand movements and perform some actions using hand gesturs.', 'https://github.com/lokendarjangid/virtual-mouse-new','https://raw.githubusercontent.com/lokendarjangid/virtual-mouse-new/main/AI-Virtual-Mouse.jpg'),
        ('Waker Linux', 'Waker is a simple tool to sleep your computer when you are away from it.', 'https://github.com/lokendarjangid/waker_linux','https://raw.githubusercontent.com/lokendarjangid/waker_linux/master/waker-linux.jpg'),
        ('Discord Bot', 'Discord bot connect with chatgpt3 to give reasponse and chat with you. use dalle-2 to generate image from text.', 'https://github.com/lokendarjangid/dis-bot','https://raw.githubusercontent.com/lokendarjangid/dis-bot/master/discord-bot.jpg'),
        #('Name', 'Description','link','imageName')
    ]
    
    return render_template('index.html',data=data)

@app.errorhandler(404)
def page_not_found(e):
    # Render the 404.html template with the 404 status code
    html404 = '<body style="background: black; font-family: Arial, Helvetica, sans-serif; display: flex; align-items: center; justify-content: center; margin-top: -50px;"><h1 style="color: white; font-size: 5rem;">404: Page Not Found :(</h1>'
    return html404, 404

if __name__ == '__main__':
    app.run()