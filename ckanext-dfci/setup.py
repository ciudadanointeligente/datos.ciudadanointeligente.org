from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-dfci',
	version=version,
	description="CKAN Extension for datos.ciudadanointeligente.org",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Labs FCI',
	author_email='devteam@ciudadanointeligente.org',
	url='datos.ciudadanointeligente.org',
	license='GLP v3',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.dfci'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	dfci=ckanext.dfci.plugin:DFCIPlugin
	""",
)
