# -*- coding: utf-8 -*-
#
# quickstart - Refreshing the GUI world.
# Copyright (C) 2013  Eugenio "g7" Paolantonio
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#

import gettext
import locale

class Translation:
	""" Translation() is the class that handles translations. """
	
	def __init__(self, domain, localedir=None, languages=None):
		""" Initializes the Translation class. """
		
		self.domain = domain
		self.localedir = localedir
		self.languages = languages
		
		self.load()
	
	def load(self, install=False):
	
		self.__gettext  = gettext.translation(self.domain, self.localedir, self.languages, fallback=True)
		self._ = self.__gettext.ugettext
		
	def install(self):
		""" Installs the _() function into the builtins namespace. """
		
		self.__gettext.install(unicode=True)
	
	def change_locale(self, newlanguages, install=True):
		""" Changes the current locale with a new one, specified in newlanguages. """
		
		self.languages = newlanguages
		
		self.load()
		if install: self.install()
	
	def bind_also_locale(self):
		""" Properly binds also the 'locale' module. Use this if you want to make glade UI files translatable. """
		
		locale.bindtextdomain(self.domain, self.localedir)
		locale.textdomain(self.domain)
