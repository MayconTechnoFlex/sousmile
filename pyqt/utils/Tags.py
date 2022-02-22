###########################################################################
"""Module with all functions used on the InOutScreen of the application"""
###########################################################################
from typing import List
################################################
# Tag lists - used on buttons
#########################################################
Tag_List = [
    "HMI.SideA.ModeValue",
    "HMI.SideB.ModeValue"
]
#########################################################
# Tags Local - In/Out
#########################################################
tags_inOut: List[str] = []

for i in range(0, 3):
    for j in range(0, 16):
        if i == 0:
            tags_inOut.append(f"Local:1:I.Data.{j}")
        elif i == 1:
            tags_inOut.append(f"Local:1:O.Data.{j}")
        elif i == 2:
            if j <= 7:
                tags_inOut.append(f"Local:2:I.Data.{j}")
#########################################################