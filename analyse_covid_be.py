import pandas as pd 
import matplotlib.pyplot as plt

# fait dataframe pour la liste entière 
ted_data = pd.read_csv('covid.csv')
covid = pd.read_csv('covid.csv')
pd.set_option('display.max_rows',11)

# fait mon filtre spécifique belgique
fil_pays = (covid['countriesAndTerritories']=='Belgium') 
liste_deces = covid.loc[fil_pays,['countriesAndTerritories','dateRep','cases','deaths']]

# retourne ma liste avec la belgique qui comprend la date les cas et nombre de déces
# ajouter tous les valeurs dans une liste
deces = liste_deces.to_dict()

def date():
    date = deces['dateRep']
    list_date  = list()
    for i in date.values():
        list_date.append(i)
    return list_date 

def cas():
    nbr_cas = deces['cases']
    list_cas = list()
    for i in nbr_cas .values():
        list_cas .append(i)
    return list_cas

def mort():
    nbr_mort = deces['deaths']
    list_mort = list()
    for i in nbr_mort.values():
        list_mort.append(i)
    return list_mort

# mes donnes sont tous desormais dans une liste

c_date = date()
c_cas = cas()
c_mort = mort()

plt.title('Covid-19 pour belgique')
plt.scatter(c_date,c_cas,label='Covid-19')
plt.scatter(c_date,c_mort,label='Covid-19')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
