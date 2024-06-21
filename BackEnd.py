from flask import *
from pyngrok import ngrok
ngrok.set_auth_token("2fhOSoa9jSR3KoJHNOmgUultPE2_6jkfdizMSEioQtYY1Q35s")
public_url = ngrok.connect(5000).public_url
app = Flask(__name__)
@app.route("/maths",methods=["POST"])
def index():
  return render_template("index.html")
@app.route("/getPrompt",methods = ["POST"])
def another_index():
  if request.method == "POST":
    question = request.form["question"]
    response = query_engine.query(question)
    return jsonify(response)
if __name__=='__main__':
  print(public_url)
  app.run(port = 5000)
