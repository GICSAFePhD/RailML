#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import ServiceSection
from typing import List, NewType
Long = NewType("Long", int)

class aServiceSection(object):
	@property
	def AllowsCleaning(self) -> Long:
		return self.___allowsCleaning
	@property
	def AllowsFueling(self) -> Long:
		return self.___allowsFueling
	@property
	def AllowsLoading(self) -> Long:
		return self.___allowsLoading
	@property
	def AllowsMaintenance(self) -> Long:
		return self.___allowsMaintenance
	@property
	def AllowsParking(self) -> Long:
		return self.___allowsParking
	@property
	def AllowsPreheating(self) -> Long:
		return self.___allowsPreheating
	@property
	def HasRamp(self) -> Long:
		return self.___hasRamp
	@property
	def AllowsToiletDischarge(self) -> Long:
		return self.___allowsToiletDischarge
	@property
	def AllowsWaterRestocking(self) -> Long:
		return self.___allowsWaterRestocking
	@property
	def AllowsSandRestocking(self) -> Long:
		return self.___allowsSandRestocking
	@property
	def HasElectricSupply(self) -> Long:
		return self.___hasElectricSupply
	@property
	def Unnamed_ServiceSection(self) -> Long:
		return self.___unnamed_ServiceSection_

	@AllowsCleaning.setter
	def AllowsCleaning(self, aAllowsCleaning : Long):
		self.___allowsCleaning = aAllowsCleaning
	@AllowsFueling.setter
	def AllowsFueling(self, aAllowsFueling : Long):
		self.___allowsFueling = aAllowsFueling
	@AllowsLoading.setter
	def AllowsLoading(self, aAllowsLoading : Long):
		self.___allowsLoading = aAllowsLoading
	@AllowsMaintenance.setter
	def AllowsMaintenance(self, aAllowsMaintenance : Long):
		self.___allowsMaintenance = aAllowsMaintenance
	@AllowsParking.setter
	def AllowsParking(self, aAllowsParking : Long):
		self.___allowsParking = aAllowsParking
	@AllowsPreheating.setter
	def AllowsPreheating(self, aAllowsPreheating : Long):
		self.___allowsPreheating = aAllowsPreheating
	@HasRamp.setter
	def HasRamp(self, aHasRamp : Long):
		self.___hasRamp = aHasRamp
	@AllowsToiletDischarge.setter
	def AllowsToiletDischarge(self, aAllowsToiletDischarge : Long):
		self.___allowsToiletDischarge = aAllowsToiletDischarge
	@AllowsWaterRestocking.setter
	def AllowsWaterRestocking(self, aAllowsWaterRestocking : Long):
		self.___allowsWaterRestocking = aAllowsWaterRestocking
	@AllowsSandRestocking.setter
	def AllowsSandRestocking(self, aAllowsSandRestocking : Long):
		self.___allowsSandRestocking = aAllowsSandRestocking
	@HasElectricSupply.setter
	def HasElectricSupply(self, aHasElectricSupply : Long):
		self.___hasElectricSupply = aHasElectricSupply
	@Unnamed_ServiceSection.setter
	def Unnamed_ServiceSection(self, aUnnamed_ServiceSection : Long):
		self.___unnamed_ServiceSection_ = aUnnamed_ServiceSection
	
	def __init__(self):
		self.___allowsCleaning : Long = 0
		"""indicate whether service section is equipped with cleaning facilities"""
		self.___allowsFueling : Long = 0
		"""indicate whether service section is equipped with fueling facilities"""
		self.___allowsLoading : Long = 0
		"""indicate whether service section is equipped with loading facilities"""
		self.___allowsMaintenance : Long = 0
		"""indicate whether service section is equipped with facilities for vehicle maintenance"""
		self.___allowsParking : Long = 0
		"""indicate whether service section allows parking of vehicles"""
		self.___allowsPreheating : Long = 0
		"""indicate whether service section is equipped with preheating facilities"""
		self.___hasRamp : Long = 0
		"""indicate whether service section is equipped with ramps for loading"""
		self.___allowsToiletDischarge : Long = 0
		"""indicate whether service section is equipped with facilities for toilet discharge"""
		self.___allowsWaterRestocking : Long = 0
		"""indicate whether service section is equipped with water restocking facilities"""
		self.___allowsSandRestocking : Long = 0
		"""indicate whether service section is equipped with sand restocking facilities"""
		self.___hasElectricSupply : Long = 0
		"""indicate whether service section is equipped with facilities supplying electricity"""
		self.___unnamed_ServiceSection_ : ServiceSection = ServiceSection.ServiceSection()

