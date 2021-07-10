#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityIL
from typing import List

class Key(EntityIL):
	"""An abstract key to unlock a device or decode a message."""
	def setIsPhysical(self, aIsPhysical : long):
		self.___isPhysical = aIsPhysical

	def getIsPhysical(self) -> long:
		return self.___isPhysical

	def __init__(self):
		self.___isPhysical : long = None
		"""The key can be of physical type, i.e. key for a mechanical lock."""

