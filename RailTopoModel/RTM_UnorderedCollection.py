#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.RailTopoModel import RTM_ElementPartCollection
from typing import List

class RTM_UnorderedCollection(RTM_ElementPartCollection.RTM_ElementPartCollection):
	def __init__(self):
		self._elementPart : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 1..*

