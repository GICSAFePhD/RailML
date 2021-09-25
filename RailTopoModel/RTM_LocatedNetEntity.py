#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_AreaLocation, RTM_LinearLocation, RTM_SpotLocation, RTM_NetEntity
from typing import List

class RTM_LocatedNetEntity(RTM_NetEntity.RTM_NetEntity):
	@property
	def AreaLocation(self) -> RTM_AreaLocation:
		return self.___areaLocation
	@property
	def LinearLocation(self) -> RTM_LinearLocation:
		return self.___linearLocation
	@property
	def SpotLocation(self) -> RTM_SpotLocation:
		return self.___spotLocation

	@AreaLocation.setter
	def AreaLocation(self, aAreaLocation : RTM_AreaLocation):
		self.___areaLocation = aAreaLocation
	@LinearLocation.setter
	def LinearLocation(self, aLinearLocation : RTM_LinearLocation):
		self.___linearLocation = aLinearLocation
	@SpotLocation.setter
	def SpotLocation(self, aSpotLocation : RTM_SpotLocation):
		self.___spotLocation = aSpotLocation

	def create_AreaLocation(self):
		if self.AreaLocation == None:
			self.AreaLocation = []
		self.AreaLocation.append(RTM_AreaLocation.RTM_AreaLocation())
	def create_LinearLocation(self):
		if self.LinearLocation == None:
			self.LinearLocation = []
		self.LinearLocation.append(RTM_LinearLocation.RTM_LinearLocation())
	def create_SpotLocation(self):
		if self.SpotLocation == None:
			self.SpotLocation = []
		self.SpotLocation.append(RTM_SpotLocation.RTM_SpotLocation())

	def __init__(self):
		super().__init__()
		self.___areaLocation : RTM_AreaLocation = None
		# @AssociationType Infrastructure.RTM.RTM_AreaLocation*
		# @AssociationMultiplicity 0..*
		self.___linearLocation : RTM_LinearLocation = None
		# @AssociationType Infrastructure.RTM.RTM_LinearLocation*
		# @AssociationMultiplicity 0..*
		self.___spotLocation : RTM_SpotLocation = None
		# @AssociationType Infrastructure.RTM.RTM_SpotLocation*
		# @AssociationMultiplicity 0..*