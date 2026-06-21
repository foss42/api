import pytest

@pytest.mark.parametrize("endpoint, input_text, expected_output", [
    ("/case/lower", "Hello World", "hello world"),
    ("/case/upper", "Hello World", "HELLO WORLD"),
    ("/case/capital", "hello world", "Hello World"),
    ("/case/title", "hello world", "Hello World"),
    ("/case/sentence", "hello world. hi.", "Hello world. hi."),
    ("/case/swap", "Hello World", "hELLO wORLD"),
    ("/case/flat", "Hello World", "helloworld"),
    ("/case/pascal", "hello world", "HelloWorld"),
    ("/case/camel", "Hello World", "helloWorld"),
    ("/case/snake", "Hello World", "hello_world"),
    ("/case/constant", "Hello World", "HELLO_WORLD"),
    ("/case/camelsnake", "Hello World", "hello_World"),
    ("/case/pascalsnake", "hello world", "Hello_World"),
    ("/case/dot", "Hello World", "hello.world"),
    ("/case/kebab", "Hello World", "hello-world"),
    ("/case/cobol", "Hello World", "HELLO-WORLD"),
    ("/case/train", "Hello World", "Hello-World"),
    ("/case/camel2lower", "helloWorld", "hello world"),
    ("/case/snake2lower", "hello_world", "hello world"),
    ("/case/kebab2lower", "hello-world", "hello world"),
])
def test_case_convert_get(client, endpoint, input_text, expected_output):
    response = client.get(f"{endpoint}?text={input_text}")
    assert response.status_code == 200
    assert response.json()["data"] == expected_output

@pytest.mark.parametrize("endpoint, input_text, expected_output", [
    ("/case/lower", "Hello World", "hello world"),
    ("/case/upper", "Hello World", "HELLO WORLD"),
    ("/case/capital", "hello world", "Hello World"),
    ("/case/title", "hello world", "Hello World"),
    ("/case/sentence", "hello world. hi.", "Hello world. hi."),
])
def test_case_convert_post(client, endpoint, input_text, expected_output):
    response = client.post(endpoint, json={"text": input_text})
    assert response.status_code == 200
    assert response.json()["data"] == expected_output
