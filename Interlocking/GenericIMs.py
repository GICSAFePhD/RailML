#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.GenericIM import GenericIM
from typing import List

class GenericIMs(object):
	"""container element for all specificIM elements"""
	def setSpecificIM(self, *aSpecificIM : GenericIM):
		self._specificIM = aSpecificIM

	def getSpecificIM(self) -> GenericIM:
		return self._specificIM

	def __init__(self):
		self._specificIM : GenericIM = None
		# @AssociationType Interlocking.GenericIM*
		# @AssociationMultiplicity 1..*
		# """Container with the generic classification of types used by a specific infrastructure manager."""

