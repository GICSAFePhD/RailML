#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import GenericIM
from typing import List

class GenericIMs(object):
	"""container element for all specificIM elements"""
	@property
	def GenericIM(self) -> GenericIM:
		return self.___specificIM
	
	@GenericIM.setter
	def GenericIM(self, *aGenericIM : GenericIM):
		self.___specificIM = aGenericIM

	def __init__(self):
		self.___specificIM : GenericIM = GenericIM.GenericIM()
		# @AssociationType Interlocking.GenericIM*
		# @AssociationMultiplicity 1..*
		# """Container with the generic classification of types used by a specific infrastructure manager."""

