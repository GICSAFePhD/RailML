#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import DerailerIL
from typing import List

class DerailersIL(object):
	@property
	def DerailerIL(self) -> DerailerIL:
		return self.___derailerIL
	
	@DerailerIL.setter
	def DerailerIL(self, aDerailerIL : DerailerIL):	# TODO *aDerailerIL
		self.___derailerIL = aDerailerIL

	def create_DerailerIL(self):
		if self.DerailerIL == None:
			self.DerailerIL = []
		self.DerailerIL.append(DerailerIL.DerailerIL())

	def __init__(self):
		self.___derailerIL : DerailerIL = None
		# @AssociationType Interlocking.DerailerIL*
		# @AssociationMultiplicity 1..*
		# """The derailer is a track asset that either allows or disallows train passage. Here the functional aspects for interlocking operation are considered."""