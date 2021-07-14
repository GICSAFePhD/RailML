#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tNavigability import tNavigability
from RailML.Infrastructure.tUsage import tUsage
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.RTM_NetworkResource import RTM_NetworkResource
from typing import List

class RTM_Relation(RTM_NetworkResource):
	def __init__(self):
		self.___navigability : tNavigability = None
		# @AssociationType schemas.3.1.tNavigability
		self.___positionOnA : tUsage = None
		self.___positionOnB : tUsage = None
		# @AssociationType schemas.3.1.tUsage
		# @AssociationType schemas.3.1.tUsage
		self._elementA : tElementWithIDref = None
		self._elementB : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 1
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 1

