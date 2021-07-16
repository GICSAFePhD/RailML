#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.DerailerIL import DerailerIL
from typing import List

class DerailersIL(object):
	def setDerailerIL(self, *aDerailerIL : DerailerIL):
		self._derailerIL = aDerailerIL

	def getDerailerIL(self) -> DerailerIL:
		return self._derailerIL

	def __init__(self):
		self._derailerIL : DerailerIL = None
		# @AssociationType Interlocking.DerailerIL*
		# @AssociationMultiplicity 1..*
		# """The derailer is a track asset that either allows or disallows train passage. Here the functional aspects for interlocking operation are considered."""

