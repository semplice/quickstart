#!/usr/bin/python
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

from gi.repository import Gtk, GObject

import time
import quickstart

@quickstart.style.custom_css("./tropez.css")
@quickstart.builder.from_file("./prova.glade")
class GUI:
	
	events = {
		"clicked": ("button1","button2",),
		"destroy": ("main_window",)
	}
	
	def on_main_window_destroy(self, window):
		
		Gtk.main_quit()
	
	def on_button1_clicked(self, button):
		
		button.set_label("AOH")
	
	@quickstart.threads.thread
	def on_button2_clicked(self, button):
		
		for item in range(100):
			print item
			GObject.idle_add(button.set_label, str(item))
			time.sleep(0.1)
		print "END"
	
	def __init__(self):
		
		self.objects.label1.set_markup("<b>CIAO QUICKSTART!</b>")
		self.objects.main_window.show_all()
		
		self.objects.button1.set_label("Se mi clicchi ti saluto!")
				
quickstart.common.quickstart(GUI)
