#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import tContactLineType, EnergyCatenary, EnergyPantograph, EnergyRollingstock, ContactWire
from RailML.Infrastructure import PantographSpacing, PhaseSeparationSection, SystemSeparationSection, FunctionalInfrastructureEntity

from typing import List

class ElectrificationSection(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def ContactLineType(self) -> tContactLineType:
		return self.___contactLineType
	@property
	def IsInsulatedSection(self) -> bool:
		return self.___isInsulatedSection
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def ElectrificationSystemRef(self) -> tElementWithIDref:
		return self.___electrificationSystemRef
	@property
	def EnergyCatenary(self) -> EnergyCatenary:
		return self.___energyCatenary
	@property
	def EnergyPantograph(self) -> EnergyPantograph:
		return self.___energyPantograph
	@property
	def EnergyRollingstock(self) -> EnergyRollingstock:
		return self.___energyRollingstock
	@property
	def ContactWire(self) -> ContactWire:
		return self.___hasContactWire
	@property
	def PantographSpacing(self) -> PantographSpacing:
		return self.___pantographSpacing
	@property
	def PhaseSeparationSection(self) -> PhaseSeparationSection:
		return self.___phaseSeparationSection
	@property
	def SystemSeparationSection(self) -> SystemSeparationSection:
		return self.___systemSeparationSection

	@ContactLineType.setter
	def ContactLineType(self, aContactLineType : tContactLineType):
		self.___contactLineType = aContactLineType
	@IsInsulatedSection.setter
	def IsInsulatedSection(self, aIsInsulatedSection : bool):
		self.___isInsulatedSection = aIsInsulatedSection
	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@ElectrificationSystemRef.setter
	def ElectrificationSystemRef(self, atElementWithIDref : tElementWithIDref):
		self.___electrificationSystemRef = atElementWithIDref
	@EnergyCatenary.setter
	def EnergyCatenary(self, aEnergyCatenary : EnergyCatenary):
		self.___energyCatenary = aEnergyCatenary
	@EnergyPantograph.setter
	def EnergyPantograph(self, aEnergyPantograph : EnergyPantograph):
		self.___energyPantograph = aEnergyPantograph
	@EnergyRollingstock.setter
	def EnergyRollingstock(self, aEnergyRollingstock : EnergyRollingstock):
		self.___energyRollingstock = aEnergyRollingstock
	@ContactWire.setter
	def ContactWire(self, aContactWire : ContactWire):
		self.___hasContactWire = aContactWire
	@PantographSpacing.setter
	def PantographSpacing(self, aPantographSpacing : PantographSpacing):
		self.___pantographSpacing = aPantographSpacing
	@PhaseSeparationSection.setter
	def PhaseSeparationSection(self, aPhaseSeparationSection : PhaseSeparationSection):
		self.___phaseSeparationSection = aPhaseSeparationSection
	@SystemSeparationSection.setter
	def SystemSeparationSection(self, aSystemSeparationSection : SystemSeparationSection):
		self.___systemSeparationSection = aSystemSeparationSection

	def create_ContactLineType(self):
		self.ContactLineType = tContactLineType.tContactLineType()
	def create_IsInsulatedSection(self):
		self.IsInsulatedSection = bool.bool()
	def create_BelongsToParent(self):
		self.BelongsToParent = tRef.tRef()
	def create_ElectrificationSystemRef(self):
		if self.ElectrificationSystemRef == None:
			self.ElectrificationSystemRef = []
		self.ElectrificationSystemRef.append(tElementWithIDref.tElementWithIDref())
	def create_EnergyCatenary(self):
		if self.EnergyCatenary == None:
			self.EnergyCatenary = []
		self.EnergyCatenary.append(EnergyCatenary.EnergyCatenary())
	def create_EnergyPantograph(self):
		if self.EnergyPantograph == None:
			self.EnergyPantograph = []
		self.EnergyPantograph.append(EnergyPantograph.EnergyPantograph())
	def create_EnergyRollingstock(self):
		if self.EnergyRollingstock == None:
			self.EnergyRollingstock = []
		self.EnergyRollingstock.append(EnergyRollingstock.EnergyRollingstock())
	def create_ContactWire(self):
		if self.ContactWire == None:
			self.ContactWire = []
		self.ContactWire.append(ContactWire.ContactWire())
	def create_PantographSpacingn(self):
		if self.PantographSpacing == None:
			self.PantographSpacing = []
		self.PantographSpacing.append(PantographSpacing.PantographSpacing())
	def create_PhaseSeparationSection(self):
		if self.PhaseSeparationSection == None:
			self.PhaseSeparationSection = []
		self.PhaseSeparationSection.append(PhaseSeparationSection.PhaseSeparationSection())
	def create_SystemSeparationSection(self):
		if self.SystemSeparationSection == None:
			self.SystemSeparationSection = []
		self.SystemSeparationSection.append(SystemSeparationSection.SystemSeparationSection())

	def __init__(self):
		super().__init__()
		self.___contactLineType : tContactLineType = None
		# @AssociationType Infrastructure.tContactLineType
		# """type of the installed contact line (most common: overhead)"""
		self.___isInsulatedSection : bool = False
		"""set true if the described electrification section is an insulated section"""
		self.___belongsToParent : tRef = None
		# @AssociationType Common.tRef
		# """reference to the (one and only) parent electrification section"""
		self.___electrificationSystemRef : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the electrification system"""
		self.___energyCatenary : EnergyCatenary = None
		# @AssociationType Infrastructure.EnergyCatenary
		# @AssociationMultiplicity 0..1
		# """child element summarizing the catenary energy parameters"""
		self.___energyPantograph : EnergyPantograph = None
		# @AssociationType Infrastructure.EnergyPantograph
		# @AssociationMultiplicity 0..1
		# """child element summarizing the pantograph energy parameters"""
		self.___energyRollingstock : EnergyRollingstock = None
		# @AssociationType Infrastructure.EnergyRollingstock
		# @AssociationMultiplicity 0..1
		# """child element summarizing the rollingstock energy parameters"""
		self.___hasContactWire : ContactWire = None
		# @AssociationType Infrastructure.ContactWire
		# @AssociationMultiplicity 0..1
		# """child element summarizing the construction details of the contact wire"""
		self.___pantographSpacing : PantographSpacing = None
		# @AssociationType Infrastructure.PantographSpacing*
		# @AssociationMultiplicity 0..*
		# """child element summarizing the pantograph spacing parameters"""
		self.___phaseSeparationSection : PhaseSeparationSection = None
		# @AssociationType Infrastructure.PhaseSeparationSection*
		# @AssociationMultiplicity 0..*
		# """child element summarizing the phase separation parameters"""
		self.___systemSeparationSection : SystemSeparationSection = None
		# @AssociationType Infrastructure.SystemSeparationSection*
		# @AssociationMultiplicity 0..*
		# """child element summarizing the electrification system separation parameters"""