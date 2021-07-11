#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure.RTM import RTM_AssociatedPositioningSystem
from Infrastructure.RTM import RTM_CompositionNetElement
from typing import List

class RTM_PositioningNetElement(RTM_CompositionNetElement):
	def __init__(self):
		self._associatedPositioningSystem : RTM_AssociatedPositioningSystem = None
		# @AssociationType Infrastructure.RTM.RTM_AssociatedPositioningSystem*
		# @AssociationMultiplicity 1..*

