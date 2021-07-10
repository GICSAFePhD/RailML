#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import ServiceSection
from typing import List

class aServiceSection(object):
	def setAllowsCleaning(self, aAllowsCleaning : long):
		self.___allowsCleaning = aAllowsCleaning

	def getAllowsCleaning(self) -> long:
		return self.___allowsCleaning

	def setAllowsFueling(self, aAllowsFueling : long):
		self.___allowsFueling = aAllowsFueling

	def getAllowsFueling(self) -> long:
		return self.___allowsFueling

	def setAllowsLoading(self, aAllowsLoading : long):
		self.___allowsLoading = aAllowsLoading

	def getAllowsLoading(self) -> long:
		return self.___allowsLoading

	def setAllowsMaintenance(self, aAllowsMaintenance : long):
		self.___allowsMaintenance = aAllowsMaintenance

	def getAllowsMaintenance(self) -> long:
		return self.___allowsMaintenance

	def setAllowsParking(self, aAllowsParking : long):
		self.___allowsParking = aAllowsParking

	def getAllowsParking(self) -> long:
		return self.___allowsParking

	def setAllowsPreheating(self, aAllowsPreheating : long):
		self.___allowsPreheating = aAllowsPreheating

	def getAllowsPreheating(self) -> long:
		return self.___allowsPreheating

	def setHasRamp(self, aHasRamp : long):
		self.___hasRamp = aHasRamp

	def getHasRamp(self) -> long:
		return self.___hasRamp

	def setAllowsToiletDischarge(self, aAllowsToiletDischarge : long):
		self.___allowsToiletDischarge = aAllowsToiletDischarge

	def getAllowsToiletDischarge(self) -> long:
		return self.___allowsToiletDischarge

	def setAllowsWaterRestocking(self, aAllowsWaterRestocking : long):
		self.___allowsWaterRestocking = aAllowsWaterRestocking

	def getAllowsWaterRestocking(self) -> long:
		return self.___allowsWaterRestocking

	def setAllowsSandRestocking(self, aAllowsSandRestocking : long):
		self.___allowsSandRestocking = aAllowsSandRestocking

	def getAllowsSandRestocking(self) -> long:
		return self.___allowsSandRestocking

	def setHasElectricSupply(self, aHasElectricSupply : long):
		self.___hasElectricSupply = aHasElectricSupply

	def getHasElectricSupply(self) -> long:
		return self.___hasElectricSupply

	def __init__(self):
		self.___allowsCleaning : long = None
		"""indicate whether service section is equipped with cleaning facilities"""
		self.___allowsFueling : long = None
		"""indicate whether service section is equipped with fueling facilities"""
		self.___allowsLoading : long = None
		"""indicate whether service section is equipped with loading facilities"""
		self.___allowsMaintenance : long = None
		"""indicate whether service section is equipped with facilities for vehicle maintenance"""
		self.___allowsParking : long = None
		"""indicate whether service section allows parking of vehicles"""
		self.___allowsPreheating : long = None
		"""indicate whether service section is equipped with preheating facilities"""
		self.___hasRamp : long = None
		"""indicate whether service section is equipped with ramps for loading"""
		self.___allowsToiletDischarge : long = None
		"""indicate whether service section is equipped with facilities for toilet discharge"""
		self.___allowsWaterRestocking : long = None
		"""indicate whether service section is equipped with water restocking facilities"""
		self.___allowsSandRestocking : long = None
		"""indicate whether service section is equipped with sand restocking facilities"""
		self.___hasElectricSupply : long = None
		"""indicate whether service section is equipped with facilities supplying electricity"""
		self._unnamed_ServiceSection_ : ServiceSection = None

