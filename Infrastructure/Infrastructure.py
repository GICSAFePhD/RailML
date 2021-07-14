#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Topology import Topology
from RailML.Infrastructure.Geometry import Geometry
from RailML.Infrastructure.FunctionalInfrastructure import FunctionalInfrastructure
from RailML.Infrastructure.PhysicalFacilities import PhysicalFacilities
from RailML.Infrastructure.InfrastructureVisualizations import InfrastructureVisualizations
from RailML.Infrastructure.InfrastructureStates import InfrastructureStates
from RailML.Common.tElementWithID import tElementWithID
from typing import List

class Infrastructure(tElementWithID):
	"""This is the top level element for the infrastructure model."""
	def setTopology(self, aTopology : Topology):
		self._topology = aTopology

	def getTopology(self) -> Topology:
		return self._topology

	def setGeometry(self, aGeometry : Geometry):
		self._geometry = aGeometry

	def getGeometry(self) -> Geometry:
		return self._geometry

	def setFunctionalInfrastructure(self, aFunctionalInfrastructure : FunctionalInfrastructure):
		self._functionalInfrastructure = aFunctionalInfrastructure

	def getFunctionalInfrastructure(self) -> FunctionalInfrastructure:
		return self._functionalInfrastructure

	def setPhysicalFacilities(self, aPhysicalFacilities : PhysicalFacilities):
		self._physicalFacilities = aPhysicalFacilities

	def getPhysicalFacilities(self) -> PhysicalFacilities:
		return self._physicalFacilities

	def setInfrastructureVisualizations(self, aInfrastructureVisualizations : InfrastructureVisualizations):
		self._infrastructureVisualizations = aInfrastructureVisualizations

	def getInfrastructureVisualizations(self) -> InfrastructureVisualizations:
		return self._infrastructureVisualizations

	def setInfrastructureStates(self, aInfrastructureStates : InfrastructureStates):
		self._infrastructureStates = aInfrastructureStates

	def getInfrastructureStates(self) -> InfrastructureStates:
		return self._infrastructureStates

	def __init__(self):
		self._topology : Topology = None
		# @AssociationType Infrastructure.Topology
		# @AssociationMultiplicity 0..1
		# """container element for topology model"""
		self._geometry : Geometry = None
		# @AssociationType Infrastructure.Geometry
		# @AssociationMultiplicity 0..1
		# """container element for geometry model"""
		self._functionalInfrastructure : FunctionalInfrastructure = None
		# @AssociationType Infrastructure.FunctionalInfrastructure
		# @AssociationMultiplicity 0..1
		# """container element for all railway network's functional infrastructure elements"""
		self._physicalFacilities : PhysicalFacilities = None
		# @AssociationType Infrastructure.PhysicalFacilities
		# @AssociationMultiplicity 0..1
		# """container element for all physical railway infrastructure facilities"""
		self._infrastructureVisualizations : InfrastructureVisualizations = None
		# @AssociationType Infrastructure.InfrastructureVisualizations
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure visualizations model"""
		self._infrastructureStates : InfrastructureStates = None
		# @AssociationType Infrastructure.InfrastructureStates
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure states model"""

