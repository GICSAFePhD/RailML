#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.RTM_NetworkResource import RTM_NetworkResource
from typing import List

class RTM_NetElement(RTM_NetworkResource):
	def __init__(self):
		self._relation : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

