#Caso 2 
    # Hacer un get a berry/2 
    # Verifi car que en fi rmness, el name sea super-hard 
    # Verifi car que el size sea mayor al del punto anterior 
    # Verifi car que el soil_dryness sea igual al del punto anterior
import requests

def test_prueba_berry2():

    berry1_url="https://pokeapi.co/api/v2/berry/1"
    respuesta1=requests.get(berry1_url)
    datosberry1=respuesta1.json()

    berry1_size=datosberry1['size']
    berry1_soil_dryness=datosberry1['soil_dryness']
    berry1_firmness_name=datosberry1['firmness']['name']

    berry2_url="https://pokeapi.co/api/v2/berry/2"
    respuesta2=requests.get(berry2_url)
    datosberry2=respuesta2.json()
    print(respuesta2.json())

    berry2_firmness_name=datosberry2['firmness']['name']
    berry2_size=datosberry2['size']
    berry2_soil_dryness=datosberry2['soil_dryness']
    print()

    assert berry2_firmness_name == 'super-hard'
    if berry2_firmness_name == 'super-hard':
        print("Verificamos que sea super-hard")
    else:
        print("No se verifica!!!")
    print()

    assert berry2_size > berry1_size
    if berry2_size > berry1_size:
        print("Size del Caso 2 es mayor al Size del Caso 1")
    else:
        print("Error garrafal")
    print()

    assert berry2_soil_dryness == berry1_soil_dryness 
    if berry2_soil_dryness == berry1_soil_dryness:
        print("Son iguales!!!!")
    else:
        print("No son iguales")

    print()

    print ("Se cumplen todos los Asserts")
    print()