# InventoryService

![tests](https://github.com/annmproject/InventoryService/actions/workflows/tests.yml/badge.svg)

Inventory service for SWA project.

## Usage

Run service from published image:

```
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

## Dependencies

- `flask`
- `logging` (should be native)
- `unittest` (should be native)
- `requests`
- `os` (should be native)

## Build

To build and run tests use command : `sudo docker compose -f docker-compose.yml -f docker-compose.test.yml up --build`.

## Logging

Logs are printed to the standard output.

## API description

### Get all items

```HTTP
GET /inventory HTTP/1.1
Host: {{host}}
```

### Get item

- If item with ID does not exist the return code will be **404**. 
- In case everything is OK the return code will be **200**.

```HTTP
GET /inventory/{{id}} HTTP/1.1
Content-Type: application/json
Host: {{host}}
```

### Add new item

- If new item does not contain following keys: `["name", "cost", "quantity"]` the return code will be **400**. 
- In case everything is OK the return code will be **200**.

```HTTP
POST /inventory HTTP/1.1
Content-Type: application/json
Host: {{host}}
Content-Length: 73

{
    "name": "Item 3",
    "cost": 99,
    "quantity": 10,
}
```

### Delete item

- If item with ID does not exist the return code will be **404**. 
- In case everything is OK the return code will be **200**.

```HTTP
DELETE /inventory/{{id}} HTTP/1.1
Content-Type: application/json
Host: {{host}}
```

### Update item

- If item with ID does not exist the return code will be **404**.
- If you try to change ID the return code will be **400**.
- In case everything is OK the return code will be **200**.

```HTTP
PUT /inventory/{{id}} HTTP/1.1
Content-Type: application/json
Host: {{host}}
Content-Length: 28

{
    "name": "Item 3",
    "cost": 99,
    "quantity": 10,
}
```
