#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tContactLineType import tContactLineType
from RailML.Common.tRef import tRef
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.EnergyCatenary import EnergyCatenary
from RailML.Infrastructure.EnergyPantograph import EnergyPantograph
from RailML.Infrastructure.EnergyRollingstock import EnergyRollingstock
from RailML.Infrastructure.ContactWire import ContactWire
from RailML.Infrastructure.PantographSpacing import PantographSpacing
from RailML.Infrastructure.PhaseSeparationSection import PhaseSeparationSection
from RailML.Infrastructure.SystemSeparationSection import SystemSeparationSection
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class ElectrificationSection(FunctionalInfrastructureEntity):
	def setContactLineType(self, aContactLineType : tContactLineType):
		self.___contactLineType = aContactLineType

	def getContactLineType(self) -> tContactLineType:
		return self.___contactLineType

	def setIsInsulatedSection(self, aIsInsulatedSection : int): #TODO DEFINED AS LONG
		self.___isInsulatedSection = aIsInsulatedSection

	def getIsInsulatedSection(self) -> int: #TODO DEFINED AS LONG
		return self.___isInsulatedSection

	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setElectrificationSystemRef(self, aElectrificationSystemRef : tElementWithIDref):
		self._electrificationSystemRef = aElectrificationSystemRef

	def getElectrificationSystemRef(self) -> tElementWithIDref:
		return self._electrificationSystemRef

	def setEnergyCatenary(self, aEnergyCatenary : EnergyCatenary):
		self._energyCatenary = aEnergyCatenary

	def getEnergyCatenary(self) -> EnergyCatenary:
		return self._energyCatenary

	def setEnergyPantograph(self, aEnergyPantograph : EnergyPantograph):
		self._energyPantograph = aEnergyPantograph

	def getEnergyPantograph(self) -> EnergyPantograph:
		return self._energyPantograph

	def setEnergyRollingstock(self, aEnergyRollingstock : EnergyRollingstock):
		self._energyRollingstock = aEnergyRollingstock

	def getEnergyRollingstock(self) -> EnergyRollingstock:
		return self._energyRollingstock

	def setHasContactWire(self, aHasContactWire : ContactWire):
		self._hasContactWire = aHasContactWire

	def getHasContactWire(self) -> ContactWire:
		return self._hasContactWire

	def setPantographSpacing(self, *aPantographSpacing : PantographSpacing):
		self._pantographSpacing = aPantographSpacing

	def getPantographSpacing(self) -> PantographSpacing:
		return self._pantographSpacing

	def setPhaseSeparationSection(self, *aPhaseSeparationSection : PhaseSeparationSection):
		self._phaseSeparationSection = aPhaseSeparationSection

	def getPhaseSeparationSection(self) -> PhaseSeparationSection:
		return self._phaseSeparationSection

	def setSystemSeparationSection(self, *aSystemSeparationSection : SystemSeparationSection):
		self._systemSeparationSection = aSystemSeparationSection

	def getSystemSeparationSection(self) -> SystemSeparationSection:
		return self._systemSeparationSection

	def __init__(self):
		self.___contactLineType : tContactLineType = None
		# @AssociationType Infrastructure.tContactLineType
		# """type of the installed contact line (most common: overhead)"""
		self.___isInsulatedSection : int = None #TODO DEFINED AS LONG
		"""set true if the described electrification section is an insulated section"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to the (one and only) parent electrification section"""
		self._electrificationSystemRef : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the electrification system"""
		self._energyCatenary : EnergyCatenary = None
		# @AssociationType Infrastructure.EnergyCatenary
		# @AssociationMultiplicity 0..1
		# """child element summarizing the catenary energy parameters"""
		self._energyPantograph : EnergyPantograph = None
		# @AssociationType Infrastructure.EnergyPantograph
		# @AssociationMultiplicity 0..1
		# """child element summarizing the pantograph energy parameters"""
		self._energyRollingstock : EnergyRollingstock = None
		# @AssociationType Infrastructure.EnergyRollingstock
		# @AssociationMultiplicity 0..1
		# """child element summarizing the rollingstock energy parameters"""
		self._hasContactWire : ContactWire = None
		# @AssociationType Infrastructure.ContactWire
		# @AssociationMultiplicity 0..1
		# """child element summarizing the construction details of the contact wire"""
		self._pantographSpacing : PantographSpacing = None
		# @AssociationType Infrastructure.PantographSpacing*
		# @AssociationMultiplicity 0..*
		# """child element summarizing the pantograph spacing parameters"""
		self._phaseSeparationSection : PhaseSeparationSection = None
		# @AssociationType Infrastructure.PhaseSeparationSection*
		# @AssociationMultiplicity 0..*
		# """child element summarizing the phase separation parameters"""
		self._systemSeparationSection : SystemSeparationSection = None
		# @AssociationType Infrastructure.SystemSeparationSection*
		# @AssociationMultiplicity 0..*
		# """child element summarizing the electrification system separation parameters"""

