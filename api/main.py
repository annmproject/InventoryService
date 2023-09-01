from flask import Flask, jsonify, request
from flasgger import Swagger
import logging
import os


# create Flask object
app = Flask(__name__)
Swagger(app)

# inventory
inventory = [
    {"id": 1, "name": "Item A", "cost": 457, "quantity": 10},
    {"id": 2, "name": "Item B", "cost": 333, "quantity": 5},
]

# get the port from the environment variable or use the default value (80)
port = int(os.environ.get("FLASK_PORT", 80))


@app.route('/inventory', methods=['GET'])
def get_items():
    """
        Get a list of all items
        ---
        responses:
          200:
            description: A list of items
    """
    logging.info("GET request received for all items")
    return jsonify(inventory), 200


@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
        Get an item by ID
        ---
        parameters:
          - name: item_id
            in: path
            type: integer
            required: true
            description: The ID of the item to retrieve
        responses:
          200:
            description: The item with the specified ID
          404:
            description: Item not found
    """
    logging.info(f"GET request received for item with ID {item_id}")
    item = next((item for item in inventory if item["id"] == item_id), None)
    if item is None:
        logging.warning(f"Item with ID {item_id} not found")
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@app.route('/inventory', methods=['POST'])
def create_item():
    """
        Create a new item
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the item
                cost:
                  type: number
                  description: The cost of the item
                quantity:
                  type: integer
                  description: The quantity of the item
        responses:
          200:
            description: The newly created item
          400:
            description: Missing required keys in JSON payload
    """
    logging.info("POST request received to create a new item")
    new_item = request.json
    required_keys = ["name", "cost", "quantity"]
    if not all(key in new_item for key in required_keys):
        logging.error("Missing required keys in JSON payload")
        return jsonify({"error": "Missing required keys"}), 400
    else:
        if len(inventory) == 0:
            new_item["id"] = 1
        else:
            new_item["id"] = inventory[-1]["id"] + 1
        inventory.append(new_item)
        logging.info(f"New item with ID {new_item['id']} created successfully")
        return jsonify(new_item), 200


@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
        Delete an item by ID
        ---
        parameters:
          - name: item_id
            in: path
            type: integer
            required: true
            description: The ID of the item to delete
        responses:
          200:
            description: Item deleted successfully
          404:
            description: Item not found
    """
    item = next((item for item in inventory if item["id"] == item_id), None)
    if item is None:
        logging.warning(f"Item with ID {item_id} not found")
        return jsonify({"error": "Item not found"}), 404
    else:
        inventory.remove(item)
        logging.info(f"Item with ID {item_id} deleted")
        return jsonify({"message": "Item deleted"}), 200


@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
        Update an item by ID
        ---
        parameters:
          - name: item_id
            in: path
            type: integer
            required: true
            description: The ID of the item to update
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: The ID of the item (readonly)
                name:
                  type: string
                  description: The name of the item
                cost:
                  type: integer
                  description: The cost of the item
                quantity:
                  type: integer
                  description: The quantity of the item
        responses:
          200:
            description: The updated item
          400:
            description: Cannot update 'id' field
          404:
            description: Item not found
    """
    item = next((item for item in inventory if item["id"] == item_id), None)
    updated_data = request.json
    if item is None:
        logging.warning(f"Item with ID {item_id} not found")
        return jsonify({"error": "Item not found"}), 404
    if "id" in updated_data and updated_data["id"] != item_id:
        logging.warning(f"Cannot update 'id' field for item with ID {item_id}")
        return jsonify({"error": "Cannot update 'id' field"}), 400
    item.update(updated_data)
    logging.info(f"Item with ID {item_id} updated")
    return jsonify(item), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)



