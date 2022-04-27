from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_developers():
    response = client.get('/developers')
    assert response.status_code == 200

def test_get_developer():
    response = client.get('/developers/6268d00eb6b68776a1ffbde7')
    assert response.status_code == 200

def test_get_skills():
    response = client.get('/developers/6268d00eb6b68776a1ffbde7/skills')
    assert response.status_code == 200

def test_get_experience():
    response = client.get('/developers/6268d00eb6b68776a1ffbde7/experience')
    assert response.status_code == 200

def test_get_languages():
    response = client.get('/developers/6268d00eb6b68776a1ffbde7/languages')
    assert response.status_code == 200

def test_create_developer():
    response = client.post('/developers', json={
        "name": "Cesar",
        "country": "Ecuador",
        "age": 26,
        "experience":[
            {
                "title": "Frontend Developer",
                "location": "Ecuador",
                "start_date": "2021",
                "end_date": "Present",
                "organization": "Real company"
            }
        ],
        "skills": [
            
        ],
        "languages": [
            {
                "name": "Spanish",
                "level": "native"
            },
            {
                "name": "English",
                "level": "intermediate"
            }
        ]
    })

    assert response.status_code == 201

def test_update_developer():
    response = client.put('/developers/6268d00eb6b68776a1ffbde7', json={
        "name": "Cesar",
        "country": "Ecuador",
        "age": 26,
        "experience":[
            {
                "title": "Frontend Developer",
                "location": "Ecuador",
                "start_date": "2021",
                "end_date": "Present",
                "organization": "Real company"
            }
        ],
        "skills": [
            
        ],
        "languages": [
            {
                "name": "Spanish",
                "level": "native"
            },
            {
                "name": "English",
                "level": "intermediate"
            }
        ]
    })

    assert response.status_code == 201

def test_update_developer2():
    response = client.put('/developers/6268d00eb6b68776a1ffbde9', json={
        "name": "Cesar",
        "country": "Ecuador",
        "age": 26,
        "experience":[
            {
                "title": "Frontend Developer",
                "location": "Ecuador",
                "start_date": "2021",
                "end_date": "Present",
                "organization": "Real company"
            }
        ],
        "skills": [
            
        ],
        "languages": [
            {
                "name": "Spanish",
                "level": "native"
            },
            {
                "name": "English",
                "level": "intermediate"
            }
        ]
    })

    assert response.status_code == 400


def test_delete_developer():
    response = client.delete('/developers/6268d00eb6b68776a1ffbde7')
    assert response.status_code == 200