#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_UnorderedCollection, RTM_OrderedCollection, RTM_NetElement
from typing import List

class RTM_CompositionNetElement(RTM_NetElement.RTM_NetElement):
	def __init__(self):
		self._elementCollectionUnordered : RTM_UnorderedCollection = None
		# @AssociationType Infrastructure.RTM.RTM_UnorderedCollection*
		# @AssociationMultiplicity 0..*
		self._elementCollectionOrdered : RTM_OrderedCollection = None
		# @AssociationType Infrastructure.RTM.RTM_OrderedCollection*
		# @AssociationMultiplicity 0..*

