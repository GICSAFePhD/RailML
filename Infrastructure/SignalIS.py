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
	def IsAnnouncementSignal(self) -> SignalAnnouncement:
		return self.___isAnnouncementSignal
	@property
	def IsCatenarySignal(self) -> SignalCatenary:
		return self.___isCatenarySignal
	@property
	def IsDangerSignal(self) -> SignalDanger:
		return self.___isDangerSignal
	@property
	def IsEtcsSignal(self) -> SignalEtcs:
		return self.___isEtcsSignal
	@property
	def IsInformationSignal(self) -> SignalInformation:
		return self.___isInformationSignal
	@property
	def IsLevelCrossingSignal(self) -> SignalLevelCrossing:
		return self.___isLevelCrossingSignal
	@property
	def IsMilepostSignal(self) -> SignalMilepost:
		return self.___isMilepost
	@property
	def IsSpeedSignal(self) -> SignalSpeed:
		return self.___isSpeedSignal
	@property
	def IsStopPostSignal(self) -> SignalStopPost:
		return self.___isStopPost
	@property
	def IsTrainMovementSignal(self) -> SignalTrainMovement:
		return self.___isTrainMovementSignal
	@property
	def IsRadioSignal(self) -> SignalRadio:
		return self.___isTrainRadioSignal
	@property
	def IsVehicleEquipmentSignal(self) -> SignalVehicleEquipment:
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
	@IsAnnouncementSignal.setter
	def IsAnnouncementSignal(self, aIsAnnouncementSignal : SignalAnnouncement):
		self.___isAnnouncementSignal = aIsAnnouncementSignal
	@IsCatenarySignal.setter
	def IsCatenarySignal(self, aIsCatenarySignal : SignalCatenary):
		self.___isCatenarySignal = aIsCatenarySignal
	@IsDangerSignal.setter
	def IsDangerSignal(self, aIsDangerSignal : SignalDanger):
		self.___isDangerSignal = aIsDangerSignal
	@IsEtcsSignal.setter
	def Signal(self, aSignal : SignalEtcs):
		self.___isEtcsSignal = aSignal
	@IsInformationSignal.setter
	def IsInformationSignal(self, aIsInformationSignal : SignalInformation):
		self.___isInformationSignal = aIsInformationSignal
	@IsLevelCrossingSignal.setter
	def IsLevelCrossingSignal(self, aIsLevelCrossingSignal : SignalLevelCrossing):
		self.___isLevelCrossingSignal = aIsLevelCrossingSignal
	@IsMilepostSignal.setter
	def IsMilepostSignal(self, aIsMilepostSignal : SignalMilepost):
		self.___isMilepost = aIsMilepostSignal
	@IsSpeedSignal.setter
	def IsSpeedSignal(self, aIsSpeedSignal : SignalSpeed):
		self.___isSpeedSignal = aIsSpeedSignal
	@IsStopPostSignal.setter
	def IsStopPostSignal(self, aIsStopPostSignal : SignalStopPost):
		self.___isStopPost = aIsStopPostSignal
	@IsTrainMovementSignal.setter
	def IsTrainMovementSignal(self, aIsTrainMovementSignal : SignalTrainMovement):
		self.___isTrainMovementSignal = aIsTrainMovementSignal
	@IsRadioSignal.setter
	def IsRadioSignal(self, aIsRadioSignal : SignalRadio):
		self.___isTrainRadioSignal = aIsRadioSignal
	@IsVehicleEquipmentSignal.setter
	def IsVehicleEquipmentSignal(self, aIsVehicleEquipmentSignal : SignalVehicleEquipment):
		self.___isVehicleEquipmentSignal = aIsVehicleEquipmentSignal
	@ConnectedWithBaliseGroup.setter
	def ConnectedWithBaliseGroup(self, aConnectedWithBaliseGroup : tElementWithIDref):
		self.___connectedWithBaliseGroup = aConnectedWithBaliseGroup
	@SignalConstruction.setter
	def SignalConstruction(self, aSignalConstruction : SignalConstruction):
		self.___signalConstruction = aSignalConstruction
	
	def create_IsAnnouncementSignal(self):
		if self.IsAnnouncementSignal == None:
			self.IsAnnouncementSignal = []
		self.IsAnnouncementSignal.append(SignalAnnouncement.SignalAnnouncement())
	def create_IsCatenarySignal(self):
		if self.IsCatenarySignal == None:
			self.IsCatenarySignal = []
		self.IsCatenarySignal.append(SignalCatenary.SignalCatenary())
	def create_IsDangerSignal(self):
		if self.IsDangerSignal == None:
			self.IsDangerSignal = []
		self.IsDangerSignal.append(SignalDanger.SignalDanger())
	def create_IsEtcsSignal(self):
		if self.IsEtcsSignal == None:
			self.IsEtcsSignal = []
		self.IsEtcsSignal.append(SignalEtcs.SignalEtcs())
	def create_IsInformationSignal(self):
		if self.IsInformationSignal == None:
			self.IsInformationSignal = []
		self.IsInformationSignal.append(SignalInformation.SignalInformation())
	def create_IsLevelCrossingSignal(self):
		if self.IsLevelCrossingSignal == None:
			self.IsLevelCrossingSignal = []
		self.IsLevelCrossingSignal.append(SignalLevelCrossing.SignalLevelCrossing())
	def create_IsMilepostSignal(self):
		if self.IsMilepostSignal == None:
			self.IsMilepostSignal = []
		self.IsMilepostSignal.append(SignalMilepost.SignalMilepost())
	def create_IsSpeedSignal(self):
		if self.IsSpeedSignal == None:
			self.IsSpeedSignal = []
		self.IsSpeedSignal.append(SignalSpeed.SignalSpeed())
	def create_IsStopPostSignal(self):
		if self.IsStopPostSignal == None:
			self.IsStopPostSignal = []
		self.IsStopPostSignal.append(SignalStopPost.SignalStopPost())
	def create_IsTrainMovementSignal(self):
		if self.IsTrainMovementSignal == None:
			self.IsTrainMovementSignal = []
		self.IsTrainMovementSignal.append(SignalTrainMovement.SignalTrainMovement())
	def create_IsRadioSignal(self):
		if self.IsRadioSignal == None:
			self.IsRadioSignal = []
		self.IsRadioSignal.append(SignalRadio.SignalRadio())
	def create_IsVehicleEquipmentSignal(self):
		if self.IsVehicleEquipmentSignal == None:
			self.IsVehicleEquipmentSignal = []
		self.IsVehicleEquipmentSignal.append(SignalVehicleEquipment.SignalVehicleEquipment())
	def create_ConnectedWithBaliseGroup(self):
		if self.ConnectedWithBaliseGroup == None:
			self.ConnectedWithBaliseGroup = []
		self.ConnectedWithBaliseGroup.append(tElementWithIDref.tElementWithIDref())
	def create_SignalConstruction(self):
		if self.SignalConstruction == None:
			self.SignalConstruction = []
		self.SignalConstruction.append(SignalConstruction.SignalConstruction())

	def __str__(self):
		return f'Id:{self.Id}|Net:{self.SpotLocation[0].NetElementRef}'


	def __init__(self):
		super().__init__()
		self.___isSwitchable : Long = None
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