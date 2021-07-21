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
		self.___topology : Topology = Topology()
		# @AssociationType Infrastructure.Topology
		# @AssociationMultiplicity 0..1
		# """container element for topology model"""
		self.___geometry : Geometry = Geometry()
		# @AssociationType Infrastructure.Geometry
		# @AssociationMultiplicity 0..1
		# """container element for geometry model"""
		self.___functionalInfrastructure : FunctionalInfrastructure = FunctionalInfrastructure()
		# @AssociationType Infrastructure.FunctionalInfrastructure
		# @AssociationMultiplicity 0..1
		# """container element for all railway network's functional infrastructure elements"""
		self.___physicalFacilities : PhysicalFacilities = PhysicalFacilities()
		# @AssociationType Infrastructure.PhysicalFacilities
		# @AssociationMultiplicity 0..1
		# """container element for all physical railway infrastructure facilities"""
		self.___infrastructureVisualizations : InfrastructureVisualizations = InfrastructureVisualizations()
		# @AssociationType Infrastructure.InfrastructureVisualizations
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure visualizations model"""
		self.___infrastructureStates : InfrastructureStates = InfrastructureStates()
		# @AssociationType Infrastructure.InfrastructureStates
		# @AssociationMultiplicity 0..1
		# """container element for infrastructure states model"""

