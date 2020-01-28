import requests
import pytest # have to install via command "pip3 install -U pytest"
import json

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

def test_no_name():
    r = requests.get('http://localhost:8085/hello-world')
    assert(r.status_code == 200)

    ret_data = json.loads(r.content)

    assert(ret_data['content'] == "Hello, Stranger!")

def test_name():
    r = requests.get('http://localhost:8085/hello-world?name=Micah')
    assert(r.status_code == 200)

    ret_data = json.loads(r.content)

    assert(ret_data['content'] == "Hello, Micah!")
