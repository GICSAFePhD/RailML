#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import ATPdevice
from typing import List

class ATPdevices(object):
	"""container element for all ATPdevice elements (not with railML3.1)"""
	@property
	def ATPdevice(self) -> ATPdevice:
		return self.___atpDevice
	
	@ATPdevice.setter
	def ATPdevice(self, aATPdevice : ATPdevice):	# TODO *aATPdevice
		self.___atpDevice = aATPdevice

	def create_ATPdevice(self):
		if self.ATPdevice == None:
			self.ATPdevice = []
		self.ATPdevice.append(ATPdevice.ATPdevice())

	def __init__(self):
		self.___atpDevice : ATPdevice = None
		# @AssociationType Interlocking.ATPdevice*
		# @AssociationMultiplicity 1..*
		# """not with railML3.1"""