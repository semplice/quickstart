#!/usr/bin/python3
# -*- coding: utf-8 -*-

import quickstart.translations

cl = quickstart.translations.Translation("hello")
cl.install()
cl.bind_also_locale()

print(_("Hello, world!"))

cl.change_locale(["en_US"])

print(_("Hello, world!"))
