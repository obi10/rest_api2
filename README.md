# Data Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all data

**Definition**

`GET /data`

**Response**

- `200 OK` on success

```json
[
    {
        "id": "madhack001",
        "num_personas": "2",
        "estado": "lleno",
        "tiempo": "11/11/2019, 14:06:12",
        "ip": "192.168.0.2"
    },
    {
        "id": "madhack002",
        "num_personas": "1",
        "estado": "vacio",
        "tiempo": "11/11/2019, 16:11:10",
        "ip": "192.168.0.3"
    }
]
```

### Registering a new data

**Definition**

`POST /data`

**Arguments**

- `"id":string` a globally unique identifier for this device
- `"num_personas":string` cantidad de personas detectadas por la camara
- `"estado":string` vacio o lleno
- `"tiempo":string` tiempo en que se envia la data al servidor remoto
- `"ip":string` the IP address of the device's controller

If a data with the given identifier(id) already exists, the existing device will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "id": "madhack002",
    "num_personas": "1",
    "estado": "vacio",
    "tiempo": "11/11/2019, 16:11:10",
    "ip": "192.168.0.3"
}
```

## Lookup data details

`GET /data/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
    "id": "madhack002",
    "num_personas": "1",
    "estado": "vacio",
    "tiempo": "11/11/2019, 16:11:10",
    "ip": "192.168.0.3"
}
```

## Delete a data

**Definition**

`DELETE /data/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success