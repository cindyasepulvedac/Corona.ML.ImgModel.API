from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

login_data = {'username':'pepito', 'password':'123'}
predict_data = {
    "request_id": "uuid",
    "modelo": "clf.pickle",
    "image":"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/wAALCAAIAAgBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AOYitTJ8BgJYkn8tZJ4maMLFEpnC5EhXJnBVh5YYZR884Ar/2Q==",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InBlcGl0byIsImVtYWlsIjoicGVwaXRvQGNvcm9uYS5jb20ifQ.3oGuPEWTP4VlWyO8VbzedM4BYGjyQrHwK1YlC_yt7Hw"
}

def test_greeting():
    response = client.get('/')
    assert response.status_code == 200

def test_valid_login():
    response = client.post('/token', data=login_data)
    assert response.status_code == 200
    
    decoded_response = response.json()
    assert decoded_response['token_type'] == 'bearer'
    assert decoded_response['access_token'] != ''

def test_invalid_login():
    response = client.post('/token', data={})
    assert response.status_code != 200

def test_model_predict():
    response = client.post('/predict', json=predict_data)
    assert response.status_code == 200

    decoded_response = response.json()
    assert decoded_response['request_id'] == 'uuid'
    assert isinstance(decoded_response['prediction'], list) == True
    assert decoded_response['prediction'] != []



    