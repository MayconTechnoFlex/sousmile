"""Módulo para lista de tags"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import List
#######################################################################################################
# TagList geral
#######################################################################################################
Tag_List = [
    "HMI.SideA.ModeValue",
    "HMI.SideB.ModeValue",
    "HMI.HoldRobo",
    "HMI.EnableLog",
    "HMI.btn_Sub1mm",
    "HMI.btn_EndCheckUF",
    "Cyl_DoorSideA.ManRet",
    "Cyl_DoorSideA.ManExt",
    "Cyl_DoorSideA.MaintTest",
    "Cyl_DoorSideB.ManRet",
    "Cyl_DoorSideB.ManExt",
    "Cyl_DoorSideB.MaintTest",
    "Cyl_SpindleRobo.ManExt",
    "Cyl_SpindleRobo.MaintTest",
    "BarCodeReader.Data",
    "In_SegLadoA",
    "In_SegLadoB"
]
#######################################################################################################
# TagList de Entradas e Saídas
#######################################################################################################
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
#######################################################################################################
# TagList de alarmes
#######################################################################################################
alarm_tag_list: List[str] = []

for i in range(0, 4):
    for j in range(0, 32):
        alarm_tag_list.append(f"AlarmProcess[{i}].{j}")
#######################################################################################################