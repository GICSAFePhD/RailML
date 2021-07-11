#!/usr/bin/python
# -*- coding: UTF-8 -*-
from schemas.3.1 import tNavigability
from schemas.3.1 import tUsage
from Common import tElementWithIDref
from Infrastructure.RTM import RTM_NetworkResource
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

