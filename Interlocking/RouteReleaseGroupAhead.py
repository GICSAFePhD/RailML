#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import PartialRoute
from typing import List, NewType

Long = NewType("Long", int)

class RouteReleaseGroupAhead(PartialRoute.PartialRoute):
	"""A route section is a partial route situated ahead of a train. In order to prevent that a stopped train locks down the remaining route, such a partial route can be released. Condition for release are expiry of a timer and/or an operator command as prescribed by the IM rules and regulations. This is especially used for ERTMS MA sections."""
	@property
	def IsAutomatic(self) -> Long:
		return self.___isAutomatic
	
	@IsAutomatic.setter
	def IsAutomatic(self, aIsAutomatic : Long):
		self.___isAutomatic = aIsAutomatic

	def __init__(self):
		self.___isAutomatic : Long = 0
		"""True if the route is released automatically after expiry of the delay. False otherwise, e.g. operator intervention is required."""

