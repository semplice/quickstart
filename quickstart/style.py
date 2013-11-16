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

from gi.repository import Gtk, Gdk

class custom_css:
	""" style.custom_css is a class decorator that permits to load a
	custom CSS file to further customize the look and feel of the application.
	
	The only required parameter is the path to the CSS file.
	
	Usage example:
	
		@quickstart.style.custom_css("./test.css")
		class GUI:
			def __init__(self):
				...
	
	The CSS provider, GDKScreen and GtkStyleContext are respectively at
	class.__cssProvider, class.__screen and class.__styleContext. """
	
	def __init__(self, csspath):
		""" Initializes the class. """
		
		self.csspath = csspath
	
	def __call__(self, clss):
		""" Magic. """
		
		def wrapper(*args, **kwargs):	

			clss.__cssProvider = Gtk.CssProvider()
			clss.__cssProvider.load_from_path(self.csspath)
			clss.__screen = Gdk.Screen.get_default()
			clss.__styleContext = Gtk.StyleContext()
			clss.__styleContext.add_provider_for_screen(clss.__screen, clss.__cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

			return clss(*args, **kwargs)
		
		return wrapper

