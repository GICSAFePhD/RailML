#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import GenericIM
from typing import List

class GenericIMs(object):
	"""container element for all specificIM elements"""
	@property
	def SpecificIM(self) -> GenericIM:
		return self.___specificIM
	
	@SpecificIM.setter
	def SpecificIM(self, aSpecificIM : GenericIM):	# TODO *aSpecificIM
		self.___specificIM = aSpecificIM

	def create_SpecificIM(self):
		if self.SpecificIM == None:
			self.SpecificIM = []
		self.SpecificIM.append(GenericIM.GenericIM())
	
	def __init__(self):
		self.___specificIM : GenericIM = None
		# @AssociationType Interlocking.GenericIM*
		# @AssociationMultiplicity 1..*
		# """Container with the generic classification of types used by a specific infrastructure manager."""