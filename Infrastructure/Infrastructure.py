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

	def create_Topology(self):
		self.Topology = Topology.Topology()
	def create_Geometry(self):
		self.Geometry = Geometry.Geometry()
	def create_FunctionalInfrastructure(self):
		self.FunctionalInfrastructure = FunctionalInfrastructure.FunctionalInfrastructure()
	def create_PhysicalFacilities(self):
		self.PhysicalFacilities = PhysicalFacilities.PhysicalFacilities()
	def create_InfrastructureVisualizations(self):
		self.InfrastructureVisualizations = InfrastructureVisualizations.InfrastructureVisualizations()
	def create_InfrastructureStates(self):
		self.InfrastructureStates = InfrastructureStates.InfrastructureStates() 

	def __init__(self):
		self.___topology : Topology = None
		# @AssociationType Infrastructure.Topology
		# @AssociationMultiplicity 0..1
		# """container element for topology model"""
		self.___geometry : Geometry = None
		# @AssociationType Infrastructure.Geometry
		# @AssociationMultiplicity 0..1
		# """container element for geometry model"""
		self.___functionalInfrastructure : FunctionalInfrastructure = None
		# @AssociationType Infrastructure.FunctionalInfrastructure
		# @AssociationMultiplicity 0..1
		# """container element for all railway network's functional infrastructure elements"""
		self.___physicalFacilities : PhysicalFacilities = None
		# @AssociationType Infrastructure.PhysicalFacilities
		# @AssociationMultiplicity 0..1
		# """container element for all physical railway infrastructure facilities"""
		self.___infrastructureVisualizations : InfrastructureVisualizations = None
		# @AssociationType Infrastructure.InfrastructureVisualizations
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure visualizations model"""
		self.___infrastructureStates : InfrastructureStates = None
		# @AssociationType Infrastructure.InfrastructureStates
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure states model"""