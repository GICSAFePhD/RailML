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
	def GenericIM(self, aGenericIM : GenericIM):	# TODO *aGenericIM
		self.___specificIM = aGenericIM

	def create_GenericIM(self):
		if self.GenericIM == None:
			self.GenericIM = []
		self.GenericIM.append(GenericIM.GenericIM())
	
	def __init__(self):
		self.___specificIM : GenericIM = None
		# @AssociationType Interlocking.GenericIM*
		# @AssociationMultiplicity 1..*
		# """Container with the generic classification of types used by a specific infrastructure manager."""