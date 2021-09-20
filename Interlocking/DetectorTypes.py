#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tDetectorTypeListExt, EntityIL
from typing import List

class DetectorTypes(EntityIL.EntityIL):
	"""The generic classification of detector types."""
	@property
	def tDetectorTypeListExt(self) -> tDetectorTypeListExt:
		return self.___detectorType
	
	@tDetectorTypeListExt.setter
	def tDetectorTypeListExt(self, atDetectorTypeListExt : tDetectorTypeListExt):
		self.___detectorType = atDetectorTypeListExt

	def __init__(self):
		super().__init__()
		self.___detectorType : tDetectorTypeListExt = None
		# @AssociationType Interlocking.tDetectorTypeListExt
		# """The classification of the particular detector type."""

