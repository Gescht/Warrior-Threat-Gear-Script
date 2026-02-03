from itertools import combinations
import polars as pl

resultsTPS = []
"""
[ {"items": string,"tps": float,}, ]
"""
total = {
    "hp": 0,
    "stam": 0,
    "str": 0,
    "armor": 0,
    "agi": 0,
    "crit": 0,
    "hit": 0,
    "ap": 0,
    "arp": 0,
    "haste": 1,
    "block_chance": 0,
    "block_value": 0,
    "def": 0,
    "dodge": 0,
    "parry": 0.08,
    "dps": 0,
    "speed": 0,
    "damage_min": 0,
    "damage_max": 0,
    "Axe": 0,
    "Dagger": 0,
    "Fist Weapon": 0,
    "Mace": 0,
    "Sword": 0,
    }
totalPreGear = {
    "hp": 0,
    "stam": 0,
    "str": 0,
    "armor": 0,
    "agi": 0,
    "crit": 0,
    "hit": 0,
    "ap": 0,
    "arp": 0,
    "haste": 1,
    "block_chance": 0,
    "block_value": 0,
    "def": 0,
    "dodge": 0,
    "parry": 0.08,
    "dps": 0,
    "speed": 0,
    "damage_min": 0,
    "damage_max": 0,
    "Axe": 0,
    "Dagger": 0,
    "Fist Weapon": 0,
    "Mace": 0,
    "Sword": 0,
    }
gear = {
    "name": "",
    "armor": 0,
    "stam": 0,
    "str": 0,
    "agi": 0,
    "hit": 0,
    "crit": 0,
    "ap": 0,
    "arp": 0,
    "haste": 1,
    "block_chance": 0,
    "block_value": 0,
    "def": 0,
    "dodge": 0,
    "parry": 0,
    "dps": 0,
    "speed": 0,
    "damage_min": 0,
    "damage_max": 0,
    "Axe": 0,
    "Dagger": 0,
    "Fist Weapon": 0,
    "Mace": 0,
    "Sword": 0,
    }
enchants = {
    "stam": 63,
    "str": 53,
    "agi": 41,
    "block_value": 30,
    "def": 14,
    "dodge": 1,
    }
consumes = {
    "hp": 1320,
    "stam": 103,
    "str": 18,
    "armor": 2890,
    "agi": 50,
    "crit": 4,
    "ap": 35,
    "haste": 1.02,
    }
buffs = {
    "stam": 86,
    "str": 112,
    "armor": 384,
    "agi": 16,
    "ap": 222,
    "Axe": 5,
    "Dagger": 5,
    "Fist Weapon": 5,
    "Mace": 5,
    "Sword": 5,
    }
base = {
    "hp": 1518,
    "stam": 112,
    "str": 125,
    "agi": 75,
    "crit": 3,
    "ap": 160,
    "def": 300,
    }
statListsNoGear = [
    enchants,
    consumes,
    buffs,
    base,
]
talents = {
    "toughness": 5,
    "defiance": 5,
    "cruelty": 3,
}
settings = {
    "tauren": True,
    "bossArmor": 191,
}
DefensiveStance = False
NormalisedOneHander = 2.4
WindfuryUsed = True
ThunderfuryUsed = True

AttackPower = 0
Hit = 0
CritChance = 0
AttackSpeed = 0
BlockValue = 0
ParryChance = 0
ParrySwingIncrease = 0
DamageMod = 0
ThreatModifier = 0
WeaponMin = 0
WeaponMax = 0
WeaponSpeed = 0
GlancingMod = 0
HeroicStrikePercentage = 0
Boss_ArmorDamageReduction = 0
BossDodge = 0
Boss_Avoidance = 0
Boss_SpellAvoidance = 0

Calc_ShieldSlam_BvScaling = 1
Calc_ShieldSlam_ApScaling = 0.2
Calc_ShieldSlam_BaseDamage = 310
Calc_ShieldSlam_ThreatMod = 1.75
Calc_ShieldSlam_CD = 4.5
Calc_Revenge_BaseDamage = 90
Calc_Revenge_BaseThreat = 355
Calc_Revenge_CD = 6
Calc_Overpower_BaseDamage = 35
Calc_Overpower_CD = 5
Calc_HeroicStrike_BaseDamage = 157
Calc_HeroicStrike_BaseThreat = 175
Calc_ConcussionBlow_ApScaling = 0.15
Calc_ConcussionBlow_BaseDamage = 235
Calc_ConcussionBlow_ThreatMod = 1.5
Calc_ConcussionBlow_CD = 20
Calc_Thunderfury_ProccChance = 0.19
Calc_Thunderfury_BaseDamage = 300
Calc_Thunderfury_BaseThreat = 234
Calc_Windfury_ProccChance = 0.2
Calc_Windfury = 315

gearIndex = [
    "item_id",
    "name",
    "raid",
    "slot",
    "type",
    "armor",
    "stam",
    "str",
    "agi",
    "hit",
    "crit",
    "ap",
    "arp",
    "haste",
    "block_chance",
    "block_value",
    "def",
    "dodge",
    "parry",
    "dps",
    "speed",
    "damage_min",
    "damage_max",
    "Axe",
    "Dagger",
    "Fist Weapon",
    "Mace",
    "Sword",
]
indexOfFirstStat = 5
gearFilePolar = pl.read_csv('C:\\Users\Tobi\\Documents\\GitHub\\Warrior-Threat-Gear-Script\\gear.csv', has_header=True)
"""
0-"item_id"
1-"name"
2-"raid"
3-"slot"
4-"type"
5-"armor"
6-"stam"
7-"str"
8-"agi"
9-"hit"
10-"crit"
11-"ap"
12-"arp"
13-"haste"
14-"block_chance"
15-"block_value"
16-"def"
17-"dodge"
18-"parry"
19-"dps"
20-"speed"
21-"damage_min"
22-"damage_max"
23-"Axe"
24-"Dagger"
25-"Fist Weapon"
26-"Mace"
27-"Sword"
"""
gearHead = []
gearNeck = []
gearShoulder = []
gearBack = []
gearChest = []
gearWrist = []
gearHands = []
gearWaist = []
gearLegs = []
gearFeet = []
gearFinger = []
gearTrinket = []
gearWeapon = []
gearOffHand = []
gearRanged = []

def sortRawGear():
    for i, row in enumerate(gearFilePolar.iter_rows()):
        #do not add Naxx loot to the sorted gear, yet
        if row[3] == "Naxx":
            continue
        match row[3]:
            case "Head":
                gearHead.append(gearFilePolar.row(i))
            case "Neck":
                gearNeck.append(gearFilePolar.row(i))
            case "Shoulder":
                gearShoulder.append(gearFilePolar.row(i))
            case "Back":
                gearBack.append(gearFilePolar.row(i))
            case "Chest":
                gearChest.append(gearFilePolar.row(i))
            case "Wrist":
                gearWrist.append(gearFilePolar.row(i))
            case "Hands":
                gearHands.append(gearFilePolar.row(i))
            case "Waist":
                gearWaist.append(gearFilePolar.row(i))
            case "Legs":
                gearLegs.append(gearFilePolar.row(i))
            case "Feet":
                gearFeet.append(gearFilePolar.row(i))
            case "Finger":
                gearFinger.append(gearFilePolar.row(i))
            case "Trinket":
                gearTrinket.append(gearFilePolar.row(i))
            case "Weapon":
                gearWeapon.append(gearFilePolar.row(i))
            case "Off Hand":
                gearOffHand.append(gearFilePolar.row(i))
            case "Ranged":
                gearRanged.append(gearFilePolar.row(i))
        #print(i, row)

def combineFingerAndTrinket():
    global gearFinger
    global gearTrinket
    gearFinger = list(combinations(gearFinger, 2))
    gearTrinket = list(combinations(gearTrinket, 2))
    return

#for i, df in enumerate(gearFinger):
#    print(gearFinger[i])

def getAddedTotalStats(stat,sList=statListsNoGear):
    totalStat = 0
    for i in sList:
        if stat in i:
            totalStat = totalStat + i[stat]
    return totalStat

def getGearStat(stat):
    if stat in gear:
        return gear[stat]
    else:
        return 0

def getMultipliedTotalHaste(sList=statListsNoGear):
    haste = 1
    for i in sList:
        if "haste" in i:
            haste = haste * i["haste"]
    return haste

def getTotalStatsArmor():
    returnArmor = int(gear["armor"]*(0.02*talents["toughness"]+1)) + totalPreGear["armor"]
    returnArmor = int(returnArmor + total["agi"]*2)
    return returnArmor

def getTotalStatsHaste():
    if "haste" in gear:
        return totalPreGear["haste"]*gear["haste"]
    else:
        return totalPreGear["haste"]
    
def getTotalStatsHp():    
    if "hp" in gear:
        return int(totalPreGear["hp"]+total["stam"]*10+getGearStat("hp"))
    else:
        return int(totalPreGear["hp"]+total["stam"]*10)

def getBaseStatWithKings(stat):
    return int((totalPreGear[stat]+getGearStat(stat))*1.1)

def calcTotalStatsWithoutGear():
    totalPreGear["stam"] = getAddedTotalStats("stam")
    totalPreGear["str"] = getAddedTotalStats("str")
    totalPreGear["agi"] = getAddedTotalStats("agi")
    totalPreGear["hp"] = getAddedTotalStats("hp")
    totalPreGear["armor"] = getAddedTotalStats("armor")
    totalPreGear["crit"] = getAddedTotalStats("crit")
    totalPreGear["hit"] = getAddedTotalStats("hit")
    totalPreGear["ap"] = getAddedTotalStats("ap")
    totalPreGear["arp"] = getAddedTotalStats("arp")
    totalPreGear["haste"] = getMultipliedTotalHaste()
    totalPreGear["block_value"] = getAddedTotalStats("block_value")
    #total["Axe"] = getAddedTotalStats("Axe")
    #total["Dagger"] = getAddedTotalStats("Dagger")
    #total["Fist Weapon"] = getAddedTotalStats("Fist Weapon")
    #total["Mace"] = getAddedTotalStats("Mace")
    totalPreGear["Sword"] = getAddedTotalStats("Sword")

def addItemsToGearTotal(*args):
    global gear
    #loop through all the items 
    for item in args:
        gear["name"] += (item[gearIndex.index("name")]+"\n")
        #print(gear["name"])
        #loop through all the stats
        for index in range(indexOfFirstStat,(len(gearIndex))):
            if item[index] is None:
                continue
            #print("--")
            if gearIndex[index] == "haste":
                #print(gearIndex[index]," before item added ", gear[gearIndex[index]])
                #print(gear[gearIndex[index]]," * ", 1+(item[index]/100)," = ",gear[gearIndex[index]]*(1+(item[index]/100)))
                gear[gearIndex[index]] = gear[gearIndex[index]]*(1+(item[index]/100))
                #print(gearIndex[index]," after item added ",gear[gearIndex[index]])
            else:
                #print(gearIndex[index]," before item added ", gear[gearIndex[index]])
                #print(gear[gearIndex[index]]," + ", item[index]," = ",gear[gearIndex[index]] + item[index])
                gear[gearIndex[index]] += item[index]
                #print(gearIndex[index]," after item added ",gear[gearIndex[index]])
    return

def resetTotalGear():
    global gear
    gear = gear = {
    "name": "",
    "armor": 0,
    "stam": 0,
    "str": 0,
    "agi": 0,
    "hit": 0,
    "crit": 0,
    "ap": 0,
    "arp": 0,
    "haste": 1,
    "block_chance": 0,
    "block_value": 0,
    "def": 0,
    "dodge": 0,
    "parry": 0,
    "dps": 0,
    "speed": 0,
    "damage_min": 0,
    "damage_max": 0,
    "Axe": 0,
    "Dagger": 0,
    "Fist Weapon": 0,
    "Mace": 0,
    "Sword": 0,
    }

def calcTotalStatsWithGear():
    total["stam"] = getBaseStatWithKings("stam")
    total["str"] = getBaseStatWithKings("str")
    total["agi"] = getBaseStatWithKings("agi")
    total["hp"] = getTotalStatsHp()
    if settings["tauren"]:
        total["hp"] = int(total["hp"]*1.05)
    total["armor"] = getTotalStatsArmor()
    total["crit"] = totalPreGear["crit"]+getGearStat("crit")+total["agi"]/20
    total["hit"] = totalPreGear["hit"]+getGearStat("hit")
    total["ap"] = totalPreGear["ap"]+getGearStat("ap")+total["str"]*2
    total["arp"] = totalPreGear["arp"]+getGearStat("arp")
    total["haste"] = getTotalStatsHaste()
    total["block_value"] = int((totalPreGear["block_value"]+getGearStat("block_value")+int(total["str"]/20))*(0.03*talents["toughness"]+1))
    total["dps"] = getGearStat("dps")+total["ap"]/14
    total["speed"] = gear["speed"]
    total["damage_min"] = getGearStat("damage_min")
    total["damage_max"] = getGearStat("damage_max")
    #total["Axe"] = total["Axe"]+getGearStat("Axe")
    #total["Dagger"] = total["Dagger"]+getGearStat("Dagger")
    #total["Fist Weapon"] = total["Fist Weapon"]+getGearStat("Fist Weapon")
    #total["Mace"] = total["Mace"]+getGearStat("Mace")
    total["Sword"] = totalPreGear["Sword"]+getGearStat("Sword")
    total["weaponskill"] = totalPreGear["Sword"]

def prepCalcStats():
    global AttackPower
    global Hit
    global CritChance
    global AttackSpeed
    global BlockValue
    global ParryChance
    global ParrySwingIncrease
    global DamageMod
    global ThreatModifier
    global WeaponMin
    global WeaponMax
    global WeaponSpeed
    global GlancingMod
    global HeroicStrikePercentage
    global ThunderfuryUsed
    global Boss_ArmorDamageReduction
    global BossDodge
    global Boss_Avoidance
    global Boss_SpellAvoidance

    AttackPower = total["ap"]
    Hit = 0.08-((total["hit"]/100)+(total["weaponskill"]*0.002))
    CritChance = (total["crit"]+talents["cruelty"])/100+total["weaponskill"]*0.0004
    AttackSpeed = total["haste"]-1
    BlockValue = total["block_value"]
    ParryChance = 0.08
    ParrySwingIncrease = 0.24*(total["speed"]/2.2)
    DamageMod = 0.9 if DefensiveStance else 1
    ThreatModifier = 1.3*(1+talents["defiance"]*0.04) if DefensiveStance else 0.8*((1.3*(1+(talents["defiance"]*0.04))-1)*1.8+1)
    WeaponMin = total["damage_min"]
    WeaponMax = total["damage_max"]
    WeaponSpeed = total["speed"]
    GlancingMod = 0.4*(0.95-((0 if total["weaponskill"] >= 15 else 15-total["weaponskill"])*0.02))-0.4+1
    HeroicStrikePercentage = 0.8
    ThunderfuryUsed = True
    Boss_ArmorDamageReduction = settings["bossArmor"]/(settings["bossArmor"]+5500)
    BossDodge = 0.05-total["weaponskill"]*0.0005
    Boss_Avoidance = (0 if Hit <= 0 else Hit)+BossDodge+0.05    
    Boss_SpellAvoidance = 0.15

def calcShieldSlamThreatPerSecond():
    shieldSlamThreatPerSecond = (
        (
            (BlockValue*Calc_ShieldSlam_BvScaling + AttackPower*Calc_ShieldSlam_ApScaling + Calc_ShieldSlam_BaseDamage)
            *DamageMod
            *(1.2*CritChance+1)                
            *(1-Boss_ArmorDamageReduction)
            *Calc_ShieldSlam_ThreatMod
            *ThreatModifier
            *(1-Boss_Avoidance)
        )/Calc_ShieldSlam_CD
    )
    #print("ShieldSlam ",shieldSlamThreatPerSecond)
    return shieldSlamThreatPerSecond
def calcRevengeThreatPerSecond():
    if DefensiveStance:    
        revengeThreatPerSecond = (
            (
                (
                    Calc_Revenge_BaseDamage
                    *DamageMod
                    *(1.2*CritChance+1)
                    *(1-Boss_ArmorDamageReduction)
                    +Calc_Revenge_BaseThreat
                )
                *ThreatModifier
                *(1-Boss_Avoidance)
            )/Calc_Revenge_CD
        )
        #print("revenge ",revengeThreatPerSecond)
        return revengeThreatPerSecond
    else:
        #print("revenge ",0)
        return 0
def calcOverpowerThreatPerSecond():
    if DefensiveStance:
        #print("Overpower ",0)
        return 0
    else:
        dodgePerSecond = ((1/(WeaponSpeed/(1+AttackSpeed)))+(1/1.5))*(1+Calc_Windfury_ProccChance if WindfuryUsed else 1)*BossDodge
        overPowerPerSecond = 1/Calc_Overpower_CD
        overPowerThreatPerSecond = (
            (
                ((WeaponMin+WeaponMax)/2)
                +Calc_Overpower_BaseDamage
                +(NormalisedOneHander*(AttackPower/14))
            )
            *DamageMod
            *( 2.2 if CritChance >= 0.5 else CritChance+1.7 )
            *(1-Boss_ArmorDamageReduction)
            *ThreatModifier
            *(overPowerPerSecond if (dodgePerSecond>overPowerPerSecond) else dodgePerSecond)
        )
        #print("Overpower ",overPowerThreatPerSecond)
        return overPowerThreatPerSecond
def calcHeroicStrikeThreatPerSecond():
    heroicStrikeThreatPerSecond = (
        (
            (
                (
                    ((WeaponMin+WeaponMax)/2)
                    +(WeaponSpeed*(AttackPower/14))
                    +Calc_HeroicStrike_BaseDamage
                )
                *DamageMod
                *(1.2*CritChance+1)
                *(1-Boss_ArmorDamageReduction)
                +Calc_HeroicStrike_BaseThreat
            )
            *ThreatModifier
            *(1-Boss_Avoidance)
            *(HeroicStrikePercentage)
        )
        /(WeaponSpeed/(1+AttackSpeed+(ParryChance*ParrySwingIncrease)))
    )
    #print("heroicStrike ",heroicStrikeThreatPerSecond)
    return heroicStrikeThreatPerSecond
def calcConcussionBlowThreatPerSecond():
    concussionBlowThreatPerSecond = (
        (
            (
                (AttackPower*Calc_ConcussionBlow_ApScaling)
                +Calc_ConcussionBlow_BaseDamage
            )
            *DamageMod
            *(1.2*CritChance+1)
            *Calc_ConcussionBlow_ThreatMod
            *ThreatModifier
            *(1-Boss_Avoidance)
        )
        /Calc_ConcussionBlow_CD
    ) 
    #print("concussionBlow ",concussionBlowThreatPerSecond)
    return concussionBlowThreatPerSecond
def calcThunderfuryThreatPerSecond():
    if ThunderfuryUsed:
        thunderfuryThreatPerSecond = (
            (
                (1/(WeaponSpeed/(1+AttackSpeed+(ParryChance*ParrySwingIncrease))))
                +(1/1.5)
            )
            *Calc_Thunderfury_ProccChance
            *(1-Boss_SpellAvoidance)
            *ThreatModifier
            *(
                Calc_Thunderfury_BaseDamage
                *DamageMod
                *1.1
                +Calc_Thunderfury_BaseThreat
            )
        )
        #print("thunderfury ",thunderfuryThreatPerSecond)
        return thunderfuryThreatPerSecond
    else:
        #print("thunderfury ",0)
        return 0
def calcWindfuryThreatPerSecond():
    if WindfuryUsed:
        windfuryThreatPerSecond = (
            (
                (
                    1
                    /(
                        WeaponSpeed
                        /(
                            1
                            +AttackSpeed
                            +(ParryChance*ParrySwingIncrease)
                        )
                    )
                )
                + 1/1.5
            )
            *(
                ((WeaponMin+WeaponMax)/2)
                +(
                    WeaponSpeed
                    *((AttackPower+Calc_Windfury)/14)
                )
            )
            *DamageMod
            *(CritChance+1)
            *(1-Boss_ArmorDamageReduction)
            *GlancingMod
            *ThreatModifier
            *Calc_Windfury_ProccChance
            *(1-Boss_Avoidance)
        )
        #print("windfury ",windfuryThreatPerSecond)
        return windfuryThreatPerSecond
    else:
        #print("Windfury ",0)
        return 0
def calcAutoattackThreatPerSecond():
    autoattackThreatPerSecond = (
        (
            (
                (
                    ((WeaponMin+WeaponMax)/2)
                    +(WeaponSpeed*(AttackPower/14))
                )
                *DamageMod
                *(CritChance+1)
                *(1-Boss_ArmorDamageReduction)
            )
            *GlancingMod
            *ThreatModifier
            *(1-HeroicStrikePercentage)
            *(1-Boss_Avoidance)
        )
        /(
            WeaponSpeed
            /(
                1
                +AttackSpeed
                +(ParryChance*ParrySwingIncrease)
            )
        )
    )
    #print("autoattack ",autoattackThreatPerSecond)
    return autoattackThreatPerSecond
def calcThreatPerSecond():
    return (
        calcShieldSlamThreatPerSecond()
        + calcRevengeThreatPerSecond()
        + calcOverpowerThreatPerSecond()
        + calcHeroicStrikeThreatPerSecond()
        + calcConcussionBlowThreatPerSecond()
        + calcThunderfuryThreatPerSecond()
        + calcWindfuryThreatPerSecond()
        + calcAutoattackThreatPerSecond()
        )

def generateGearSets():
    global resultsTPS
    for head, _ in enumerate(gearHead):
        for neck, _ in enumerate(gearNeck):
            for shoulder, _ in enumerate(gearShoulder):
                for back, _ in enumerate(gearBack):
                    for chest, _ in enumerate(gearChest):
                        for wrist, _ in enumerate(gearWrist):
                            for hands, _ in enumerate(gearHands):
                                for waist, _ in enumerate(gearWaist):
                                    for legs, _ in enumerate(gearLegs):
                                        for feet, _ in enumerate(gearFeet):
                                            for fingers, _ in enumerate(gearFinger):
                                                for trinkets, _ in enumerate(gearTrinket):
                                                    for weapon, _ in enumerate(gearWeapon):
                                                        for offhand, _ in enumerate(gearOffHand):
                                                            for ranged, _ in enumerate(gearRanged):
                                                                addItemsToGearTotal(gearHead[head],gearNeck[neck],gearShoulder[shoulder],gearBack[back],gearChest[chest],gearWrist[wrist],gearHands[hands],gearWaist[waist],gearLegs[legs],gearFeet[feet],gearFinger[fingers][0],gearFinger[fingers][1],gearTrinket[trinkets][0],gearTrinket[trinkets][1],gearWeapon[weapon],gearOffHand[offhand],gearRanged[ranged])

                                                                #calculate the total stats including stats from gear
                                                                calcTotalStatsWithGear()

                                                                #convert character stats into stats used by the threat calc
                                                                prepCalcStats()

                                                                resultsTPS.append({"items":gear["name"],"tps":calcThreatPerSecond(),"hit":Hit})

                                                                #reset all stats to prepare for the next gearset
                                                                resetTotalGear()

sortRawGear()

combineFingerAndTrinket()

calcTotalStatsWithoutGear()

generateGearSets()

def resultSort(e):
    return e["tps"]
resultsTPS.sort(reverse=True,key=resultSort)

print("**************************************")
for results in resultsTPS[:5]:
    print("tps: ",results["tps"])
    print("hit: ",results["hit"])
    print(results["items"])
    print("**********")