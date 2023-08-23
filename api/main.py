from flask import Flask, jsonify, request
import logging
import os


# create Flask object
app = Flask(__name__)

# inventory
inventory = [
    {"id": 1, "name": "Item A", "cost": 333, "quantity": 10},
    {"id": 2, "name": "Item B", "cost": 333, "quantity": 5},
]

# get the port from the environment variable or use the default value (80)
port = int(os.environ.get("FLASK_PORT", 80))


@app.route('/inventory', methods=['GET'])
def get_items():
    logging.info("GET request received for all items")
    return jsonify(inventory), 200


@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    logging.info(f"GET request received for item with ID {item_id}")
    item = next((item for item in inventory if item["id"] == item_id), None)
    if item is None:
        logging.warning(f"Item with ID {item_id} not found")
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@app.route('/inventory', methods=['POST'])
def create_item():
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
    app.run(host='0.0.0.0', port=port)


