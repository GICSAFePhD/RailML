#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.ATPdevice import ATPdevice
from typing import List

class ATPdevices(object):
	"""container element for all ATPdevice elements (not with railML3.1)"""
	def setAtpDevice(self, *aAtpDevice : ATPdevice):
		self._atpDevice = aAtpDevice

	def getAtpDevice(self) -> ATPdevice:
		return self._atpDevice

	def __init__(self):
		self._atpDevice : ATPdevice = None
		# @AssociationType Interlocking.ATPdevice*
		# @AssociationMultiplicity 1..*
		# """not with railML3.1"""

