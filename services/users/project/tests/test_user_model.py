# services/users/project/tests/test_user_model.py

import unittest

from sqlalchemy.exc import IntegrityError

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserModel(BaseTestCase):
    def test_add_user(self):
        user = add_user("testit", "testit@test.com", "thisisatest")
        self.assertTrue(user.id)
        self.assertEqual(user.username, "testit")
        self.assertEqual(user.email, "testit@test.com")
        self.assertTrue(user.active)
        self.assertTrue(user.password)

    def test_add_user_duplicate_username(self):
        add_user("testit", "testit@test.com", "thisisatest")
        duplicate_user = User(
            username="testit", email="testit@test2.com", password="thisisatest"
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        add_user("testit", "testit@test.com", "thisisatest")
        duplicate_user = User(
            username="testit2", email="testit@test.com", password="thisisatest"
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = add_user("testit", "testit@test.com", "thisisatest")
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_passwords_are_random(self):
        user_one = add_user("testit1", "testit1@test.com", ', "thisisatest"')
        user_two = add_user("testit2", "testit2@test2.com", ', "thisisatest"')
        self.assertNotEqual(user_one.password, user_two.password)


if __name__ == "__main__":
    unittest.main()
