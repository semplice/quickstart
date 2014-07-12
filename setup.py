#!/usr/bin/env python3
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

from distutils.core import setup

setup(name='quickstart',
	version='2.0.0',
	description='a python library that has the aim to ease and reduce the work needed to create rich, interactive, GTK3 based graphical applications.',
	author='Eugenio Paolantonio',
	author_email='me@medesimo.eu',
	url='https://github.com/semplice/quickstart',
	packages=[
		"quickstart"
      ],
	requires=['gi.repository.Gtk', 'gi.repository.GObject', 'gi.repository.Gdk', 'importlib', 'gettext', 'locale', 'signal', 'threading', 'sys']
)

