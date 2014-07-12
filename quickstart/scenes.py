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

from gi.repository import GObject
import quickstart.threads
import quickstart.events
import importlib

class BaseScene:
	""" A BaseScene() class is a base scene object. """
	
	scene_container = None
	
	def __init__(self, parent):
		self.parent = parent
	
	def prepare_scene(self):
		
		pass
	
	def on_scene_called(self):
		
		pass
	
	def on_scene_asked_to_close(self):
		"""
		Called when the scene has been asked to close (via SceneManager.can_close()).
		Returns True if the scene can be switched, False otherwise.
		"""
		
		return True

class SceneManager:
	""" A SceneManager() class is an object that manages the scenes. """
	
	loaded_scenes = {}
	
	def __init__(self, parent, container, scenes):
		""" Initializes the SceneManager. """
		
		self.current_scene = None
		
		self.parent = parent
		self.container = container
		self.scenes = scenes
	
	def can_close(self):
		"""
		This method calls on_scene_asked_to_close on the current scene, and
		returns its result.
		"""
		
		if self.current_scene:
			return self.loaded_scenes[self.current_scene]["object"].on_scene_asked_to_close()
		else:
			return True
	
	def load(self, scene):

		if self.current_scene == scene:
			
			if scene in self.loaded_scenes:
				# Has a separate module
				# fire called
				GObject.idle_add(self.loaded_scenes[scene]["object"].on_scene_called)
			
			# Scene is currently shown, returning nicely
			return
		
		self.__load(scene)
	
	@quickstart.threads.on_idle
	def __load(self, scene):
		""" Loads a scene. """
				
		if self.scenes[scene].startswith(":"):
			# Scene is an internal page
			self.container.set_visible_child_name(self.scenes[scene].replace(":",""))
		elif not scene in self.loaded_scenes:
			self.loaded_scenes[scene] = {}
			self.loaded_scenes[scene]["module"] = importlib.import_module(self.scenes[scene])
			self.loaded_scenes[scene]["object"] = self.loaded_scenes[scene]["module"].Scene(self.parent)
			
			# Prepare the scene
			self.loaded_scenes[scene]["object"].prepare_scene()
			
			# events
			if hasattr(self.loaded_scenes[scene]["object"], "events"):
				quickstart.events.connect(self.loaded_scenes[scene]["object"])
			
			# Remove scene container's parent, so that we can reparent it later
			parent = self.loaded_scenes[scene]["object"].scene_container.get_parent()
			if parent:
				parent.remove(self.loaded_scenes[scene]["object"].scene_container)
			
			# Do the real thing and pack the main scene widget to the container.
			# The index will be stored in self.loaded_scenes[scene]["page"].
			self.loaded_scenes[scene]["page"] = self.container.add_named(self.loaded_scenes[scene]["object"].scene_container, scene)
			self.container.set_visible_child(self.loaded_scenes[scene]["object"].scene_container)
			
			# fire called
			GObject.idle_add(self.loaded_scenes[scene]["object"].on_scene_called)
		else:
			# Simply set the page, scene already loaded.
			self.container.set_visible_child(self.loaded_scenes[scene]["object"].scene_container)

			# fire called
			GObject.idle_add(self.loaded_scenes[scene]["object"].on_scene_called)
				
		self.current_scene = scene

def initialize(clss):
	
	# Get the container
	#container = clss.objects[clss.scenes_container]
	container = clss.scene_container
	
	# Return a new SceneManager
	return SceneManager(clss, container, clss.scenes)
