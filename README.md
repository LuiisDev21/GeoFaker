# GeoFaker

GeoFaker es una librería de Python diseñada para trabajar con direcciones reales seleccionadas a partir de conjuntos de datos públicos, verificadas mediante servicios de geocodificación como la API de Google Maps. Su propósito es ofrecer datos de direcciones auténticas que se resuelven correctamente al ser geocodificadas, lo que resulta útil para pruebas, simulaciones o demostraciones que requieran ubicaciones verídicas sin comprometer datos personales.

Además de direcciones reales, GeoFaker también genera datos aleatorios complementarios como nombres, números de teléfono, direcciones de correo electrónico y otros detalles típicos de perfiles, permitiendo crear conjuntos de datos más completos y realistas para entornos de desarrollo o pruebas de sistemas que manejen información personal ficticia pero coherente.

## Instalación

Puedes instalar GeoFaker usando pip:

```sh
pip install GeoFaker
```

## Uso

```python
from GeoFaker import XMap

# Cargar una nueva instancia ./utils, defs....
def XmapNewInstance():
    try:
        XMap.LoadMap()
        return {
            "street": XMap.GetMap("address1"),
            "city": XMap.GetMap("city"),
            "state": XMap.GetMap("state"),
            "stid": XMap.GetMap("StateCode"),
            "zipp": XMap.GetMap("PostalCode"),
            "num": XMap.GetMap("Phone"),
            "usuario": XMap.GetMap("User"),
            "password": XMap.GetMap("Pass"),
            "mail": XMap.GetMap("Mail"),
            "name": XMap.GetMap("Fname"),
            "last": XMap.GetMap("Lname"),
        }
    except Exception as e:
        print(f"Error loading XMap data: {e}")
        return None


# Uso en tu proyecto
try: 
    NewMap  = XmapNewInstance()
    street = NewMap['street']
    city = NewMap['city']
    stid = NewMap['stid']
    zipp = NewMap['zipp']
    state = NewMap['state']
    num = NewMap['num']
    usuario = NewMap['usuario']
    password = NewMap['password']
    mail = NewMap['mail']
    name = NewMap['name']
    last = NewMap['last']
except Exception as u:
    print(f"Error getting Xmap data: {e}")
    return None

```

## Estructura del Proyecto

```
GeoFaker/
    __init__.py
    Func.py
    data/
        usa.json
README.md
setup.py
```

- `Func.py`: Lógica principal de la clase `XMap`.
- `data/usa.json`: Dataset de direcciones de EE.UU.
- `setup.py`: Script de instalación.
- `README.md`: Este archivo.

## Requisitos

- Python >= 3.10
- [names](https://pypi.org/project/names/)
- Json

---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# GeoFaker (English)

GeoFaker is a Python library designed to work with real-world addresses selected from public datasets, verified using geocoding services such as the Google Maps API. Its purpose is to provide authentic address data that resolves correctly when geocoded, making it ideal for testing, simulations, or demonstrations that require realistic locations without compromising personal information.

In addition to real addresses, GeoFaker also generates complementary random data such as names, phone numbers, email addresses, and other typical profile details—allowing you to create richer, more realistic datasets for development or testing environments involving fictitious but coherent personal information.

## Installation

You can install GeoFaker using pip:

```sh
pip install GeoFaker
```

## Usage

```python
from GeoFaker import XMap

# Load a random address
XMap.LoadMap()

# Get different data from the current address
print(XMap.GetMap('address1'))   # Main address
print(XMap.GetMap('city'))       # City
print(XMap.GetMap('state'))      # State
print(XMap.GetMap('PostalCode')) # Postal code
print(XMap.GetMap('Phone'))      # Random phone
print(XMap.GetMap('User'))       # Random user
print(XMap.GetMap('Mail'))       # Random email
print(XMap.GetMap('Pass'))       # Random password
print(XMap.GetMap('Fname'))      # Random first name
print(XMap.GetMap('Lname'))      # Random last name
```

## Project Structure

```
GeoFaker/
    __init__.py
    Func.py
    data/
        usa.json
README.md
setup.py
```

- `Func.py`: Main logic of the `XMap` class.
- `data/usa.json`: US address dataset.
- `setup.py`: Installation script.
- `README.md`: This file.

## Requirements

- Python >= 3.10
- [names](https://pypi.org/project/names/)
- Json

---
