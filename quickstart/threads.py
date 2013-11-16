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

from threading import Thread

def thread(function):
	""" threads.thread is a method decorator that makes sure that the decorated
	function is executed in a threading.Thread.
	
	No parameters are required.
	
	Usage example:
	
		class GUI:
			
			@threads.thread
			def this_will_be_executed_in_a_thread(self, string):
				print string
			
			def __init__(self):
				self.this_will_be_executed_in_a_thread("Test") """
		
	def wrapper(*args, **kwargs):
				
		return Thread(target=function, args=args, kwargs=kwargs).start()
		
	return wrapper
