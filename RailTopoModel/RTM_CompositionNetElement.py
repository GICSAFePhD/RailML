#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_UnorderedCollection, RTM_OrderedCollection, RTM_NetElement
from typing import List

class RTM_CompositionNetElement(RTM_NetElement.RTM_NetElement):
	@property
	def ElementCollectionOrdered(self) -> RTM_OrderedCollection:
		return self.___elementCollectionOrdered
	@property
	def ElementCollectionUnordered(self) -> RTM_UnorderedCollection:
		return self.___elementCollectionUnordered

	@ElementCollectionOrdered.setter
	def ElementCollectionOrdered(self, aElementCollectionOrdered : RTM_OrderedCollection):
		self.___elementCollectionOrdered = aElementCollectionOrdered
	@ElementCollectionUnordered.setter
	def ElementCollectionUnordered(self, aElementCollectionUnordered : RTM_UnorderedCollection):
		self.___elementCollectionUnordered = aElementCollectionUnordered

	def create_ElementCollectionOrdered(self):
		if self.ElementCollectionOrdered == None:
			self.ElementCollectionOrdered = []
		self.ElementCollectionOrdered.append(RTM_OrderedCollection.RTM_OrderedCollection())
	def create_ElementCollectionUnordered(self):
		if self.ElementCollectionUnordered == None:
			self.ElementCollectionUnordered = []
		self.ElementCollectionUnordered.append(RTM_UnorderedCollection.RTM_UnorderedCollection())

	def __init__(self):
		super().__init__()
		self.___elementCollectionUnordered : RTM_UnorderedCollection = None
		# @AssociationType Infrastructure.RTM.RTM_UnorderedCollection*
		# @AssociationMultiplicity 0..*
		self.___elementCollectionOrdered : RTM_OrderedCollection = None
		# @AssociationType Infrastructure.RTM.RTM_OrderedCollection*
		# @AssociationMultiplicity 0..*

