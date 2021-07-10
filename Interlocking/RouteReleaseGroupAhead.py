#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import PartialRoute
from typing import List

class RouteReleaseGroupAhead(PartialRoute):
	"""A route section is a partial route situated ahead of a train. In order to prevent that a stopped train locks down the remaining route, such a partial route can be released. Condition for release are expiry of a timer and/or an operator command as prescribed by the IM rules and regulations. This is especially used for ERTMS MA sections."""
	def setIsAutomatic(self, aIsAutomatic : long):
		self.___isAutomatic = aIsAutomatic

	def getIsAutomatic(self) -> long:
		return self.___isAutomatic

	def __init__(self):
		self.___isAutomatic : long = None
		"""True if the route is released automatically after expiry of the delay. False otherwise, e.g. operator intervention is required."""
