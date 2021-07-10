#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import Interface
from typing import List

class Interfaces(object):
	"""container element for all Interface elements"""
	def setInterface(self, *aInterface : Interface*):
		self._interface = aInterface

	def getInterface(self) -> Interface*:
		return self._interface

	def __init__(self):
		self._interface : Interface = None
		# @AssociationType Interlocking.Interface*
		# @AssociationMultiplicity 1..*
		# """Description of a physical interface with definition of the information to be exchanged in which direction."""

