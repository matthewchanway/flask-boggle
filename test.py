from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import pdb

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class AllTests(TestCase):
    # """
    # Checking that the 'gameboard' stored in session is an instance of a list.
    # """
    # def test_gameboard_init(self):
    #     with app.test_client() as client:
    #         resp = client.get("/boggle")

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIsInstance(session['gameboard'], list)

    def test_check_guess(self):
        """
        Upon posting a guess ('hi'), checking that the result will either be OK, not-on-board, or not-word.
        """
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['gameboard'] = [['h','i','v','d','s'],['c','t','o','b','e'],['a','b','c','d','e'],['g','o','d','a','b'],['s','e','e','a','c']]  
            resp = client.post('/guess/hi')
                    
            html = resp.get_data(as_text=True)
            # pdb.set_trace()
            self.assertEqual(resp.status_code, 200)
            self.assertIn(bytes("ok","utf-8"),resp.data)
            

    # def test_check_session(self):
    #     """
    #     Test that 'games played' will be 1 upon posting to player-data, and check for the correct status code.
    #     """

    #     with app.test_client() as client:
    #         resp = client.post('/player-data',json={'storedScore': 1})

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(session['games_played'], 1)