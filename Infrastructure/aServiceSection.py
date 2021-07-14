#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from RailML.Infrastructure.ServiceSection import ServiceSection	#TODO CIRCULAR!
from typing import List

class aServiceSection(object):
	def setAllowsCleaning(self, aAllowsCleaning : int):	#TODO DEFINES AS LONG
		self.___allowsCleaning = aAllowsCleaning

	def getAllowsCleaning(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsCleaning

	def setAllowsFueling(self, aAllowsFueling : int):	#TODO DEFINES AS LONG
		self.___allowsFueling = aAllowsFueling

	def getAllowsFueling(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsFueling

	def setAllowsLoading(self, aAllowsLoading : int):	#TODO DEFINES AS LONG
		self.___allowsLoading = aAllowsLoading

	def getAllowsLoading(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsLoading

	def setAllowsMaintenance(self, aAllowsMaintenance : int):	#TODO DEFINES AS LONG
		self.___allowsMaintenance = aAllowsMaintenance

	def getAllowsMaintenance(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsMaintenance

	def setAllowsParking(self, aAllowsParking : int):	#TODO DEFINES AS LONG
		self.___allowsParking = aAllowsParking

	def getAllowsParking(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsParking

	def setAllowsPreheating(self, aAllowsPreheating : int):	#TODO DEFINES AS LONG
		self.___allowsPreheating = aAllowsPreheating

	def getAllowsPreheating(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsPreheating

	def setHasRamp(self, aHasRamp : int):	#TODO DEFINES AS LONG
		self.___hasRamp = aHasRamp

	def getHasRamp(self) -> int:	#TODO DEFINES AS LONG
		return self.___hasRamp

	def setAllowsToiletDischarge(self, aAllowsToiletDischarge : int):	#TODO DEFINES AS LONG
		self.___allowsToiletDischarge = aAllowsToiletDischarge

	def getAllowsToiletDischarge(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsToiletDischarge

	def setAllowsWaterRestocking(self, aAllowsWaterRestocking : int):	#TODO DEFINES AS LONG
		self.___allowsWaterRestocking = aAllowsWaterRestocking

	def getAllowsWaterRestocking(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsWaterRestocking

	def setAllowsSandRestocking(self, aAllowsSandRestocking : int):	#TODO DEFINES AS LONG
		self.___allowsSandRestocking = aAllowsSandRestocking

	def getAllowsSandRestocking(self) -> int:	#TODO DEFINES AS LONG
		return self.___allowsSandRestocking

	def setHasElectricSupply(self, aHasElectricSupply : int):	#TODO DEFINES AS LONG
		self.___hasElectricSupply = aHasElectricSupply

	def getHasElectricSupply(self) -> int:	#TODO DEFINES AS LONG
		return self.___hasElectricSupply

	def __init__(self):
		self.___allowsCleaning : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with cleaning facilities"""
		self.___allowsFueling : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with fueling facilities"""
		self.___allowsLoading : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with loading facilities"""
		self.___allowsMaintenance : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with facilities for vehicle maintenance"""
		self.___allowsParking : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section allows parking of vehicles"""
		self.___allowsPreheating : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with preheating facilities"""
		self.___hasRamp : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with ramps for loading"""
		self.___allowsToiletDischarge : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with facilities for toilet discharge"""
		self.___allowsWaterRestocking : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with water restocking facilities"""
		self.___allowsSandRestocking : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with sand restocking facilities"""
		self.___hasElectricSupply : int = None	#TODO DEFINES AS LONG
		"""indicate whether service section is equipped with facilities supplying electricity"""
		#self._unnamed_ServiceSection_ : ServiceSection = None	#TODO CIRCULAR!

