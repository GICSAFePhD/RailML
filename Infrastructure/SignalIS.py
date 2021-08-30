#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import SignalAnnouncement, SignalCatenary, SignalDanger, SignalEtcs, SignalInformation
from RailML.Infrastructure import SignalLevelCrossing, SignalMilepost, SignalSpeed, SignalStopPost, SignalTrainMovement
from RailML.Infrastructure import SignalRadio, SignalVehicleEquipment, SignalConstruction, FunctionalInfrastructureEntity
from typing import List, NewType
Long = NewType("Long", int)

class SignalIS(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def IsSwitchable(self) -> Long:
		return self.___isSwitchable
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def IsSignalAnnouncement(self) -> SignalAnnouncement:
		return self.___isAnnouncementSignal
	@property
	def IsSignalCatenary(self) -> SignalCatenary:
		return self.___isCatenarySignal
	@property
	def IsSignalDanger(self) -> SignalDanger:
		return self.___isDangerSignal
	@property
	def IsSignalEtcs(self) -> SignalEtcs:
		return self.___isEtcsSignal
	@property
	def IsSignalInformation(self) -> SignalInformation:
		return self.___isInformationSignal
	@property
	def IsSignalLevelCrossing(self) -> SignalLevelCrossing:
		return self.___isLevelCrossingSignal
	@property
	def IsSignalMilepost(self) -> SignalMilepost:
		return self.___isMilepost
	@property
	def IsSignalSpeed(self) -> SignalSpeed:
		return self.___isSpeedSignal
	@property
	def IsSignalStopPost(self) -> SignalStopPost:
		return self.___isStopPost
	@property
	def IsSignalTrainMovement(self) -> SignalTrainMovement:
		return self.___isTrainMovementSignal
	@property
	def IsSignalRadio(self) -> SignalRadio:
		return self.___isTrainRadioSignal
	@property
	def IsSignalVehicleEquipment(self) -> SignalVehicleEquipment:
		return self.___isVehicleEquipmentSignal
	@property
	def ConnectedWithBaliseGroup(self) -> tElementWithIDref:
		return self.___connectedWithBaliseGroup
	@property
	def SignalConstruction(self) -> SignalConstruction:
		return self.___signalConstruction

	@IsSwitchable.setter
	def IsSwitchable(self, aIsSwitchable : Long):
		self.___isSwitchable = aIsSwitchable
	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@IsSignalAnnouncement.setter
	def IsSignalAnnouncement(self, aSignalAnnouncement : SignalAnnouncement):
		self.___isAnnouncementSignal = aSignalAnnouncement
	@IsSignalCatenary.setter
	def IsSignalCatenary(self, aSignalCatenary : SignalCatenary):
		self.___isCatenarySignal = aSignalCatenary
	@IsSignalDanger.setter
	def IsSignalDanger(self, aSignalDanger : SignalDanger):
		self.___isDangerSignal = aSignalDanger
	@IsSignalEtcs.setter
	def IsSignalEtcs(self, aSignalEtcs : SignalEtcs):
		self.___isEtcsSignal = aSignalEtcs
	@IsSignalInformation.setter
	def IsSignalInformation(self, aSignalInformation : SignalInformation):
		self.___isInformationSignal = aSignalInformation
	@IsSignalLevelCrossing.setter
	def IsSignalLevelCrossing(self, aSignalLevelCrossing : SignalLevelCrossing):
		self.___isLevelCrossingSignal = aSignalLevelCrossing
	@IsSignalMilepost.setter
	def IsSignalMilepost(self, aSignalMilepost : SignalMilepost):
		self.___isMilepost = aSignalMilepost
	@IsSignalSpeed.setter
	def IsSignalSpeed(self, aSignalSpeed : SignalSpeed):
		self.___isSpeedSignal = aSignalSpeed
	@IsSignalStopPost.setter
	def IsSignalStopPost(self, aSignalStopPost : SignalStopPost):
		self.___isStopPost = aSignalStopPost
	@IsSignalTrainMovement.setter
	def IsSignalTrainMovement(self, aSignalTrainMovement : SignalTrainMovement):
		self.___isTrainMovementSignal = aSignalTrainMovement
	@IsSignalRadio.setter
	def IsSignalRadio(self, aSignalRadio : SignalRadio):
		self.___isTrainRadioSignal = aSignalRadio
	@IsSignalVehicleEquipment.setter
	def IsSignalVehicleEquipment(self, aSignalVehicleEquipment : SignalVehicleEquipment):
		self.___isVehicleEquipmentSignal = aSignalVehicleEquipment
	@ConnectedWithBaliseGroup.setter
	def ConnectedWithBaliseGroup(self, aConnectedWithBaliseGroup : tElementWithIDref):
		self.___connectedWithBaliseGroup = aConnectedWithBaliseGroup
	@SignalConstruction.setter
	def SignalConstruction(self, aSignalConstruction : SignalConstruction):
		self.___signalConstruction = aSignalConstruction
	
	def create_IsSignalAnnouncement(self):
		if self.IsSignalAnnouncement == None:
			self.IsSignalAnnouncement = []
		self.IsSignalAnnouncement.append(SignalAnnouncement.SignalAnnouncement())
	def create_IsSignalCatenary(self):
		if self.IsSignalCatenary == None:
			self.IsSignalCatenary = []
		self.IsSignalCatenary.append(SignalCatenary.SignalCatenary())
	def create_IsSignalDanger(self):
		if self.IsSignalDanger == None:
			self.IsSignalDanger = []
		self.IsSignalDanger.append(SignalDanger.SignalDanger())
	def create_IsSignalEtcs(self):
		if self.IsSignalEtcs == None:
			self.IsSignalEtcs = []
		self.IsSignalEtcs.append(SignalEtcs.SignalEtcs())
	def create_IsSignalInformation(self):
		if self.IsSignalInformation == None:
			self.IsSignalInformation = []
		self.IsSignalInformation.append(SignalInformation.SignalInformation())
	def create_IsSignalLevelCrossing(self):
		if self.IsSignalLevelCrossing == None:
			self.IsSignalLevelCrossing = []
		self.IsSignalLevelCrossing.append(SignalLevelCrossing.SignalLevelCrossing())
	def create_IsSignalMilepost(self):
		if self.IsSignalMilepost == None:
			self.IsSignalMilepost = []
		self.IsSignalMilepost.append(SignalMilepost.SignalMilepost())
	def create_IsSignalSpeed(self):
		if self.IsSignalSpeed == None:
			self.IsSignalSpeed = []
		self.IsSignalSpeed.append(SignalSpeed.SignalSpeed())
	def create_IsSignalStopPost(self):
		if self.IsSignalStopPost == None:
			self.IsSignalStopPost = []
		self.IsSignalStopPost.append(SignalStopPost.SignalStopPost())
	def create_IsSignalTrainMovement(self):
		if self.IsSignalTrainMovement == None:
			self.IsSignalTrainMovement = []
		self.IsSignalTrainMovement.append(SignalTrainMovement.SignalTrainMovement())
	def create_IsSignalRadio(self):
		if self.IsSignalRadio == None:
			self.IsSignalRadio = []
		self.IsSignalRadio.append(SignalRadio.SignalRadio())
	def create_IsSignalVehicleEquipment(self):
		if self.IsSignalVehicleEquipment == None:
			self.IsSignalVehicleEquipment = []
		self.IsSignalVehicleEquipment.append(SignalVehicleEquipment.SignalVehicleEquipment())
	def create_ConnectedWithBaliseGroup(self):
		if self.ConnectedWithBaliseGroup == None:
			self.ConnectedWithBaliseGroup = []
		self.ConnectedWithBaliseGroup.append(tElementWithIDref.tElementWithIDref())
	def create_SignalConstruction(self):
		if self.SignalConstruction == None:
			self.SignalConstruction = []
		self.SignalConstruction.append(SignalConstruction.SignalConstruction())

	def __init__(self):
		super().__init__()
		self.___isSwitchable : Long = 0
		"""set TRUE if the signal is able to show several signal aspects, set FALSE if the signal is a static panel that always shows the same signal aspect"""
		self.___belongsToParent : tRef = None
		"""reference to the (one and only) parent signal this signal belongs to"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a generic signal"""
		self.___isAnnouncementSignal : SignalAnnouncement = None
		# @AssociationType Infrastructure.SignalAnnouncement
		# @AssociationMultiplicity 0..1
		self.___isCatenarySignal : SignalCatenary = None
		# @AssociationType Infrastructure.SignalCatenary
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the catenary signal/sign in more detail"""
		self.___isDangerSignal : SignalDanger = None
		# @AssociationType Infrastructure.SignalDanger
		# @AssociationMultiplicity 0..1
		self.___isEtcsSignal : SignalEtcs = None
		# @AssociationType Infrastructure.SignalEtcs
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the ETCS signal in more detail"""
		self.___isInformationSignal : SignalInformation = None
		# @AssociationType Infrastructure.SignalInformation
		# @AssociationMultiplicity 0..1
		self.___isLevelCrossingSignal : SignalLevelCrossing = None
		# @AssociationType Infrastructure.SignalLevelCrossing
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the level crossing signal in more detail"""
		self.___isMilepost : SignalMilepost = None
		# @AssociationType Infrastructure.SignalMilepost
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the milepost marker in more detail"""
		self.___isSpeedSignal : SignalSpeed = None
		# @AssociationType Infrastructure.SignalSpeed
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the speed signal in more detail"""
		self.___isStopPost : SignalStopPost = None
		# @AssociationType Infrastructure.SignalStopPost
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the stop post in more detail"""
		self.___isTrainMovementSignal : SignalTrainMovement = None
		# @AssociationType Infrastructure.SignalTrainMovement
		# @AssociationMultiplicity 0..1
		self.___isTrainRadioSignal : SignalRadio = None
		# @AssociationType Infrastructure.SignalRadio
		# @AssociationMultiplicity 0..1
		self.___isVehicleEquipmentSignal : SignalVehicleEquipment = None
		# @AssociationType Infrastructure.SignalVehicleEquipment
		# @AssociationMultiplicity 0..1
		self.___connectedWithBaliseGroup : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a balise (group) that is connected with this signal"""
		self.___signalConstruction : SignalConstruction = None
		# @AssociationType Infrastructure.SignalConstruction
		# @AssociationMultiplicity 0..1
		# """child element for construction details of the (physical) signal"""