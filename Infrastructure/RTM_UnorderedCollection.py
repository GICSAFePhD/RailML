#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tElementWithIDref
from Infrastructure.RTM import RTM_ElementPartCollection
from typing import List

class RTM_UnorderedCollection(RTM_ElementPartCollection):
	def __init__(self):
		self._elementPart : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 1..*

