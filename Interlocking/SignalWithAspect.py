#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tProtectingSideList, SignalAndGivenAspect, EntityIL
from typing import List

class SignalWithAspect(EntityIL.EntityIL):
	"""reference to any signal and its aspect inside or outside the restricted area required for use and/or protection"""
	@property
	def ProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide
	@property
	def GivenAspect(self) -> SignalAndGivenAspect:
		return self.___givenAspect

	@ProtectingSide.setter
	def ProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide
	@GivenAspect.setter
	def GivenAspect(self, aGivenAspect : SignalAndGivenAspect):
		self.___givenAspect = aGivenAspect

	def __init__(self):
		self.___protectingSide : tProtectingSideList = tProtectingSideList.tProtectingSideList()
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required aspect is for protection of the area from inside or outside"""
		self.___givenAspect : SignalAndGivenAspect = SignalAndGivenAspect.SignalAndGivenAspect()
		# @AssociationType Interlocking.SignalAndGivenAspect
		# @AssociationMultiplicity 1
		# """the tuple of references to the signal and its aspect plus the level of enforcement"""

