from app.main import solution


def test_email_app():
    assert solution(
        "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker",
        "Example") == "John Doe <john.doe@example.com>, Peter Benjamin Parker <peter.parker@example.com>, Mary Jane Watson-Parker <mary.watsonparker@example.com>, John Elvis Doe <john.doe2@example.com>, John Evan Doe <john.doe3@example.com>, Jane Doe <jane.doe@example.com>, Peter Brian Parker <peter.parker2@example.com>"
