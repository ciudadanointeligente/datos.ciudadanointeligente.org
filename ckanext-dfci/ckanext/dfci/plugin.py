import os
#from logging import getLogger

#from pylons import request

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IConfigurer

#log = getLogger(__name__)

class DFCIPlugin(SingletonPlugin):
	implements(IConfigurer, inherit=True)

	def update_config(self, config):
		here = os.path.dirname(__file__)
		rootdir = os.path.dirname(os.path.dirname(here))
		our_public_dir = os.path.join(rootdir, 'ckanext','dfci', 'theme', 'public')
		template_dir = os.path.join(rootdir, 'ckanext','dfci', 'theme', 'templates')
		config['extra_public_paths'] = ','.join([our_public_dir,config.get('extra_public_paths', '')])
		config['extra_template_paths'] = ','.join([template_dir,config.get('extra_template_paths', '')])
		config['ckan.site_title'] = u"Datos de la Fundacion Ciudadano Inteligente"