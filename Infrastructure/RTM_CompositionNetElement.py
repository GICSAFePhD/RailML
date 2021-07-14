#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.RTM_UnorderedCollection import RTM_UnorderedCollection
from RailML.Infrastructure.RTM_OrderedCollection import RTM_OrderedCollection
from RailML.Infrastructure.RTM_NetElement import RTM_NetElement
from typing import List

class RTM_CompositionNetElement(RTM_NetElement):
	def __init__(self):
		self._elementCollectionUnordered : RTM_UnorderedCollection = None
		# @AssociationType Infrastructure.RTM.RTM_UnorderedCollection*
		# @AssociationMultiplicity 0..*
		self._elementCollectionOrdered : RTM_OrderedCollection = None
		# @AssociationType Infrastructure.RTM.RTM_OrderedCollection*
		# @AssociationMultiplicity 0..*

