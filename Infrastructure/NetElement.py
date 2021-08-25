#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('.')
from RailML.Common import tLengthM,Name
from RailML.Infrastructure import Validity
from RailML.RailTopoModel import RTM_AssociatedNetElement, RTM_OrderedCollection, RTM_UnorderedCollection, RTM_PositioningNetElement, RTM_Relation
from typing import List

class NetElement(RTM_PositioningNetElement.RTM_PositioningNetElement):
	"""The NetElement type is derived from the RailTopoModel class PositioningNetElement."""
	@property
	def tLengthM(self) -> tLengthM:
		return self.___length
	@property
	def AssociatedPositioningSystem(self) -> RTM_AssociatedNetElement:
		return self.___associatedPositioningSystem
	@property
	def ElementCollectionOrdered(self) -> RTM_OrderedCollection:
		return self.___elementCollectionOrdered
	@property
	def ElementCollectionUnordered(self) -> RTM_UnorderedCollection:
		return self.___elementCollectionUnordered
	@property
	def IsValid(self) -> Validity:
		return self.___isValid
	@property
	def Name(self) -> Name:
		return self.___name
	@property
	def Relation(self) -> RTM_Relation:
		return self.___relation

	@tLengthM.setter
	def tLengthM(self, atLengthM : tLengthM):
		self.___length = atLengthM
	@AssociatedPositioningSystem.setter
	def AssociatedPositioningSystem(self, aAssociatedPositioningSystem : RTM_AssociatedNetElement):
		self.___associatedPositioningSystem = aAssociatedPositioningSystem
	@ElementCollectionOrdered.setter
	def ElementCollectionOrdered(self, aElementCollectionOrdered : RTM_OrderedCollection):
		self.___elementCollectionOrdered = aElementCollectionOrdered
	@ElementCollectionUnordered.setter
	def ElementCollectionUnordered(self, aElementCollectionUnordered : RTM_UnorderedCollection):
		self.___elementCollectionUnordered = aElementCollectionUnordered
	@IsValid.setter
	def IsValid(self, aIsValid : Validity):
		self.___isValid = aIsValid
	@Name.setter
	def Name(self, aName : Name):
		self.___name = aName
	@Relation.setter
	def Relation(self, aRelation : RTM_Relation):
		self.___relation = aRelation

	def create_tLengthM(self):
		self.tLengthM = tLengthM.tLengthM()
	def create_AssociatedPositioningSystem(self):
		if self.AssociatedPositioningSystem == None:
			self.AssociatedPositioningSystem = []
		self.AssociatedPositioningSystem.append(RTM_AssociatedNetElement.RTM_AssociatedNetElement())
	def create_ElementCollectionOrdered(self):
		if self.ElementCollectionOrdered == None:
			self.ElementCollectionOrdered = []
		self.ElementCollectionOrdered.append(RTM_OrderedCollection.RTM_OrderedCollection())
	def create_ElementCollectionUnordered(self):
		if self.ElementCollectionUnordered == None:
			self.ElementCollectionUnordered = []
		self.ElementCollectionUnordered.append(RTM_UnorderedCollection.RTM_UnorderedCollection())
	def create_IsValid(self):
		if self.IsValid == None:
			self.IsValid = []
		self.IsValid.append(Validity.Validity())
	def create_Name(self):
		if self.Name == None:
			self.Name = []
		self.Name.append(Name.Name())
	def create_Relation(self):
		if self.Relation == None:
			self.Relation = []
		self.Relation.append(RTM_Relation.RTM_Relation())

	def __init__(self):
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# """length of the NetElement in metres"""
		self.___associatedPositioningSystem : RTM_AssociatedNetElement = None
		# @AssociationMultiplicity 1..*
		self.___elementCollectionOrdered : RTM_OrderedCollection = None
		# @AssociationMultiplicity 0..*
		self.___elementCollectionUnordered : RTM_UnorderedCollection = None
		# @AssociationMultiplicity 0..*
		self.___isValid : Validity = None
		# @AssociationMultiplicity 0..*
		self.___name : Name = None
		# @AssociationMultiplicity 0..*
		self.___relation : RTM_Relation = None
		# @AssociationMultiplicity 0..*