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

Numbers = [1,2,3,4,5,6,7,8,9,0]
Num_Reverse = Number.Reverse()
Num_Sort = Number.Sort(Reverse=True)
Num_Copy = Number.Copy()
print(Numbers)
print(Num_Reverse)
print(Num_Sort)
