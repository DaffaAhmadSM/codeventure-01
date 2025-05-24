# myName = "Raehan"
# myHobby = "Coding"
# myList = ["Ihsan", "Tian", "Daffa", "Firdaus"]
# myTuple = ("")

# print(f'Nama saya: , {myName}, Hobi saya adalah {myHobby}')
# print(f'Hasil dari penjumlahan 5 dan 6 adalah {5+6}')
# for name in myList:
#     print(name)


# nama3 = myList[2]
# num1 = myList[4]
# float1 = myList[6]
# namaTeman = myList[0]
# # namaTeman / namateman / nama_teman

# myList2 = myList.pop(0)
# myList.append(5.8)
# myList.append(699)
# myList.remove("Nanda")
# # myList.clear()

# print(nama3)
# print(num1)
# print(myList2)
# print(myList)
# print(f'Jumlah list: {len(myList)}')



myList = ["Alfi", "Nanda", "Sabil", 23, 45, 55, 2.4]

def add(list, value):
    list.append(value)
    return list

def remove(list, value):
    list.remove(value)
    return list

def func3(list):
    for i in list:
        if type(i) == str:
            print(i)
        else:
            print("not a string")

# myNewList = add(myList,'Sabtu')
# myNewList1 = remove(myList, 55)
# print(f"List baru: {myNewList} dan {myNewList1}")

func3(myList)