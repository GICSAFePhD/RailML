#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import RestrictionArea
from typing import List

class RestrictionAreas(object):
	def setRestrictionArea(self, *aRestrictionArea : RestrictionArea*):
		self._restrictionArea = aRestrictionArea

	def getRestrictionArea(self) -> RestrictionArea*:
		return self._restrictionArea

	def __init__(self):
		self._restrictionArea : RestrictionArea = None
		# @AssociationType Infrastructure.RestrictionArea*
		# @AssociationMultiplicity 1..*

