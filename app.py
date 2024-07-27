from flask import Flask, render_template,jsonify, request

app=Flask(__name__)#object of class

@app.route("/")
def first():
  return render_template('start_page.html')


if __name__=="__main__":
  app.run(debug=True)