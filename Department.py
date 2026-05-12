import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize(
    "department_name, description, head_search, head_email, location_search, location_name",
    [
        (
            "Data Analysis",
            "Data Analysis is done here",
            "kona",
            "konaw90924@gixpos.com",
            "ipl",
            "IPL Technology - Bengaluru"
        ),
        (
            "Human Resource",
            "HR operations are managed here",
            "kona",
            "konaw90924@gixpos.com",
            "ipl",
            "IPL Technology - Bengaluru"
        ),
        (
            "Finance",
            "Finance and accounting handled here",
            "kona",
            "konaw90924@gixpos.com",
            "ipl",
            "IPL Technology - Bengaluru"
        )
    ]
)
def test_create_department(
    page: Page,
    department_name,
    description,
    head_search,
    head_email,
    location_search,
    location_name
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
        name="Department"
    ).click()

    # ---------------- OPEN MODAL ---------------- #

    page.get_by_role(
        "button",
        name="Add Department"
    ).click()

    # ---------------- DEPARTMENT NAME ---------------- #

    page.get_by_role(
        "textbox",
        name="Department Name *"
    ).fill(department_name)

    # ---------------- DESCRIPTION ---------------- #

    page.get_by_role(
        "textbox",
        name="Description"
    ).fill(description)

    # ---------------- DEPARTMENT HEAD ---------------- #

    page.get_by_role(
        "button",
        name="Department Head Email"
    ).click()

    search_box = page.get_by_role(
        "textbox",
        name="Search by email or name..."
    )

    search_box.fill(head_search)

    page.get_by_role(
        "listbox"
    ).get_by_text(head_email).click()

    # ---------------- LOCATION ---------------- #

    page.get_by_role(
        "button",
        name="Location",
        exact=True
    ).click()

    location_box = page.get_by_role(
        "textbox",
        name="Search locations..."
    )

    location_box.fill(location_search)

    page.get_by_text(location_name).click()

    # ---------------- SUBMIT ---------------- #

    page.get_by_role(
        "button",
        name="Create Department"
    ).click()

    # ---------------- VALIDATION LOGS ---------------- #

    print("\nDepartment Created Successfully")

    print(f"Department: {department_name}")
    print(f"Description: {description}")
    print(f"Department Head: {head_email}")
    print(f"Location: {location_name}")
