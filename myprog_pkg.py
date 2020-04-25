#!/usr/bin/python
import my_pkg

if __name__ == "__main__":

	while(1):
		num = (int)(input("Select menu: 1) convserion 2) union/intersection 3) exit? "))
		if(num not in range(1, 4)):
			print("not in menu!") 
			continue

		if(num == 1):
			binnum = (int)(input("input binary number : "))
			print("=> OCT> ",my_pkg.OCT(binnum))
			print("=> DEC> ",my_pkg.DEC(binnum))
			print("=> HEX> ",my_pkg.HEX(binnum))
		elif(num == 2):
			list1 = input("1st list: ")
			list1 = list1[1:-1].split(',')
			for i in list1:
				list1[list1.index(i)] = i.strip()
			list2 = input("2nd list: ")
			list2 = list2[1:-1].split(',')
			for i in list2:
				list2[list2.index(i)] = i.strip()

			print("=> union ", my_pkg.union(list1, list2))
			print("=> intersection ", my_pkg.intersection(list1, list2))
		else:
			print("exit the program...")
			break
