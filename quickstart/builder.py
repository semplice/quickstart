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

from gi.repository import Gtk

class from_file:
	""" builder.from_file is a class decorator that will automatically load
	the UI file specified in the arguments in a Gtk.Builder object.
	
	A Dynamic dictionary will be created in class.objects. This special dict
	gets the UI objects on-the-fly.
	
	The only required parameter is the UI file position.
	
	Usage example:
	
		@quickstart.builder.from_file("./test.glade")
		class GUI:
			def __init__(self):
				
				self.objects["main_window"].show_all()
	
	The Gtk.Builder object will be created at class.__builder. """
	
	class DynamicObjectsDictionary(dict):
		""" A dynamic dictionary! """
		
		def __init__(self, builder):
			self.builder = builder
			
			dict.__init__(self)
		
		def __getitem__(self, key):
			""" Returns the specified object if it is already in the dictionary,
			otherwise gets it from the builder first and then returns it. """
			
			itm = self.get(key)
			if not itm:
				obj = self.builder.get_object(key)
				if not obj:
					raise Exception("Object %s not found!" % key)
				self[key] = obj
				itm = obj
			
			return itm
		
		__getattr__ = __getitem__
		__setattr__ = dict.__setitem__
		__delattr__ = dict.__delitem__
	
	def __init__(self, uipath):
		""" Initializes the class. """
		
		self.uipath = uipath
	
	def __call__(self, clss):
		""" Magic. """
		
		def wrapper(*args, **kwargs):	
			
			clss.__builder = Gtk.Builder()
			clss.__builder.add_from_file(self.uipath)
			
			clss.objects = self.DynamicObjectsDictionary(clss.__builder)
			return clss(*args, **kwargs)
		
		return wrapper

