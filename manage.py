import unittest
from core import app
<<<<<<< HEAD
from flask_script import Manager

=======
from core.config import TestConfig
from flask_script import Manager

app.config.from_object(TestConfig)
>>>>>>> 9a953c6... created test suit, updated configuration setting and entry, created manage.py file
manager = Manager(app)


@manager.command
def tests():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
