import os
from flask import Flask, request

app = Flask(__name__)
app.config.update(TESTING=True, SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/')
directory_paths = os.listdir("functions")


@app.route("/<string:var>")
def make_view(var):
    exec(f"from functions.{var} import main")
    function = eval("main")
    response = function.execute()
    if not function.execute():
        return ("BAD REQUEST", 400)

    return (response, 200)


if __name__ == "__main__":
    app.run(debug=True)
