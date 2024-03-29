#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import InfrastructureManager, VehicleManufacturer, VehicleOperator, Customer
from RailML.Common import RailwayUndertaking, OperationalUndertaking, Concessionaire, Contractor
from typing import List

class OrganizationalUnits(object):
	"""This is the top level element for various company definitions regarding the railway services referred to in this file"""
	
	@property
	def InfrastructureManager(self) -> InfrastructureManager:
		return self.___infrastructureManager
	@property
	def VehicleManufacturer(self) -> VehicleManufacturer:
		return self.___vehicleManufacturer
	@property
	def VehicleOperator(self) -> VehicleOperator:
		return self.___vehicleOperator
	@property
	def Customer(self) -> Customer:
		return self.___customer
	@property
	def RailwayUndertaking(self) -> RailwayUndertaking:
		return self.___railwayUndertaking
	@property
	def OperationalUndertaking(self) -> OperationalUndertaking:
		return self.___operationalUndertaking
	@property
	def Concessionaire(self) -> Concessionaire:
		return self.___concessionaire
	@property
	def Contractor(self) -> Contractor:
		return self.___contractor

	@InfrastructureManager.setter
	def InfrastructureManager(self, aInfrastructureManager : InfrastructureManager):
		self.___infrastructureManager = aInfrastructureManager
	@VehicleManufacturer.setter
	def VehicleManufacturer(self, aVehicleManufacturer : VehicleManufacturer):
		self.___vehicleManufacturer = aVehicleManufacturer
	@VehicleOperator.setter
	def VehicleOperator(self, aVehicleOperator : VehicleOperator):
		self.___vehicleOperator = aVehicleOperator
	@Customer.setter
	def Customer(self, aCustomer : Customer):
		self.___customer = aCustomer
	@RailwayUndertaking.setter
	def RailwayUndertaking(self, aRailwayUndertaking : RailwayUndertaking):
		self.___railwayUndertaking = aRailwayUndertaking
	@OperationalUndertaking.setter
	def OperationalUndertaking(self, aOperationalUndertaking : OperationalUndertaking):
		self.___operationalUndertaking = aOperationalUndertaking
	@Concessionaire.setter
	def Concessionaire(self, aConcessionaire : Concessionaire):
		self.___concessionaire = aConcessionaire
	@Contractor.setter
	def Contractor(self, aContractor : Contractor):
		self.___contractor = aContractor

	def create_InfrastructureManager(self):
		if self.InfrastructureManager == None:
			self.InfrastructureManager = []
		self.InfrastructureManager.append(InfrastructureManager.InfrastructureManager())
	def create_VehicleManufacturer(self):
		if self.VehicleManufacturer == None:
			self.VehicleManufacturer = []
		self.VehicleManufacturer.append(VehicleManufacturer.VehicleManufacturer())
	def create_VehicleOperator(self):
		if self.VehicleOperator == None:
			self.VehicleOperator = []
		self.VehicleOperator.append(VehicleOperator.VehicleOperator())
	def create_Customer(self):
		if self.Customer == None:
			self.Customer = []
		self.Customer.append(Customer.Customer())
	def create_RailwayUndertaking(self):
		if self.RailwayUndertaking == None:
			self.RailwayUndertaking = []
		self.RailwayUndertaking.append(RailwayUndertaking.RailwayUndertaking())
	def create_OperationalUndertaking(self):
		if self.OperationalUndertaking == None:
			self.OperationalUndertaking = []
		self.OperationalUndertaking.append(OperationalUndertaking.OperationalUndertaking())
	def create_Concessionaire(self):
		if self.Concessionaire == None:
			self.Concessionaire = []
		self.Concessionaire.append(Concessionaire.Concessionaire())
	def create_Contractor(self):
		if self.Contractor == None:
			self.Contractor = []
		self.Contractor.append(Contractor.Contractor())

	def __init__(self):
		self.___infrastructureManager : InfrastructureManager = None
		# @AssociationType Common.InfrastructureManager*
		# @AssociationMultiplicity 0..*
		self.___vehicleManufacturer : VehicleManufacturer = None
		# @AssociationType Common.VehicleManufacturer*
		# @AssociationMultiplicity 0..*
		self.___vehicleOperator : VehicleOperator = None
		# @AssociationType Common.VehicleOperator*
		# @AssociationMultiplicity 0..*
		self.___customer : Customer = None
		# @AssociationType Common.Customer*
		# @AssociationMultiplicity 0..*
		self.___railwayUndertaking : RailwayUndertaking = None
		# @AssociationType Common.RailwayUndertaking*
		# @AssociationMultiplicity 0..*
		self.___operationalUndertaking : OperationalUndertaking = None
		# @AssociationType Common.OperationalUndertaking*
		# @AssociationMultiplicity 0..*
		self.___concessionaire : Concessionaire = None
		# @AssociationType Common.Concessionaire*
		# @AssociationMultiplicity 0..*
		self.___contractor : Contractor = None
		# @AssociationType Common.Contractor*
		# @AssociationMultiplicity 0..*

