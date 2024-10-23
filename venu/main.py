from flask import Flask

app = Flask(__name__)

@app.route("/test/")
def page_test():
    return "Приложение работает"

app.run()