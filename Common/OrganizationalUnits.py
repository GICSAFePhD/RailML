#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.InfrastructureManager import InfrastructureManager
from RailML.Common.VehicleManufacturer import VehicleManufacturer
from RailML.Common.VehicleOperator import VehicleOperator
from RailML.Common.Customer import Customer
from RailML.Common.RailwayUndertaking import RailwayUndertaking
from RailML.Common.OperationalUndertaking import OperationalUndertaking
from RailML.Common.Concessionaire import Concessionaire
from RailML.Common.Contractor import Contractor
from typing import List

class OrganizationalUnits(object):
	"""This is the top level element for various company definitions regarding the railway services referred to in this file"""
	def setInfrastructureManager(self, *aInfrastructureManager : InfrastructureManager):
		self._infrastructureManager = aInfrastructureManager

	def getInfrastructureManager(self) -> InfrastructureManager:
		return self._infrastructureManager

	def setVehicleManufacturer(self, *aVehicleManufacturer : VehicleManufacturer):
		self._vehicleManufacturer = aVehicleManufacturer

	def getVehicleManufacturer(self) -> VehicleManufacturer:
		return self._vehicleManufacturer

	def setVehicleOperator(self, *aVehicleOperator : VehicleOperator):
		self._vehicleOperator = aVehicleOperator

	def getVehicleOperator(self) -> VehicleOperator:
		return self._vehicleOperator

	def setCustomer(self, *aCustomer : Customer):
		self._customer = aCustomer

	def getCustomer(self) -> Customer:
		return self._customer

	def setRailwayUndertaking(self, *aRailwayUndertaking : RailwayUndertaking):
		self._railwayUndertaking = aRailwayUndertaking

	def getRailwayUndertaking(self) -> RailwayUndertaking:
		return self._railwayUndertaking

	def setOperationalUndertaking(self, *aOperationalUndertaking : OperationalUndertaking):
		self._operationalUndertaking = aOperationalUndertaking

	def getOperationalUndertaking(self) -> OperationalUndertaking:
		return self._operationalUndertaking

	def setConcessionaire(self, *aConcessionaire : Concessionaire):
		self._concessionaire = aConcessionaire

	def getConcessionaire(self) -> Concessionaire:
		return self._concessionaire

	def setContractor(self, *aContractor : Contractor):
		self._contractor = aContractor

	def getContractor(self) -> Contractor:
		return self._contractor

	def __init__(self):
		self._infrastructureManager : InfrastructureManager = None
		# @AssociationType Common.InfrastructureManager*
		# @AssociationMultiplicity 0..*
		self._vehicleManufacturer : VehicleManufacturer = None
		# @AssociationType Common.VehicleManufacturer*
		# @AssociationMultiplicity 0..*
		self._vehicleOperator : VehicleOperator = None
		# @AssociationType Common.VehicleOperator*
		# @AssociationMultiplicity 0..*
		self._customer : Customer = None
		# @AssociationType Common.Customer*
		# @AssociationMultiplicity 0..*
		self._railwayUndertaking : RailwayUndertaking = None
		# @AssociationType Common.RailwayUndertaking*
		# @AssociationMultiplicity 0..*
		self._operationalUndertaking : OperationalUndertaking = None
		# @AssociationType Common.OperationalUndertaking*
		# @AssociationMultiplicity 0..*
		self._concessionaire : Concessionaire = None
		# @AssociationType Common.Concessionaire*
		# @AssociationMultiplicity 0..*
		self._contractor : Contractor = None
		# @AssociationType Common.Contractor*
		# @AssociationMultiplicity 0..*

