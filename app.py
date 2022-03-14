import os
from flask import Flask, json, request, Response

app = Flask(__name__)
app.config.update(
    GOOGLE_SERVICE_ACCOUNT=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", None),
    PROJECT_ID="app-agrogo",
    TESTING=True,
)
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
