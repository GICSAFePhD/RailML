#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import Interface
from typing import List

class Interfaces(object):
	"""container element for all Interface elements"""
	@property
	def Interface(self) -> Interface:
		return self.___interface
	
	@Interface.setter
	def Interface(self, *aInterface : Interface):
		self.___interface = aInterface

	def __init__(self):
		self.___interface : Interface = None
		# @AssociationType Interlocking.Interface*
		# @AssociationMultiplicity 1..*
		# """Description of a physical interface with definition of the information to be exchanged in which direction."""