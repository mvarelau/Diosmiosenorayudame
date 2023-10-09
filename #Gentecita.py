#Gentecita
poblacion_pais_A= 25  # en millones
poblacion_pais_B = 18.9  # en millones
tasa_crecimiento_A = 0.02  
tasa_crecimiento_B = 0.03  
año = 2022
while poblacion_pais_A>poblacion_pais_B:
    poblacion_pais_A += poblacion_pais_A*tasa_crecimiento_A
    poblacion_pais_B += poblacion_pais_B*tasa_crecimiento_B
    año = año +1
    
print(f"En el año {año} la población del país B superará a la población del país A")
    
    
    

    
    

