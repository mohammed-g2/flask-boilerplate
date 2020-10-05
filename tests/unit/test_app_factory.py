import unittest
from flask import current_app
from app import create_app, db


class TestAppFactory(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app, current_app._get_current_object())

    def test_app_testing(self):
        self.assertTrue(current_app.config['TESTING'])
        self.assertEqual(current_app.config['SQLALCHEMY_DATABASE_URI'], 'sqlite://')
        self.assertEqual(current_app.config['MAIL_SERVER'], 'localhost')
