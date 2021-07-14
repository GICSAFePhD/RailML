#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tLineTrafficCodeExt import tLineTrafficCodeExt
from typing import List

class LineTrafficCode(object):
	def setValue(self, aValue : tLineTrafficCodeExt):
		self.___value = aValue

	def getValue(self) -> tLineTrafficCodeExt:
		return self.___value

	def __init__(self):
		self.___value : tLineTrafficCodeExt = None
		# @AssociationType Infrastructure.tLineTrafficCodeExt
		# """TSI category of line as defined in TSI INF section 4.2.1"""

