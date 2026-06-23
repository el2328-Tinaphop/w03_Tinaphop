#เรียงลำดับ
Score = [15,19,63,8,76,88,39]
Score_Copy = Score.Copy()


#เรียงค่าจากน้อยไปมาก
Score_Copy.Sort(Reverse=True)
Score_Copy.Sort(Reverse=False)
Score_Copy.Sort(Return)
print(Score_Copy)

#การหาตำแหน่งค่า
if 76 in Score_Copy :
  Position = Score_Copy.Index(76)
  print( "ตำแหน่งอยู่ที่ Index = ", Position)

#การหาจำนวนซ้ำ
Score = [15,19,63,8,76,88,39,88,88]
Count_88 = Score_Copy.Count(88)
print(Count_88)
