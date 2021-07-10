#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tGenericAspectList
from Interlocking import EntityIL
from typing import List

class GenericAspect(EntityIL):
	"""A signal aspect according to the IM regulations. Each aspect is given a unique identifier, a name, e.g. Vr-6 and description e.g. warning signal - expect stop (Vorsignal Halt erwarten). This element allows a generic classification of each aspect. The aspect can include speed information."""
	def setGenericAspect(self, aGenericAspect : tGenericAspectList):
		self.___genericAspect = aGenericAspect

	def getGenericAspect(self) -> tGenericAspectList:
		return self.___genericAspect

	def __init__(self):
		self.___genericAspect : tGenericAspectList = None
		# @AssociationType Interlocking.tGenericAspectList
		# """The classification of the aspect."""

