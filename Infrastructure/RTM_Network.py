#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Infrastructure.RTM import RTM_LevelNetwork
from Infrastructure.RTM import RTM_NetworkResource
from Infrastructure.RTM import RTM_NamedResource
from typing import List

class RTM_Network(RTM_NamedResource):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self._level : RTM_LevelNetwork = None
		# @AssociationType Infrastructure.RTM.RTM_LevelNetwork*
		# @AssociationMultiplicity 1..*
		self._networkResource : RTM_NetworkResource = None
		# @AssociationType Infrastructure.RTM.RTM_NetworkResource*
		# @AssociationMultiplicity 0..*

