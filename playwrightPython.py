from playwright.sync_api import sync_playwright

def test_api_get_request():
    with sync_playwright() as pw:
        request_context = pw.request.new_context()

        # Replace with your actual API endpoint
        response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")

        # Assertions
        assert response.status == 200, f"Expected status 200, got {response.status}"
        json_data = response.json()

        assert json_data["id"] == 1, "ID mismatch in response"
        print("GET request test passed!")

def test_api_post_request():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }

        response = request_context.post("https://jsonplaceholder.typicode.com/posts", data=payload)

        assert response.status == 201, f"Expected status 201, got {response.status}"
        json_data = response.json()

        assert json_data["title"] == "foo", "Title mismatch in response"
        print("POST request test passed!")

def test_api_put_request():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        payload = {
            "id": 1,
            "title": "title harmeet",
            "body": "body harmeet singh",
            "userId": 1
        }

        response = request_context.put("https://jsonplaceholder.typicode.com/posts/1", data=payload)

        assert response.status == 200, f"Expected status 200, got {response.status}"
        json_data = response.json()

        assert json_data["title"] == "title harmeet", "Title mismatch in response"
        print("PUT request test passed!")

def test_api_patch_request(posts):
    with sync_playwright() as p:
        request_context = p.request.new_context()

        payload = {
            "title": "patched harmeet"
        }

        response = request_context.patch("https://jsonplaceholder.typicode.com/posts/"+str(posts), data=payload)

        assert response.status == 200, f"Expected status 200, got {response.status}"
        json_data = response.json()

        assert json_data["title"] == "patched harmeet", "Title mismatch in response"
        print("PATCH request test passed!")

def test_api_delete_request(posts):
    with sync_playwright() as p:
        request_context = p.request.new_context()

        response = request_context.delete("https://jsonplaceholder.typicode.com/posts/"+str(posts))

        assert response.status == 200, f"Expected status 200, got {response.status}"
        print("DELETE request test passed!")


# Run tests
pts = 1  # Test Data
test_api_get_request()
test_api_post_request()
test_api_put_request()
test_api_patch_request(pts)
test_api_delete_request(pts)