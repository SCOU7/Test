from flask import Flask
import flask_cors
app=Flask(__name__)

# Members API Route
@app.route("/members")
@flask_cors.cross_origin()
def members():
  return {"members" : ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
  app.run(debug=True)