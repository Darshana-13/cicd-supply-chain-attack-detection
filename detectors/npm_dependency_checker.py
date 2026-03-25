
import json

def check_npm_dependencies():

    with open("package.json") as f:
        data = json.load(f)

    deps = data["dependencies"]

    suspicious = []

    for pkg in deps:

        if pkg.startswith("test-"):

            suspicious.append(pkg)

    return suspicious
