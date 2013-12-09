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

def connect(clss):
	""" events.connect() connects the events specified in the events dictionary in
	the class, which is the only required paramter.
	
	The objects are connected to methods called using the following scheme:
	
		on_<object>_<event>
	
	So, when talking about the "clicked" event of object "button1":
		
		on_button1_clicked
	
	Usage example:
	
		class GUI:
			
			events = {
				"clicked": ("button1","button2","button3"),
				"destroy": ("main_window",)
			}
			
			def on_button1_clicked(self, button):
				...
			
			def on_button2_clicked(self, button):
				...
			
			def on_button3_clicked(self, button):
				...
			
			def on_main_window_destroy(self, window):
				...
		
		g = GUI()
		events.connect(g)
	
	"""
	
	for event, to_connect in clss.events.items():				
		for obj in to_connect:
			if "-" in event:
				# Replace - with _ because python doesn't like them...
				event = event.replace("-","_")
			if not hasattr(clss, "on_%s_%s" % (obj, event)):
				print("quickstart: unable to connect %s. Event handler not found!" % obj)
				continue
					
			clss.objects[obj].connect(event, getattr(clss, "on_%s_%s" % (obj, event)))

