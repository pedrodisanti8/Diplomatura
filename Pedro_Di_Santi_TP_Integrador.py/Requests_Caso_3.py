 #Caso 3
    # Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/) 
    # Verifi car que su experiencia base es mayor a 10 y menor a 1000 
    # Verifi car que su tipo es “electric”
import requests

def test_prueba_pikachu():
    pikachu_url="https://pokeapi.co/api/v2/pokemon/pikachu/"
    response=requests.get(pikachu_url)
    datospikachu=response.json()
    #print(response.json())

    pikachu_tipo = [t["type"]["name"] for t in datospikachu.get("types", []) if "type" in t and "name" in t["type"]]
    pikachu_exp=datospikachu['base_experience']
    print()

    assert 'electric' in pikachu_tipo
    if 'electric' in pikachu_tipo:
        print("Verificamos con el 'Tipo' es electric!!")
    else:
        print("No pudimos verificarlo, lo lamentamos mucho!")
    print()

    assert 10 < pikachu_exp < 1000 
    if 10 < pikachu_exp and pikachu_exp < 1000:
        print("Esta dentro de los parametros!!")
    else:
        print("No cumple con lo solicitado")
    print()

    print(f"Tipo: {pikachu_tipo}", f"Exp : {pikachu_exp}")