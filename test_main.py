from fastapi import testclient
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_1():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == []
    response = client.post('/', json={"name": "FastAPI", "description": "Learn basics", "completed": False, "date": "Today"})
    assert response.status_code == 200
    assert response.json()[0]['name'] == 'FastAPI'
    assert response.json()[0]['description'] == 'Learn basics'
    assert response.json()[0]['completed'] == False
    assert response.json()[0]['date'] == 'Today'
    prev_id = response.json()[0]['id']
    response = client.delete('/'+prev_id)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_2():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == []
    
    response = client.post('/', json={"name": "FastAPI", "description": "Learn basics", "completed": False, "date": "Today"})
    assert response.status_code == 200
    assert response.json()[0]['name'] == 'FastAPI'
    assert response.json()[0]['description'] == 'Learn basics'
    assert response.json()[0]['completed'] == False
    assert response.json()[0]['date'] == 'Today'
    prev_id = response.json()[0]['id']
    
    response = client.put('/'+prev_id, json={"name": "FastAPI", "description": "Learnt the basics", "completed": True, "date": "Yesterday"})
    assert response.status_code == 200
    assert response.json()[0]['name'] == 'FastAPI'
    assert response.json()[0]['description'] == 'Learnt the basics'
    assert response.json()[0]['completed'] == True
    assert response.json()[0]['date'] == 'Yesterday'

    response = client.get('/'+prev_id)
    assert response.status_code == 200
    assert response.json()['name'] == 'FastAPI'
    assert response.json()['description'] == 'Learnt the basics'
    assert response.json()['completed'] == True
    assert response.json()['date'] == 'Yesterday'

    response = client.delete('/'+prev_id)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}