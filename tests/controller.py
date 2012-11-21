from ckan import plugins
from ckan.tests import BaseCase

class TestMyPlugin(BaseCase):

    @classmethod
    def setup_class(cls):
        # Use the entry point name of your plugin as declared
        # in your package's setup.py
        plugins.load('dfci')

    @classmethod
    def teardown_class(cls):
        plugins.reset()


    def test_testing(self):
        assert True, u"Esto tiene que fallar"
