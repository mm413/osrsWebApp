# Mark Meade
# Gear.py
import sys
sys.path.insert(0,'/osrsWebApp/logicHandling/gear/')
from osrsbox import items_api

class Gear:
    def __init__(self):
        self.headSlotItems = []
        self.neckSlotItems = []
        self.shieldSlotItems = []
        self.mainHandSlotItems = []
        self.chestSlotItems = []
        self.legSlotItems = []
        self.footSlotItems = []
        self.handSlotItems = []
        self.ringSlotItems = []
        self.ammoSlotItems = []
        self.capeSlotItems = []
        self.twohandSlotItems = []
        self.loadGear()

    def loadGear(self):
        items = items_api.load()
        for item in items:
            if item.equipable_by_player:
                if item.equipment.slot == 'weapon':
                    self.mainHandSlotItems.append(item)
                elif item.equipment.slot == '2h':
                    self.twohandSlotItems.append(item)
                elif item.equipment.slot == 'ammo':
                    self.ammoSlotItems.append(item)
                elif item.equipment.slot == 'body':
                    self.chestSlotItems.append(item)
                elif item.equipment.slot == 'cape':
                    self.capeSlotItems.append(item)
                elif item.equipment.slot == 'feet':
                    self.footSlotItems.append(item)
                elif item.equipment.slot == 'hands':
                    self.handSlotItems.append(item)
                elif item.equipment.slot == 'head':
                    self.headSlotItems.append(item)
                elif item.equipment.slot == 'legs':
                    self.legSlotItems.append(item)
                elif item.equipment.slot == 'neck':
                    self.neckSlotItems.append(item)
                elif item.equipment.slot == 'ring':
                    self.ringSlotItems.append(item)
                elif item.equipment.slot == 'shield':
                    self.shieldSlotItems.append(item)



