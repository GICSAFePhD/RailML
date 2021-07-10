#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import DerailerIS
from typing import List

class DerailersIS(object):
	def setDerailerIS(self, *aDerailerIS : DerailerIS*):
		self._derailerIS = aDerailerIS

	def getDerailerIS(self) -> DerailerIS*:
		return self._derailerIS

	def __init__(self):
		self._derailerIS : DerailerIS = None
		# @AssociationType Infrastructure.DerailerIS*
		# @AssociationMultiplicity 1..*

