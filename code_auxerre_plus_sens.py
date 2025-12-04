import csv
f2008=[]
f2016=[]
f2021=[]
f2023=[]

#ouverture des différents fichier
with open('donnees_2008.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		f2008.append(row)

with open('donnees_2016.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		f2016.append(row)
		
with open('donnees_2021.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		f2021.append(row)
		
with open('donnees_2023.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=';')
	for row in reader:
		f2023.append(row)

#suppression de la ligne de descriptif
del f2008[0]
del f2016[0]
del f2021[0]
del f2023[0]

#récupération de la ligne Auxerre dans chaque fichier
for a in range(len(f2008)):
	for b in range(len(f2008[a])):
		if f2008[a][b]=="Auxerre":
			auxerre08=f2008[35574]
			print(auxerre08)

for a in range(len(f2016)):
	for b in range(len(f2016[a])):
		if f2016[a][b]=="Auxerre":
			auxerre16=f2016[34258]
			print(auxerre16)

for a in range(len(f2021)):
	for b in range(len(f2021[a])):
		if f2021[a][b]=="89024":
			auxerre21=f2021[33875]
			print(auxerre21)

for a in range(len(f2023)):
	for b in range(len(f2023[a])):
		if f2023[a][b]=="Auxerre":
			auxerre23=f2023[33855]
			print(auxerre23)




p_tot08=int(auxerre08[9])
p_tot16=int(auxerre16[9])
p_tot21=int(auxerre21[5])
p_tot23=int(auxerre23[10])
print(p_tot08,p_tot16,p_tot21,p_tot23)
print(type(p_tot08))

from pylab import figure,plot,show


#récupération de la ligne Sens dans chaque fichier
for a in range(len(f2008)):
	for b in range(len(f2008[a])):
		if f2008[a][b]=="Sens":
			Sens08=f2008[35914]
			print(Sens08)

for a in range(len(f2016)):
	for b in range(len(f2016[a])):
		if f2016[a][b]=="Sens":
			Sens16=f2016[34577]
			print(Sens16)

for a in range(len(f2021)):
	for b in range(len(f2021[a])):
		if f2021[a][b]=="89387":
			Sens21=f2021[34190]
			print(Sens21)

for a in range(len(f2023)):
	for b in range(len(f2023[a])):
		if f2023[a][b]=="Sens":
			Sens23=f2023[34170]
			print(Sens23)




p_toto08=int(Sens08[9])
p_toto16=int(Sens16[9])
p_toto21=int(Sens21[5])
p_toto23=int(Sens23[10])
print(p_toto08,p_toto16,p_tot21,p_toto23)
print(type(p_toto08))

from pylab import figure,plot,show
a_abscisse=[p_tot08,p_tot16,p_tot21,p_tot23]
a_ordonnée=[2008,2016,2021,2023]
s_abscisse=[p_toto08,p_toto16,p_toto21,p_toto23]
s_ordonnée=[2008,2016,2021,2023]
figure()
plot(a_ordonnée,a_abscisse)
plot(s_ordonnée,s_abscisse)
show()
