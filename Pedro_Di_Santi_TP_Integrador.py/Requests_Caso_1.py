#Caso 1 
# Hacer un get a berry/1 
# Verifi car que el size sea 20 
# Verifi car que el soil_dryness sea 15 
# Verifi car que en fi rmness, el name sea soft.

import requests

def test_prueba_berry1():
    berry1_url="https://pokeapi.co/api/v2/berry/1"
    respuesta=requests.get(berry1_url)
    datosberry1=respuesta.json()
    print(respuesta.json())

    berry1_size=datosberry1['size']
    berry1_soil_dryness=datosberry1['soil_dryness']
    berry1_firmness_name=datosberry1['firmness']['name']
    print()
    
    assert berry1_size == 20
    if berry1_size==20:
        print("Verificamos berry1 size")
    else:
        print("No verificamos")
    print()
    
    assert berry1_soil_dryness == 15
    if berry1_soil_dryness == 15:
        print("Verificamos berry1 soildryness")
    else:
        print("No verificamos")
    print()
    
    assert berry1_firmness_name == 'soft'
    if berry1_firmness_name =='soft':
        print("Verificamos berry1_firmness_name")
    else:
        print("No verificamos berry1_firmness_name")
    print()

    print ({berry1_size},{berry1_soil_dryness},{berry1_firmness_name})

    

   