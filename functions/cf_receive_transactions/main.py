def execute(request):
    request_json = request.get_json()
    save_transaction(request=request)
    return ("", 200)


def save_transaction(request):
    print("FORM")
    print(f"request_json: {request.form.to_dict()}")
    print(None)
    print("JSON")
    print(f"request_json: {request.json}")