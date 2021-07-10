#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import Border
from typing import List

class Borders(object):
	def setBorder(self, *aBorder : Border*):
		self._border = aBorder

	def getBorder(self) -> Border*:
		return self._border

	def __init__(self):
		self._border : Border = None
		# @AssociationType Infrastructure.Border*
		# @AssociationMultiplicity 1..*

