from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/live/<username>")
def live(username=None):
  return render_template("live.html", username=username)

@app.errorhandler(404)
def not_found(error):
  return redirect(url_for("index"))

if __name__ == "__main__":
  app.debug = False
  app.run(threaded=True)