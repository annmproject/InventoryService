# InventoryService

Inventory service for SWA project.

## API description

### Get all items

```HTTP
GET /inventory HTTP/1.1
Host: {{host}}
```

### Get item

If item with ID does not exist the return code will be **404**. 
In case everything is OK the return code will be **200**.

```HTTP
GET /inventory/{{id}} HTTP/1.1
Content-Type: application/json
Host: {{host}}
```

### Add new item

If new item does not contain following keys: `["name", "cost", "quantity"]` the return code will be **400**. 
In case everything is OK the return code will be **200**.

```HTTP
POST /users HTTP/1.1
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

If item with ID does not exist the return code will be **404**. 
In case everything is OK the return code will be **200**.

```HTTP
DELETE /users/{{id}} HTTP/1.1
Content-Type: application/json
Host: {{host}}
```

### Update item

If item with ID does not exist the return code will be **404**.
If you try to change ID the return code will be **400**.
In case everything is OK the return code will be **200**.

```HTTP
PUT /users/{{id}} HTTP/1.1
Content-Type: application/json
Host: {{host}}
Content-Length: 28

{
    "name": "Item 3",
    "cost": 99,
    "quantity": 10,
}
```
