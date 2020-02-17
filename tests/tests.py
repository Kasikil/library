from app import app, db
from app.models import User
from config import Config
from flask_api import status
import unittest


class UserModelCase(unittest.TestCase):

    def setUp(self):
        self.good_user = User(username=Config.good_test_user, password=Config.good_test_password)
        db.session.add(self.good_user)
        db.session.commit()
        pass

    def tearDown(self):
        User.query.delete()
        db.session.commit()
        pass

    # Login Tests


if __name__ == '__main__':
    unittest.main(verbosity=2)
