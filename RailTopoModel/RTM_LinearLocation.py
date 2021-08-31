#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tApplicationDirection
from RailML.RailTopoModel import RTM_AssociatedNetElement, RTM_LinearCoordinate, RTM_GeometricCoordinate, RTM_EntityLocation
from typing import List

class RTM_LinearLocation(RTM_EntityLocation.RTM_EntityLocation):
	@property
	def ApplicationDirection(self) -> tApplicationDirection:
		return self.___applicationDirection
	@property
	def AssociatedNetElement(self) -> RTM_AssociatedNetElement:
		return self.___associatedNetElement
	@property
	def LinearCoordinate(self) -> RTM_LinearCoordinate:
		return self.___linearCoordinate
	@property
	def GeometricCoordinate(self) -> RTM_GeometricCoordinate:
		return self.___geometricCoordinate

	@ApplicationDirection.setter
	def ApplicationDirection(self, aApplicationDirection : tApplicationDirection):
		self.___applicationDirection = aApplicationDirection
	@AssociatedNetElement.setter
	def AssociatedNetElement(self, aAssociatedNetElement : RTM_AssociatedNetElement):
		self.___associatedNetElement = aAssociatedNetElement
	@LinearCoordinate.setter
	def LinearCoordinate(self, aLinearCoordinate : RTM_LinearCoordinate):
		self.___linearCoordinate = aLinearCoordinate
	@GeometricCoordinate.setter
	def GeometricCoordinate(self, aGeometricCoordinate : RTM_GeometricCoordinate):
		self.___geometricCoordinate = aGeometricCoordinate

	def create_AssociatedNetElement(self):
		if self.AssociatedNetElement == None:
			self.AssociatedNetElement = []
		self.AssociatedNetElement.append(RTM_AssociatedNetElement.RTM_AssociatedNetElement())
	def create_LinearCoordinate(self):
		if self.LinearCoordinate == None:
			self.LinearCoordinate = []
		self.LinearCoordinate.append(RTM_LinearCoordinate.RTM_LinearCoordinate())
	def create_GeometricCoordinate(self):
		if self.GeometricCoordinate == None:
			self.GeometricCoordinate = []
		self.GeometricCoordinate.append(RTM_GeometricCoordinate.RTM_GeometricCoordinate())

	def __init__(self):
		super().__init__()
		self.___applicationDirection : tApplicationDirection = None
		# @AssociationType schemas.3.1.tApplicationDirection
		# """direction in which the element is applied, related to the orientation of the <netElement>"""
		self.___associatedNetElement : RTM_AssociatedNetElement = None
		# @AssociationType Infrastructure.RTM.RTM_AssociatedNetElement*
		# @AssociationMultiplicity 1..*
		self.___linearCoordinate : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate*
		# @AssociationMultiplicity 0..*
		self.___geometricCoordinate : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate*
		# @AssociationMultiplicity 0..*