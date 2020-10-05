import os
from app import create_app, db
from app.models import User, AnonymousUser

app = create_app(os.environ.get('APP_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, AnonymousUser=AnonymousUser)


@app.cli.command('test')
def test():
    """run unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command('deploy')
def deploy():
    """run deployment tasks"""
    import string
    import random
    import dotenv
    from flask_migrate import upgrade
    # run migrations
    upgrade()
    
    # set secret key
    env_file = dotenv.find_dotenv()
    secret_key = ''.join(random.choices(
        string.ascii_letters + string.digits + '@.-_=+', k=32))
    dotenv.set_key(env_file, 'SECRET_KEY', secret_key)
