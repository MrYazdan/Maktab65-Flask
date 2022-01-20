from flask import Flask
from views import *

# Configure Flask
app = Flask(__name__)

# Configure Urls
# app.add_url_rule('/', 'home', home)
app.add_url_rule('/hi/', 'hi', say_hello, defaults={'name': 'Kokab'})
app.add_url_rule('/hi/<name>', 'hi', say_hello)
app.add_url_rule('/hi', 'hello', say_hello_by_query)
app.add_url_rule('/pow/<int:num1>/', 'power', power, defaults={'num2': 2})
app.add_url_rule('/pow/<int:num1>/<int:num2>', 'power', power)
app.add_url_rule('/search/<text>', 'search', google_search)
app.add_url_rule('/method', 'method_detector', detector, methods=['GET', 'POST'])
app.add_url_rule('/info', 'request_info', request_info, methods=['GET', 'POST'])
app.add_url_rule('/handler', 'handle', handler)

# Flask 2:
app.add_url_rule('/', 'home', home)
app.add_url_rule('/posts', 'posts', posts)
app.add_url_rule('/posts/<int:post_id>', 'post', post)
app.add_url_rule('/new_post', 'new_post', new_post, methods=['POST', 'GET'])
app.add_url_rule('/about-us', 'about', about)

if __name__ == '__main__':
    app.run()
