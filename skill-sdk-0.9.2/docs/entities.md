# Entities

An intent can have optional arguments called entities. Entities are passed to the skill in an invoke call and their type is defined in the intent definition.

## Overview of the entities included in the SDK

Due to their semantic (because almost every entity can have multiple values), entities are passed to the skill as **string arrays**, 
and can be converted to a native Python representation using helper functions defined in `skill_sdk.entities` module.

Here is overview of the entity types included in SDK:

### "Location" entities

Location entities are converted to a `skill_sdk.entities.Location` instance.

- **Input**: City name (for example "Erste Strasse 1, Berlin)"
  - Optionally, when the `Location` is instantiated directly,  `coordinates` are accepted as a tuple of float latitude and longitude
- **Output**: `skill_sdk.entities.Location` instance
  
  **Example**

    ```python
    >>> loc = Location("Berlin")

    >>> loc.text
    'Berlin'

    >>> loc.coordinates
    (52.4773614, 13.4265271)

    >>> loc.timezone
    'Europe/Berlin'
    ```
    - `Loc.text`: Free text value as transmitted in the request
  - `Loc.coordinates`: Returns a tuple of latitude and longitude as float with the geographic location of the city
  - `Loc.timezone`: Time zone name of the city as text


### Timedelta entities

Timedelta entities represent a time duration in ISO format. They can be converted to `datetime.timedelta` objects.

- **Input**: Duration, format: "1H12M10S" for 1 hour, 12 minutes and 10 seconds
- **Output**: `datetime.timedelta` instance

**Example**

```python
>>> isodate.parse_duration("PT10M")
datetime.timedelta(0, 600)

>>> isodate.parse_duration("PT10H12M24S")
datetime.timedelta(0, 36744)
```

### Boolean entities

Entities `bool` convert values like "yes", "no", 0, 1, "true", "false", etc. to a boolean. 

- **Input**: Yes, No, 1, 0, etc.
- **Output**: bool, True or False


### "Device" entities

Entities of type `Device` represent a client device identified by a name. 

- **Input**: device name
- **Output**: `skill_sdk.entities.Device` instance

### "Rank" entities

Rank entities are representing a "generic order" concept ("Minimum", "Maximum", "Preceding", "Succeeding") and ordinal numbers ("First", "Second", "Third", etc.)
They are converted to integer values corresponding to similar Python "slice" indices:

| Order | Ordinal   | Value |
|-------|-----------|------:|
| "min" | "First"   |   0   |
|       | "Second"  |   1   |
|       | "Third"   |   2   |
|       | **n**<sup>th</sup>| n-1|
| "max" |           |   -1  |
| "prec"|           |   -2  |


### String entities

String entities are being simply passedto the implementation function as a string without conversion. 

- **Input**: String (for example "Hello, World")
- **Output**: Same string (for example "Hello, World")

The value is passes as string array without modification and can be manually converted to native Python objects using the following helpers: 

### Helper functions

* entities.get_value(entities: Union[List, Tuple]) -> str
    
    Silently returns first element from entities list. Will return unchanged value if passed parameter is not an instance of list or tuple.
    
* entities.to_datetime(value: Union[List, AnyStr, datetime.date, datetime.time]) -> datetime.datetime

    Gently parses ISO-formatted datetime string and returns datetime value. 
    If value is a list, will apply `entities.get_value` to get first element of the list.
    
    The parsing is relaxed so that: if year is omitted, the datetime object is extended with the current year,
        if day is omitted - the current day is added to resulting datetime object.
    
    If value is a datetime.date, the datetime object is extended with "00:00" timestamp.
    If value is a datetime.time, the datetime object is extended with current date.
    
    ```python
    >>> entities.to_datetime('2106-12-31T12:30')
    datetime.datetime(2106, 12, 31, 12, 30)

    >>> entities.to_datetime(['--12-31'])
    datetime.datetime(2019, 12, 31, 0, 0)

    >>> entities.to_datetime(['17:30'])
    datetime.datetime(2019, 3, 5, 17, 30)
    ```
    
* entities.to_date(value: Union[List, AnyStr, datetime.datetime]) -> datetime.date

    Gently parses ISO-formatted datetime string and returns the date value. 
    If value is a list, will apply `entities.get_value` to get first element of the list.

    The parsing is relaxed so that: if year is omitted, the date object is extended with the current year,
        if day is omitted - the current day is added to resulting date object.
    
    If value is a datetime.datetime, the time part is trimmed.
    
    ```python
    >>> entities.to_date('2106-12-31T12:30')
    datetime.date(2106, 12, 31)

    >>> entities.to_date(['--12-31'])
    datetime.date(2019, 12, 31)
    ```
    
* entities.to_time(value: Union[List, AnyStr, datetime.datetime]) -> datetime.time

    Gently parses ISO-formatted datetime string and returns the time value. 
    If value is a list, will apply `entities.get_value` to get first element of the list.

    If value is a datetime.datetime, the date part is trimmed. 
    If value is a dateime.date (no time part), simple "00:00" timestamp is returned.
    
    ```python
    >>> entities.to_time('2106-12-31T12:30')
    datetime.time(12, 30)

    >>> entities.to_time(['--12-31'])
    datetime.time(0, 0)

    ```
    
* entities.on_off_to_boolean(value: str) -> bool

    Converts ON_OFF entity value to boolean.
    
* entities.rank(value: str) -> int

    Converts RANK entity value to integer.
    
* entities.convert(value: str, to_type: Union[bool, datetime, int, float, Callable]) -> Any
    
    Generic converter: converts value to one of primitive types or any other type if conversion function supplied as `to_type` parameter.

**Example**

```python
from typing import List
from skill_sdk import Response, entities, skill

@skill.intent_handler("WEATHER_CURRENT")
def weather(date_list: List[str]) -> Response:
    # Return the weather forecast for a number of days
    my_dates = [entities.to_datetime(date) for date in date_list]
    # Or if we only need a single date:
    my_date = entities.to_datetime(date_list)
    ...
```

## Simplifying entities handling with decorators 

To simplify the entities parsing and conversion, you can use the following decorator

### Intent handler decorator: "@skill.intent_handler"

The decorator `@intent_handler` uses type hints from the handler definition and converts the entities list into the specified type.
The following types are supported:
- `datetime.timedelta`
- `datetime.datetime` / `datetime.date` / `datetime.time`
- `int` / `float` / `bool`

**Examples**

To receive an entity converted to a single `datetime.timedelta` value:

   ```python
import datetime
from skill_sdk import Context, Response, skill

@skill.intent_handler('WEATHER__CURRENT')
def intent_handler_expecting_timedelta(context: Context, timedelta: datetime.timedelta) -> Response:
    ...
   ```

To receive a list of `datetime.date` values:

   ```python
import datetime
from skill_sdk import Context, Response, skill

@skill.intent_handler('WEATHER__CURRENT')
def intent_handler_expecting_dates_list(context: Context, date_list: [datetime.date]) -> Response:
    ...
   ```

By default, `intent_handler` decorator suppresses conversion errors and returns an instance of 
`EntityValueException` exception, if conversion error occurs. 

You may add your own error handler to the `intent_handler` decorator to handle exceptions yourself:

```python
def date_error(name, value, exception) -> responses.Response:
    return f"Wrong {name} value: {value}, exception {exception.__cause__}"

@skill.intent_handler('Test_Intent', error_handler=date_error)
def handler(date: datetime.date = None) -> responses.Response:
  ...
```

## Nested and overlapping entities

Some entities might have the values that are nesting in or overlapping each other.
For example, the utterance "Turn on Super RTL" has two overlapping values for a `channel` entity: "RTL" and "Super RTL" 
(both are valid channel names)

To distinguish their nesting, skill may request entity values in `AttributeV2` format.
`AttributeV2` is a data structure that contains, along with the entity value, 
the unique index and pointers to other entities, that might contain or overlap this entity.

Here is an example of two entity values for "Turn on Super RTL" utterance in `AttributeV2` format:
 
```json   
    "attributesV2": {
      "channel": [
        {
          "id": 1,
          "value": "super rtl",
          "nestedIn": [],
          "overlapsWith": []
        },
        {
          "id": 2,
          "value": "rtl",
          "nestedIn": [
            1
          ],
          "overlapsWith": []
        }
      ]
    }
```   

To receive the values in `AttributeV2` format, use the type hints when decorating your intent handler with `@intent_handler`.

If you want to receive a list of `AttributeV2` values:

```python
from typing import List
from skill_sdk import entities, Response, skill

@skill.intent_handler('TV__INTENT')
def intent_handler_expecting_list_of_attributes_v2(channel: List[entities.AttributeV2]) -> Response:
    ...
```

To receive a single value (first one will be returned from the list):

```python
from skill_sdk import entities, Response, skill

@skill.intent_handler('TV__INTENT')
def intent_handler_expecting_single_attribute_v2(channel: entities.AttributeV2) -> Response:
    ...
```

To receive a list of `AttributeV2` that are definitely holding integer values: 

```python
from typing import List
from skill_sdk import entities, Response, skill

@skill.intent_handler('TV__INTENT')
def intent_handler_expecting_single_attribute_v2(channel: List[entities.AttributeV2[int]]) -> Response:
    ...
```
