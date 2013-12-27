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

import sys
import importlib

class DynamicModule(object):
	def __init__(self, module):
		
		self.module = "quickstart.%s" % module
		self.loaded = None
	
	def __getattribute__(self, attr):
		
		modname = object.__getattribute__(self, "module") 
		
		if not modname in sys.modules:
			# Load now
			mod = importlib.import_module(modname)
		else:
			mod = sys.modules[modname]
		
		return getattr(mod, attr)

__all__ = (
	"builder",
	"common",
	"events",
	"style",
	"threads",
	"scenes",
	"translations",
)

for module in __all__:
	globals()[module] = DynamicModule(module)
