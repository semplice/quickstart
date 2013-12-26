quickstart
==========

quickstart is a python library that has the aim to ease and reduce the work needed to create rich, interactive, GTK3 based graphical applications.

What does it provide?
---------------------

Currently (2013-12-26):
 * Easy load of GtkBuilder UI files
 * A dynamic dictionary where the widgets are stored, removing the need to always call builder.get_object() to get a widget.
 * Easy load of a custom CSS file to further customize the look and feel of the application
 * Easy to use helpers to get objects connected without wasting precious lines of code
 * Easy to use threads
 * Scenes support
 * Translations
 * And more to come...

Examples, please!
-----------------

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
			
			button.set_label("Hey!")
		
		@quickstart.threads.thread
		def on_button2_clicked(self, button):
			
			for item in range(100):
				print item
				GObject.idle_add(button.set_label, str(item))
				time.sleep(0.1)
			print "END"
		
		def __init__(self):
			
			self.objects["label1"].set_markup("<b>HELLO QUICKSTART!</b>")
			self.objects["main_window"].show_all()
			
			self.objects["button1"].set_label("Click me!")
					
	quickstart.common.quickstart(GUI)
