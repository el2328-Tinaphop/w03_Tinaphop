#String Methods
Call_Sign = " king "
Massege = " EMERGENCY  RADIO "

#การจัดการ White Space
Clean_Call_Sign = Call_Sign.strip()
#print(Clean_Call_Sign)
#print(Call_Sign)

#การเปลี่ยนตัวพิมพ์
Upper_Call_Sign = Clean_Call_Sign.upper()
lower_Massege = Massege.lower()
print(Upper_Call_Sign)
print(lower_Massege)

#ตรวจสอบข้อความ
if "emergency" in lower_Massege :
    print("This is an emergency")