import json
import random
import json
import os
import random
import names
import importlib.resources

states = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawái', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Luisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Míchigan', 'MN': 'Minnesota', 'MS': 'Misisipi',
    'MO': 'Misuri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
    'NH': 'Nuevo Hampshire', 'NJ': 'Nueva Jersey', 'NM': 'Nuevo México',
    'NY': 'Nueva York', 'NC': 'Carolina del Norte', 'ND': 'Dakota del Norte',
    'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregón', 'PA': 'Pensilvania',
    'RI': 'Rhode Island', 'SC': 'Carolina del Sur', 'SD': 'Dakota del Sur',
    'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'Virginia Occidental',
    'WI': 'Wisconsin', 'WY': 'Wyoming'
}

class XMap:
    _data = None
    _current = None

    @classmethod
    def _load_data(cls):
        if cls._data is None:
            with importlib.resources.files('XetMap.data').joinpath('usa.json').open('r', encoding='utf-8') as f:
                data = json.load(f)
                cls._data = data['addresses']

    @classmethod
    def LoadMap(cls):
        cls._load_data()
        cls._current = random.choice(cls._data)

    @classmethod
    def GetMap(cls, key: str):
        if cls._current is None:
            cls.LoadMap()
        if key == 'state':
            stid = cls._current.get('StateCode', None)
            return states.get(stid.upper()) if stid else None
        if key == 'Phone':
            return str(random.randint(9876655444, 9998765433))
        if key == 'User':
            return f"{names.get_first_name()}asdasdasd{random.randint(100,200)}"
        if key == 'Mail':
            return f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999999)}@gmail.com"
        if key == 'Pass':
            return f'{names.get_first_name()}##{random.randint(10,90)}'
        if key == 'Fname':
            return names.get_first_name()
        if key == 'Lname':
            return names.get_last_name()
        return cls._current.get(key, None)


