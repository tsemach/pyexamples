
"""
from: https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/

below, the code in the else block is executed only if the code in the try block didn't throw an exception. 
It's conceptually similar to using else with a for loop (which is itself a useful, if not widely known, idiom). 
"""

def display_username(user_id):
    try:
        db_connection = get_db_connection()
    except DatabaseEatenByGrueError:
        print('Sorry! Database was eaten by a grue.')
    else:
        print(db_connection.get_username(user_id))
        db_connection.cleanup()

