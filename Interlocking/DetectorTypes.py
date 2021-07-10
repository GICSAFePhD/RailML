#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tDetectorTypeListExt
from Interlocking import EntityIL
from typing import List

class DetectorTypes(EntityIL):
	"""The generic classification of detector types."""
	def setDetectorType(self, aDetectorType : tDetectorTypeListExt):
		self.___detectorType = aDetectorType

	def getDetectorType(self) -> tDetectorTypeListExt:
		return self.___detectorType

	def __init__(self):
		self.___detectorType : tDetectorTypeListExt = None
		# @AssociationType Interlocking.tDetectorTypeListExt
		# """The classification of the particular detector type."""

