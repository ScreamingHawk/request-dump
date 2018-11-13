from flask import Flask, request

app = Flask(__name__)

def log(filename, s):
	print(s)
	with open("output/{}".format(filename), "w") as fout:
		fout.write(s)

@app.route("/body", methods=["GET", "POST"])
def dump_request():
	log("body.txt", request.get_data(as_text=True))
	return ""

print("Running")
