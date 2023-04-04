import sqlite3
from credits import credits
import re
from sqlite3 import Error

 
def newplayer(username: str):
    try:
        if re.match(r'^(?=.[a-z])(?=.[A-Z])(?=.*\d)[A-Za-z\d]$', username):
            conn = sqlite3.connect('ahorcadogame.db')
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO players (username, points) VALUES (?, ?)", ({username}, 0))
            conn.commit()
            conn.close()
        else:
            print ("Usernames permitted have only alphanumerical characters, please try again")
            
    except Error as e:
       print(f"The error '{e}' occurred")
    except KeyboardInterrupt:
        credits()

    return 