from paste.deploy import appconfig
import paste.fixture

from ckan.config.middleware import make_app
from ckan import plugins
from ckan.tests import conf_dir, url_for, CreateTestData, BaseCase

class TestMyPlugin(BaseCase):

    @classmethod
    def setup_class(cls):
         config = appconfig('config:test.ini', relative_to=conf_dir)
         config.local_conf['ckan.plugins'] = 'dfci'
         wsgiapp = make_app(config.global_conf, **config.local_conf)
         cls.app = paste.fixture.TestApp(wsgiapp)
         CreateTestData.create()

    @classmethod
    def teardown_class(cls):
        plugins.reset()


    def test_testing(self):
        url = url_for(controller='home', action='index')
        response = self.app.get(url)
        assert not isinstance(response.c.recently_changed_packages_activity_list_html, property),\
               "Es del tipo "+response.c.recently_changed_packages_activity_list_html.__class__.__name__
