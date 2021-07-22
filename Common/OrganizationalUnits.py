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

	def __init__(self):
		self.___infrastructureManager : InfrastructureManager = InfrastructureManager.InfrastructureManager()
		# @AssociationType Common.InfrastructureManager*
		# @AssociationMultiplicity 0..*
		self.___vehicleManufacturer : VehicleManufacturer = VehicleManufacturer.VehicleManufacturer()
		# @AssociationType Common.VehicleManufacturer*
		# @AssociationMultiplicity 0..*
		self.___vehicleOperator : VehicleOperator = VehicleOperator.VehicleOperator()
		# @AssociationType Common.VehicleOperator*
		# @AssociationMultiplicity 0..*
		self.___customer : Customer = Customer.Customer()
		# @AssociationType Common.Customer*
		# @AssociationMultiplicity 0..*
		self.___railwayUndertaking : RailwayUndertaking = RailwayUndertaking.RailwayUndertaking()
		# @AssociationType Common.RailwayUndertaking*
		# @AssociationMultiplicity 0..*
		self.___operationalUndertaking : OperationalUndertaking = OperationalUndertaking.OperationalUndertaking()
		# @AssociationType Common.OperationalUndertaking*
		# @AssociationMultiplicity 0..*
		self.___concessionaire : Concessionaire = Concessionaire.Concessionaire()
		# @AssociationType Common.Concessionaire*
		# @AssociationMultiplicity 0..*
		self.___contractor : Contractor = Contractor.Contractor()
		# @AssociationType Common.Contractor*
		# @AssociationMultiplicity 0..*

