import sys
from ckan.lib.base import request
from ckan.lib.base import c, g, h
from ckan.lib.base import model
from ckan.lib.base import render
from ckan.lib.base import _
import ckan.logic
from ckan.lib.navl.validators import not_empty

from ckan.controllers.home import HomeController


class CustomHomeController(HomeController):
	def index(self):
		response = super(CustomHomeController, self).index()
		context = {'model': model, 'session': model.Session, 'user': c.user or c.author}
		c.recently_changed_packages_activity_list_html = \
				ckan.logic.action.get.recently_changed_packages_activity_list_html(context, {})
		return render('home/index.html', cache_force=False)

