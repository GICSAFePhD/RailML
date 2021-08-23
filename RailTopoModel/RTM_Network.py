#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.RailTopoModel import RTM_LevelNetwork, RTM_NetworkResource, RTM_NamedResource
from typing import List

class RTM_Network(RTM_NamedResource.RTM_NamedResource):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self._level : RTM_LevelNetwork = None
		# @AssociationType Infrastructure.RTM.RTM_LevelNetwork*
		# @AssociationMultiplicity 1..*
		self._networkResource : RTM_NetworkResource = None
		# @AssociationType Infrastructure.RTM.RTM_NetworkResource*
		# @AssociationMultiplicity 0..*

