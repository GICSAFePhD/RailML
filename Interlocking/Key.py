#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityIL
from typing import List, NewType
Long = NewType("Long", int)

class Key(EntityIL.EntityIL):
	"""An abstract key to unlock a device or decode a message."""
	@property
	def IsPhysical(self) -> Long:
		return self.___isPhysical
	
	@IsPhysical.setter
	def IsPhysical(self, aIsPhysical : Long):
		self.___isPhysical = aIsPhysical

	def __init__(self):
		super().__init__()
		self.___isPhysical : Long = 0
		"""The key can be of physical type, i.e. key for a mechanical lock."""