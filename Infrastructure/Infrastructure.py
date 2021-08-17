#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithID
from RailML.Infrastructure import Topology, Geometry, FunctionalInfrastructure, PhysicalFacilities
from RailML.Infrastructure import InfrastructureVisualizations, InfrastructureStates

from typing import List

class Infrastructure(tElementWithID.tElementWithID):
	"""This is the top level element for the infrastructure model."""
	@property
	def Topology(self) -> Topology:
		return self.___topology
	@property
	def Geometry(self) -> Geometry:
		return self.___geometry
	@property
	def FunctionalInfrastructure(self) -> FunctionalInfrastructure:
		return self.___functionalInfrastructure
	@property
	def PhysicalFacilities(self) -> PhysicalFacilities:
		return self.___physicalFacilities
	@property
	def InfrastructureVisualizations(self) -> InfrastructureVisualizations:
		return self.___infrastructureVisualizations
	@property
	def InfrastructureStates(self) -> InfrastructureStates:
		return self.___infrastructureStates
	
	@Topology.setter
	def Topology(self, aTopology : Topology):
		self.___topology = aTopology
	@Geometry.setter
	def Geometry(self, aGeometry : Geometry):
		self.___geometry = aGeometry
	@FunctionalInfrastructure.setter
	def FunctionalInfrastructure(self, aFunctionalInfrastructure : FunctionalInfrastructure):
		self.___functionalInfrastructure = aFunctionalInfrastructure	
	@PhysicalFacilities.setter
	def PhysicalFacilities(self, aPhysicalFacilities : PhysicalFacilities):
		self.___physicalFacilities = aPhysicalFacilities	
	@InfrastructureVisualizations.setter
	def InfrastructureVisualizations(self, aInfrastructureVisualizations : InfrastructureVisualizations):
		self.___infrastructureVisualizations = aInfrastructureVisualizations
	@InfrastructureStates.setter
	def InfrastructureStates(self, aInfrastructureStates : InfrastructureStates):
		self.___infrastructureStates = aInfrastructureStates

	def __init__(self):
		self.___topology : Topology = None#Topology.Topology()
		# @AssociationType Infrastructure.Topology
		# @AssociationMultiplicity 0..1
		# """container element for topology model"""
		self.___geometry : Geometry = None#Geometry.Geometry()
		# @AssociationType Infrastructure.Geometry
		# @AssociationMultiplicity 0..1
		# """container element for geometry model"""
		self.___functionalInfrastructure : FunctionalInfrastructure = None#FunctionalInfrastructure.FunctionalInfrastructure()
		# @AssociationType Infrastructure.FunctionalInfrastructure
		# @AssociationMultiplicity 0..1
		# """container element for all railway network's functional infrastructure elements"""
		self.___physicalFacilities : PhysicalFacilities = None#PhysicalFacilities.PhysicalFacilities()
		# @AssociationType Infrastructure.PhysicalFacilities
		# @AssociationMultiplicity 0..1
		# """container element for all physical railway infrastructure facilities"""
		self.___infrastructureVisualizations : InfrastructureVisualizations = None#InfrastructureVisualizations.InfrastructureVisualizations()
		# @AssociationType Infrastructure.InfrastructureVisualizations
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure visualizations model"""
		self.___infrastructureStates : InfrastructureStates = None#InfrastructureStates.InfrastructureStates()
		# @AssociationType Infrastructure.InfrastructureStates
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure states model"""

