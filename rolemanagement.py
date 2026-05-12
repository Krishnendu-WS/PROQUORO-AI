import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize(
    "role_name, role_code, description",
    [
        (
            "Data Engineer",
            "DE-009",
            "This role is for Data Engineer"
        ),
        (
            "Backend Developer",
            "BD-010",
            "This role is for Backend Developer"
        ),
        (
            "QA Engineer",
            "QA-011",
            "This role is for QA Engineer"
        )
    ]
)
def test_create_role(
    page: Page,
    role_name,
    role_code,
    description
):

    # ---------------- LOGIN ---------------- #

    page.goto("https://stg.proquro.ai/")

    page.get_by_role(
        "link",
        name="Sign In"
    ).click()

    page.get_by_role(
        "link",
        name="Securely Login With Email"
    ).click()

    page.get_by_role(
        "textbox",
        name="Email"
    ).fill("mobpark@yopmail.com")

    page.get_by_role(
        "textbox",
        name="Password"
    ).fill("Avromandal12345@")

    page.get_by_role(
        "button",
        name="Log In"
    ).click()

    # ---------------- NAVIGATION ---------------- #

    page.get_by_role("button").first.click()

    page.get_by_role(
        "link",
        name="Role Management"
    ).click()

    # ---------------- CREATE ROLE ---------------- #

    page.get_by_role(
        "button",
        name="+ Create New Role"
    ).click()

    # ---------------- ROLE NAME ---------------- #

    page.get_by_role(
        "textbox",
        name="e.g., Senior Procurement"
    ).fill(role_name)

    # ---------------- ROLE CODE ---------------- #

    page.get_by_role(
        "textbox",
        name="e.g., SR_PROC_OFF"
    ).fill(role_code)

    # ---------------- DESCRIPTION ---------------- #

    page.get_by_role(
        "textbox",
        name="Describe the role's"
    ).fill(description)

    # ---------------- SUBMIT ---------------- #

    page.get_by_role(
        "button",
        name="Create Role"
    ).click()

    # ---------------- VALIDATION LOGS ---------------- #

    print("\nRole Created Successfully")

    print(f"Role Name: {role_name}")
    print(f"Role Code: {role_code}")
    print(f"Description: {description}")
