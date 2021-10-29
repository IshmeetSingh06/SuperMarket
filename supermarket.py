def show_menu():

	print("\nMY BAZAAR")
	print("Welcome to my Grocery Store!")
	print("Following are the products available in shop:")
	print( """               Code  Description  Category    Cost(Rs)
	           0     Tshirt       Apparels     500 
	           1     Trousers     Apparels     600
	           2     Scarf        Apparels     250
	           3     Smartphone   Electronics  20,000
	           4     Ipad         Electronics  30,000
	           5     Laptop       Electronics  50,000
	           6     Eggs         Eatables     5
	           7     Chocolate    Eatables     10
	           8     Juice        Eatables     100
	           9     Milk         Eatables     45""")


def get_regular_input():

	print("ENTER ITEMS YOU WISH TO BUY")
	X=input("enter the item codes space separatedly")
	X=X.split()

	return X


def get_bulk_input():
	print("\nEnter items and quantities")
	X=[]
	while True:
		itms= input("Enter code and quantity(leave a blank space to stop)")
		if itms==" ":
			break
		itms = itms.split()
		if int(itms[0])==0:
			print("You added",itms[1],"Tshirts")
		if int(itms[0])==1:
			print("You added",itms[1],"Trousers")
		if int(itms[0])==2:
			print("You added",itms[1],"Scarf")
		if int(itms[0])==3:
			print("You added",itms[1],"Smartphone")
		if int(itms[0])==4:
			print("You added",itms[1],"iPad")
		if int(itms[0])==5:
			print("You added",itms[1],"Laptop")
		if int(itms[0])==6:
			print("You added",itms[1],"Eggs")
		if int(itms[0])==7:
			print("You added",itms[1],"Chocolate")
		if int(itms[0])==8:
			print("You added",itms[1],"Juice")
		if int(itms[0])==9:
			print("You added",itms[1],"Milk")


		if int(itms[0])<0 or int(itms[0])>9 or int(itms[1])<0 :
			print("Invalid quantity")

		for i in range(int(itms[1]) ):
			X.append(itms[0])


	return X








def print_order_details(a,b,c,d,e,f,g,h,i,j):
	print("\n\nORDER DETAILS")
	z=1
	if a>0:
		print(z,"Tshirt x ",a,"= Rs 500 * ",a,"=",500*a)
		z=z+1
	if b>0:
		print(z,"Trousers x ",b,"= Rs 600 * ",b,"=",600*b)
		z = z + 1
	if c>0:
		print(z,"Scarf x ",c,"= Rs 250 * ",c,"=",250*c)
		z = z + 1
	if d>0:
		print(z,"Smartphone x ",d,"= Rs 20000 * ",d,"=",20000*d)
		z = z + 1
	if e>0:
		print(z,"ipad x ",e,"= Rs 30000  * ",e,"=",30000*e)
		z = z + 1
	if f>0:
		print(z,"Laptop x ",f,"= Rs 50000 * ",f,"=",50000*f)
		z = z + 1
	if g>0:
		print(z,"Eggs x ",g,"= Rs 5 * ",g,"=",5*g)
		z = z + 1
	if h>0:
		print(z,"Chocolate x ",h,"= Rs 10 * ",h,"=",10*h)
		z = z + 1
	if i>0:
		print(z,"Juice x ",i,"= Rs 100 * ",i,"=",100*i)
		z = z + 1
	if j>0:
		print(z,"Milk x ",j,"= Rs 45 * ",j,"=",45*j)
		z = z + 1







def calculate_category_wise_cost(a,b,c,d,e,f,g,h,i,j):
	print("\n\n Category Wise Costs")
	print("Apparel = Rs",a*500+b*600+c*250)
	print("Electronics = Rs",d*20000 + e*30000 + f*50000)
	print("Eatables = Rs",g*5 + h*10 + i*100 + j*45)


def get_discount(a,b,c,d,e,f,g,h,i,j):
	q=0
	x= a*500+b*600+c*250
	if x>=2000:
		q=0.1*x
	y= d*20000 + e*30000 + f*50000
	if y>=25000:
		q = q+ 0.1*y
	z= g*5 + h*10 + i*100 + j*45
	if z>=500:
		q = q+ 0.1*q
	return q





def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	print("\n \nDiscounts")

	if apparels_cost >= 2000:
		print("[APPAREL] Rs",apparels_cost,"- Rs",0.1*apparels_cost,"= Rs",apparels_cost-0.1*apparels_cost )
		apparels_cost=apparels_cost - apparels_cost*0.1
	if electronics_cost >= 25000:
		print("[Electronics] Rs",electronics_cost,"- Rs",0.1*electronics_cost,"= Rs",electronics_cost-0.1*electronics_cost )

		electronics_cost= electronics_cost- electronics_cost*0.1
	if eatables_cost >= 500:
		print("[EATABLES] Rs",eatables_cost,"- Rs",0.1*eatables_cost,"= Rs",eatables_cost-0.1*eatables_cost )

		eatables_cost=eatables_cost-eatables_cost*0.1

	print("TOTAL COST AFTER DISCOUNT= ",apparels_cost+electronics_cost+eatables_cost)
	return apparels_cost,electronics_cost,eatables_cost





def get_tax(cost, tax):

	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	print("\n\nTAX")
	print("[APPAREL] RS",apparels_cost,"* 0.10 = ",apparels_cost*0.1)
	print("[ELECTRONICS] RS ",electronics_cost,"* 0.15 =",electronics_cost*0.15)
	print("[EATABLES] RS ",eatables_cost,"* 0.05 =",eatables_cost*0.05)
	print("Total Tax = ",apparels_cost*0.1+eatables_cost*0.05+electronics_cost*0.15)
	print("Total cost =",apparels_cost+electronics_cost+eatables_cost+apparels_cost*0.1+electronics_cost*0.15+eatables_cost*0.05)

	return apparels_cost+electronics_cost+eatables_cost+apparels_cost*0.1+electronics_cost*0.15+eatables_cost*0.05




def apply_coupon_code(total_cost):
	print("\nCOUPON CODE")
	while True:
		coupon = input("Enter coupon code(else leave blank)")
		if coupon == "CHILLI50":
				if total_cost*0.5 > 10000:
					print("CHILLI50,min(10000,cost * 0.5)= Rs", 10000)
					print("TOTAL COUPON DISCOUNT = Rs", 10000)
					print("TOTAL COST = Rs", total_cost - 10000)
				elif total_cost*0.5< 10000:
					print("CHILLI50,min(5000,cost * 0.5)= Rs", total_cost*0.5)
					print("TOTAL COUPON DISCOUNT = Rs", total_cost*0.5)
					print("TOTAL COST = Rs", total_cost - total_cost*0.5)

				break

		if coupon == "HELLE25":
			if total_cost * 0.25 > 5000:
				print("HELLE25,min(5000,cost*0.25 = RS", 5000)
				print("TOTAL COUPON DISCOUNT = Rs", 5000)
				print("TOTAL COST = Rs", total_cost - 5000)
			else:
				print("HELLE25,min(5000,cost*0.25 = RS", total_cost*0.25)
				print("TOTAL COUPON DISCOUNT = Rs", total_cost*0.25)
				print("TOTAL COST = Rs", total_cost - total_cost*0.25)
			break
		if coupon==" ":
			break
		else:
			continue









def main():
	show_menu()


	while True:
		A = input("Would you like to buy in bulk? (y or Y/n or N)")
		if A=='Y' or A == 'y':
			X=get_bulk_input()
			break
		elif A=='n' or A=='N':
			X=get_regular_input()
			break
		else:
			continue

	a = X.count('0')
	b = X.count('1')
	c = X.count('2')
	d = X.count('3')
	e = X.count('4')
	f = X.count('5')
	g = X.count('6')
	h = X.count('7')
	i = X.count('8')
	j = X.count('9')
	print_order_details(a, b, c, d, e, f, g, h, i, j)
	calculate_category_wise_cost(a, b, c, d, e, f, g, h, i, j)
	q = get_discount(a, b, c, d, e, f, g, h, i, j)
	apparels_cost = a * 500 + b * 600 + c * 250
	electronics_cost = d * 20000 + e * 30000 + f * 50000
	eatables_cost = g * 5 + h * 10 + i * 100 + j * 45

	apparels_cost,electronics_cost,eatables_cost=calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)
	totalcost=calculate_tax(apparels_cost, electronics_cost, eatables_cost)
	apply_coupon_code(totalcost)
	print("\n\nThank you for visiting")






if __name__ == '__main__':
	main()
