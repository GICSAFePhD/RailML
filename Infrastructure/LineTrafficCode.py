#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tLineTrafficCodeExt
from typing import List

class LineTrafficCode(object):
	@property
	def tLineTrafficCodeExt(self) -> tLineTrafficCodeExt:
		return self.___value
	
	@tLineTrafficCodeExt.setter
	def tLineTrafficCodeExt(self, atLineTrafficCodeExt : tLineTrafficCodeExt):
		self.___value = atLineTrafficCodeExt

	def __init__(self):
		self.___value : tLineTrafficCodeExt = tLineTrafficCodeExt.tLineTrafficCodeExt()
		# @AssociationType Infrastructure.tLineTrafficCodeExt
		# """TSI category of line as defined in TSI INF section 4.2.1"""

