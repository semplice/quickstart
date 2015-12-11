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

import signal

from quickstart import events
from gi.repository import Gtk

def quickstart(gui, with_threads=True):
	""" common.quickstart() provide a quick way to start the main loop.
	It requires the class containing the UI.
	If the optional parameter with_threads is True (default), the GObject
	threads are automatically initialized.
	
	If the class contains the event dictionary (see events.connect() for details),
	events.connect() will be automatically called.
	
	This method also properly handles KeyboardInterrupts.
	
	Usage example:
	
		class GUI:
			
			events = {
				"clicked": ("button1","button2","button3"),
				"destroy": ("main_window",)
			}
			
			...
		
		common.quickstart(GUI, with_threads=True)
	
	"""
	
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	
	clss = gui()
	if hasattr(clss, "events"):
		events.connect(clss)
	
	# Handle threads?
	if with_threads:
		from gi.repository import GObject, Gdk
		GObject.threads_init()
		Gdk.threads_init()
	
	Gtk.main()
