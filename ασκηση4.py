number=int(input("dvse ton arithmo: "))
latin=""

if number <=0 or number > 1000000:
	print ("den yposthrizetai h metatraph aytoy toy arithmoy")
else:
		if number == 1000000:
			latin += "M_"
			number %=1000000
		if number>=100000:
			psifio = (number//100000)
			if psifio == 9:
				latin += "C_M_"
			elif psifio >=5:
				latin +="D_"
				for i in range (0,(psifio-5),1):
					latin +="C_"
			elif psifio ==4 :
				latin +="C_D_"
			elif psifio >=1:
				for i in range (0,psifio,1):
					latin+="C_"
		number %=100000
		if number >= 10000:
			psifio = (number//10000)
			if psifio == 9:
				latin +="X_C_"
			elif psifio >=5:
				latin +="L_"
				for i in range (0,(psifio-5),1):
					latin +="X_"
			elif psifio ==4 :
				latin +="X_L_"
			elif psifio>=1:
				for i in range (0,psifio,1):
					latin +="X_"
		number %=10000
		if number >=1000:
			psifio = (number//1000)
			if psifio == 9:
				latin +="I_X_"
			elif psifio >=5:
				latin +="V_"
				for i in range (0,(psifio-5),1):
					latin +="M"
			elif psifio ==4 :
				latin +="MV_"
			elif psifio >=1:
				for i in range (0,psifio,1):
					latin +="M"
		number %=1000
		if number >= 100:
			psifio = (number//100)
			if psifio == 9:
				latin +="CM"
			elif psifio >=5:
				latin +="D"
				for i in range (0,(psifio-5),1):
					latin +="C"
			elif psifio ==4 :
				latin +="CD"
			elif psifio>=1:
				for i in range (0,psifio,1):
					latin +="C"
		number %=100
		if number >=10:
			psifio = (number//10)
			if psifio == 9:
				latin +="XC"
			elif psifio >=5:
				latin +="L"
				for i in range (0,(psifio-5),1):
					latin +="X"
			elif psifio ==4 :
				latin +="XL"
			elif psifio >=1:
				for i in range (0,psifio,1):
					latin +="X"
		number %=10
		if number >=1:
			psifio = number
			if psifio == 9:
				latin +="IX"
			elif psifio >=5:
				latin +="V"
				for i in range (0,(psifio-5),1):
					latin +="I"
			elif psifio ==4 :
				latin +="IV"
			elif psifio >=1:
				for i in range (0,psifio,1):
					latin +="I"

print (latin)
