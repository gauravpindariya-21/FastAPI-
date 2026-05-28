from tests.conftest import auth_headers, create_user, login


def test_blog_owner_can_update_and_delete(client):
    create_user(client, "owner@example.com")
    token = login(client, "owner@example.com")

    created = client.post(
        "/blog/",
        json={"title": "First", "body": "Body"},
        headers=auth_headers(token),
    )
    blog_id = created.json()["id"]

    updated = client.put(
        f"/blog/{blog_id}",
        json={"title": "Updated", "body": "Updated body"},
        headers=auth_headers(token),
    )
    deleted = client.delete(f"/blog/{blog_id}", headers=auth_headers(token))

    assert created.status_code == 201
    assert updated.status_code == 202
    assert updated.json()["title"] == "Updated"
    assert deleted.status_code == 204


def test_non_owner_cannot_delete_blog(client):
    create_user(client, "owner2@example.com")
    owner_token = login(client, "owner2@example.com")

    created = client.post(
        "/blog/",
        json={"title": "First", "body": "Body"},
        headers=auth_headers(owner_token),
    )
    blog_id = created.json()["id"]

    create_user(client, "intruder@example.com")
    intruder_token = login(client, "intruder@example.com")
    response = client.delete(f"/blog/{blog_id}", headers=auth_headers(intruder_token))

    assert response.status_code == 403
    assert response.json()["error"]["message"] == "Not authorized to delete this blog"
