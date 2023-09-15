import requests

# Test CREATE operation
new_person = {"name": "John Doe"}
response = requests.post("http://10.0.0.176:5050/api", json=new_person)

print("Response Status Code:", response.status_code)
print("Response Content:", response.text)

assert response.status_code == 201  # Ensure a successful creation

# Test READ operation
response = requests.get("http://10.0.0.176:5050/api/1")  # Assuming '1' is a valid user_id
assert response.status_code == 200  # Ensure a successful retrieval

# Test UPDATE operation
updated_person = {"name": "Updated Name"}
response = requests.put("http://10.0.0.176:5050/api/1", json=updated_person)
assert response.status_code == 200  # Ensure a successful update

# Test DELETE operation
response = requests.delete("http://10.0.0.176:5050/api/1")
assert response.status_code == 200  # Ensure a successful deletion
