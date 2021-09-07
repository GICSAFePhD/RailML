#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import RestrictedArea
from typing import List

class ShuntingZone(RestrictedArea.RestrictedArea):
	"""Simple zone defined for shunting movements. It can be used to define any shunting zones."""
	def __init__(self):
		super().__init__()
