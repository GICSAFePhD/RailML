#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tGenericAspectList, EntityIL
from typing import List

class GenericAspect(EntityIL.EntityIL):
	"""A signal aspect according to the IM regulations. Each aspect is given a unique identifier, a name, e.g. Vr-6 and description e.g. warning signal - expect stop (Vorsignal Halt erwarten). This element allows a generic classification of each aspect. The aspect can include speed information."""
	@property
	def GenericAspect(self) -> tGenericAspectList:
		return self.___genericAspect
	
	@GenericAspect.setter
	def GenericAspect(self, aGenericAspect : tGenericAspectList):
		self.___genericAspect = aGenericAspect

	def __init__(self):
		super().__init__()
		self.___genericAspect : tGenericAspectList = None
		# @AssociationType Interlocking.tGenericAspectList
		# """The classification of the aspect."""