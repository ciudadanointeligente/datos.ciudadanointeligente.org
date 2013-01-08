import os
#from logging import getLogger

#from pylons import request

from ckan.plugins import implements, SingletonPlugin, IRoutes
from ckan.plugins import IConfigurer

#log = getLogger(__name__)

class DFCIPlugin(SingletonPlugin):
	implements(IConfigurer, inherit=True)
	implements(IRoutes, inherit=True)

	def update_config(self, config):
		here = os.path.dirname(__file__)
		rootdir = os.path.dirname(os.path.dirname(here))
		our_public_dir = os.path.join(rootdir, 'ckanext','dfci', 'theme', 'public')
		template_dir = os.path.join(rootdir, 'ckanext','dfci', 'theme', 'templates')
		config['extra_public_paths'] = ','.join([our_public_dir,config.get('extra_public_paths', '')])
		config['extra_template_paths'] = ','.join([template_dir,config.get('extra_template_paths', '')])
		config['ckan.site_title'] = u"Datos de la Fundacion Ciudadano Inteligente"
		config['ckan.site_logo'] = "/base/images/logo-data.png"
        #ckan.favicon = /images/icons/ckan.ico
		config['ckan.favicon'] = "/base/images/icons/favicon-data.ico"



	def before_map(self, map):
		"""This IRoutes implementation overrides the standard
		``/user/register`` behaviour with a custom controller.  You
		might instead use it to provide a completely new page, for
		example.

		Note that we have also provided a custom register form
		template at ``theme/templates/user/register.html``.
		"""
		# Hook in our custom user controller at the points of creation
		# and edition.

		map.connect('/',
		            controller='ckanext.dfci.controllers:CustomHomeController',
		            action='index')
		return map
