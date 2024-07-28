from flask import Flask, render_template,jsonify, request
from database import load_rank_from_db,load_all_ranks_from_db

app=Flask(__name__)#object of class

@app.route("/")
def first():
  return render_template('start_page.html')

@app.route("/home")
def open_Home():
  return render_template('home.html')

@app.route("/home/play")
def play_game():
  return render_template('play.html')

@app.route("/home/ranks")
def show_ranks():
    ranks = load_all_ranks_from_db()
    return render_template('rank_page.html', ranks=ranks)

@app.route('/home/ranks/<int:id>', methods=['GET'])
def show_specific_rank(id):
    rank = load_rank_from_db(id)
    return jsonify(rank) if rank else jsonify({"error": "Rank not found"})

@app.route("/home/logs")
def show_logs():
  return render_template('logs_page.html')

# @app.route("/")
# def exit_button():
#   return render_template('exit.html')

if __name__=="__main__":
  app.run(debug=True)