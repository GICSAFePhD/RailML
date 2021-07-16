#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class Key(EntityIL):
	"""An abstract key to unlock a device or decode a message."""
	def setIsPhysical(self, aIsPhysical : int):	#TODO DEFINED AS LONG
		self.___isPhysical = aIsPhysical

	def getIsPhysical(self) -> int:	#TODO DEFINED AS LONG
		return self.___isPhysical

	def __init__(self):
		self.___isPhysical : int = None	#TODO DEFINED AS LONG
		"""The key can be of physical type, i.e. key for a mechanical lock."""

