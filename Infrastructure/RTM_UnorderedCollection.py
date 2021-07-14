#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.RTM_ElementPartCollection import RTM_ElementPartCollection
from typing import List

class RTM_UnorderedCollection(RTM_ElementPartCollection):
	def __init__(self):
		self._elementPart : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 1..*

