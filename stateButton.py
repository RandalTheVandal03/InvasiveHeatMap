from backend import *

class state:
    def __init__(self, lw, rw, th, bh, name):
        self.leftBound = lw
        self.rightBound = rw
        self.bottomBound = bh
        self.topBound = th
        self.stateName = str(name).lower()
        self.dataSet = getStateData(self.stateName)

    def onClicked(self):
        print("Clicked " + self.stateName)    
        for list in self.dataSet:
            for list2 in list:
                print(list2 , end=" ")
            print()

    def isClicked(self, mouseX, mouseY):
        if (self.leftBound <= mouseX <= self.rightBound) and (self.bottomBound <= mouseY <= self.topBound):
            self.onClicked()
            
def stateInstantiation():
    stateButtonList = []
    stateButtonList.append(state(793, 841, 112, 36, 'Florida'))
    stateButtonList.append(state(678, 727, 626-403, 626-470, 'Alabama'))
    stateButtonList.append(state(172, 241, 626-472, 626-548, 'Alaska'))
    stateButtonList.append(state(182, 263, 626-331, 626-429, 'Arizona'))
    stateButtonList.append(state(280, 360, 626-332, 626-411, 'New_Mexico'))
    stateButtonList.append(state(389, 527, 626-432, 626-512, 'Texas'))
    stateButtonList.append(state(353, 409, 626-548, 626-603, 'Hawaii'))
    stateButtonList.append(state(555, 600, 626-441, 626-483, 'Louisiana'))
    stateButtonList.append(state(619, 663, 626-429, 626-480, 'Mississippi'))
    stateButtonList.append(state(735, 801, 626-410, 626-473, 'Georgia'))
    stateButtonList.append(state(783, 844, 626-383, 626-419, 'South_Carolina'))
    stateButtonList.append(state(783, 877, 626-343, 626-370, 'North_Carolina'))
    stateButtonList.append(state(650, 737, 626-355, 626-380, 'Tennessee'))
    stateButtonList.append(state(551, 616, 626-372, 626-413, 'Arkansas'))
    stateButtonList.append(state(451, 540, 626-346, 626-400, 'Oklahoma'))
    stateButtonList.append(state(802, 879, 626-305, 626-327, 'Virginia'))
    stateButtonList.append(state(679, 747, 626-319, 626-340, 'Kentucky'))
    stateButtonList.append(state(552, 618, 626-297, 626-344, 'Missouri'))
    stateButtonList.append(state(422, 524, 626-474, 626-469, 'Kansas'))
    stateButtonList.append(state(293, 401, 626-252, 626-325, 'Colorado'))
    stateButtonList.append(state(207, 274, 626-238, 626-296, 'Utah'))
    stateButtonList.append(state(107, 189, 626-204, 626-258, 'Nevada'))
    stateButtonList.append(state(49, 108, 626-255, 626-346, 'California'))
    stateButtonList.append(state(782, 811, 626-269, 626-303, 'West_Virginia'))
    stateButtonList.append(state(905, 963, 626-280, 626-302, 'Maryland'))
    stateButtonList.append(state(898, 961, 626-254, 626-275, 'Delaware'))
    stateButtonList.append(state(935, 978, 626-72, 626-120, 'Maine'))
    stateButtonList.append(state(920, 940, 626-135, 626-160, 'New_Hampshire'))
    stateButtonList.append(state(897, 915, 626-122, 626-146, 'Vermont'))
    stateButtonList.append(state(910, 940, 626-165, 626-180, 'Massachusetts'))
    stateButtonList.append(state(942, 959, 626-195, 626-202, 'Rhode_Island'))
    stateButtonList.append(state(908, 937, 626-187, 626-200, 'Connecticut'))
    stateButtonList.append(state(898, 948, 626-220, 626-252, 'New_Jersey'))
    stateButtonList.append(state(820, 900, 626-137, 626-195, 'New_York'))
    stateButtonList.append(state(796, 885, 626-210, 626-248, 'Pennsylvania'))
    stateButtonList.append(state(725, 778, 626-235, 626-275, 'Ohio'))
    stateButtonList.append(state(675, 745, 626-119, 626-222, 'Michigan'))
    stateButtonList.append(state(674, 716, 626-238, 626-299, 'Indiana'))
    stateButtonList.append(state(617, 665, 626-240, 626-300, 'Illinois'))
    stateButtonList.append(state(585, 650, 626-140, 626-194, 'Wisconsin'))
    stateButtonList.append(state(518, 579, 626-90, 626-184, 'Minnesota'))
    stateButtonList.append(state(530, 604, 626-204, 626-250, 'Iowa'))
    stateButtonList.append(state(404, 503, 626-70, 626-130, 'North_Dakota'))
    stateButtonList.append(state(395, 507, 626-140, 626-200, 'South_Dakota'))
    stateButtonList.append(state(275, 380, 626-150, 626-230, 'Wyoming'))
    stateButtonList.append(state(237, 384, 626-84, 626-190, 'Montana'))
    stateButtonList.append(state(178, 242, 626-84, 626-190, 'Idaho'))
    stateButtonList.append(state(77, 177, 626-11, 626-75, 'Washington'))
    stateButtonList.append(state(51, 169, 626-114, 626-156, 'Oregon'))
    stateButtonList.append(state(405, 510, 626-210, 626-258, 'Nebraska'))



    return stateButtonList
    
