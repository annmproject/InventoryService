import unittest
import requests


class TestAppIntegration(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://api"

    def test_full_flow(self):

        # get all data
        response = requests.get(f"{self.base_url}/inventory")
        self.assertEqual(response.status_code, 200)

        # get existing item with ID 1
        response = requests.get(f"{self.base_url}/inventory/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Item A")

        # get non-existing item with ID 9999
        response = requests.get(f"{self.base_url}/inventory/9999")
        self.assertEqual(response.status_code, 404)

        # create item without all fields
        response = requests.post(f"{self.base_url}/inventory", json={"name": "New Item", "cost": 100})
        self.assertEqual(response.status_code, 400)

        # create item with all fields
        response = requests.post(f"{self.base_url}/inventory", json={"name": "New Item", "cost": 100, "quantity": 1})
        self.assertEqual(response.status_code, 200)

        # get ID of created item
        new_item_id = response.json()['id']

        # update quantity of new item
        response = requests.put(f"{self.base_url}/inventory/{new_item_id}", json={"quantity": 10})
        self.assertEqual(response.status_code, 200)

        # get data of updated item again
        response = requests.get(f"{self.base_url}/inventory/{new_item_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['quantity'], 10)

        # try to update id of new item
        response = requests.put(f"{self.base_url}/inventory/{new_item_id}", json={"id": 0})
        self.assertEqual(response.status_code, 400)

        # try to update non-existing item
        response = requests.get(f"{self.base_url}/inventory/9999")
        self.assertEqual(response.status_code, 404)

        # try to delete non-existing item
        response = requests.delete(f"{self.base_url}/inventory/9999")
        self.assertEqual(response.status_code, 404)

        # try to delete new item
        response = requests.delete(f"{self.base_url}/inventory/{new_item_id}")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
