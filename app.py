import pdb
from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "way-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

@app.route('/boggle')
def display_gameboard():
    """
    Instantiates the gameboard, saves it to the session, and passes it to the Jinger template where it's displayed.
    """
    gameboard = boggle_game.make_board()
    session['gameboard'] = gameboard
    return render_template("board-display.html",gameboard=gameboard)

@app.route('/guess/<guess>', methods=['POST','GET'])
def check_guess(guess):
    """
    Receives the Axios post request and runs the check_valid_word function on the gameboard, returning a JSON response 
    where the word is either 'OK', 'not on board',or 'not a word.'
    """
    print("There should be an argument coming in from the url:", guess, "***************************************")  
    gameboard = session['gameboard']
    result = boggle_game.check_valid_word(gameboard,guess)
    response = jsonify(result = result)
    return response

@app.route('/player-data', methods =['POST', 'GET'])
def record_player_data():
    """
    Receives an axios request when the game is over, saving the total number of games played in session,
    as well as the highest score recorded.
    """
    res = request.json
    if 'games_played' in session:
        session['games_played'] = session.get('games_played')+1
    else:
        session['games_played'] = 1
    if 'high_score' in session:
        if res.get('storedScore') > session.get('high_score'):
            session['high_score'] = res['storedScore']
    else:
        session['high_score'] = res['storedScore']
    
    # print(session['games_played'])
    # print(session['high_score'])
    # pdb.set_trace()
    return 'yes'
   




