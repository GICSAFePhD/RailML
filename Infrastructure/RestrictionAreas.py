#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import RestrictionArea
from typing import List

class RestrictionAreas(object):
	@property
	def RestrictionArea(self) -> RestrictionArea:
		return self.___restrictionArea
	
	@RestrictionArea.setter
	def RestrictionArea(self, aRestrictionArea : RestrictionArea):
		self.___restrictionArea = aRestrictionArea

	def __init__(self):
		self.___restrictionArea : RestrictionArea = RestrictionArea.RestrictionArea()
		# @AssociationType Infrastructure.RestrictionArea*
		# @AssociationMultiplicity 1..*

