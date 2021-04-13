import os
from flask import Flask, json, request, Response

app = Flask(__name__)
app.config.update(TESTING=True, SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/')
directory_paths = os.listdir("functions")


@app.route("/<string:var>", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
def make_view(var):
    exec(f"from functions.{var} import main")
    function = eval("main")
    response = function.execute()
    if not response:
        return Response(
            status=400,
        )

    return Response(
        response=json.dumps(response),
        mimetype="application/json",
        status=200,
    )


if __name__ == "__main__":
    app.run(debug=True)
