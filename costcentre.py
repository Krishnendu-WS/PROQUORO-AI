import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize(
    "cost_code, cost_type, cost_name, description, location_search, status",
    [
        (
            "CB-PROB-01",
            "ITEM",
            "MARABATI",
            "This is a plant situated in maharashtra",
            "ipl",
            "Active"
        ),
        (
            "CB-PROB-02",
            "ITEM",
            "KOLKATA HUB",
            "Kolkata operational plant",
            "ipl",
            "Active"
        ),
        (
            "CB-PROB-03",
            "ITEM",
            "MUMBAI CENTER",
            "Mumbai distribution center",
            "ipl",
            "Active"
        )
    ]
)
def test_create_cost_center(
    page: Page,
    cost_code,
    cost_type,
    cost_name,
    description,
    location_search,
    status
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
        name="Cost Centre"
    ).click()

    page.get_by_role(
        "button",
        name="+ Add Cost Center"
    ).click()

    # ---------------- COST CODE ---------------- #

    page.get_by_role(
        "textbox",
        name="e.g., CC-PROD-"
    ).fill(cost_code)

    # ---------------- COST TYPE ---------------- #

    page.get_by_role(
        "button",
        name="Select type"
    ).click()

    search_box = page.get_by_role(
        "textbox",
        name="Search…"
    )

    search_box.fill(cost_type)

    page.get_by_role(
        "listbox"
    ).get_by_text(
        "Item pick up centre"
    ).click()

    # ---------------- COST CENTER NAME ---------------- #

    page.get_by_role(
        "textbox",
        name="e.g., Production - Main Plant"
    ).fill(cost_name)

    # ---------------- DESCRIPTION ---------------- #

    page.get_by_role(
        "textbox",
        name="Brief description of what"
    ).fill(description)

    # ---------------- LOCATION ---------------- #

    page.get_by_role(
        "button",
        name="Select location"
    ).click()

    location_box = page.get_by_role(
        "textbox",
        name="Search…"
    )

    location_box.fill(location_search)

    page.get_by_text(
        "IPL Technology - Bengaluru Tech Center, Bengaluru, Karnataka,"
    ).click()

    # ---------------- STATUS ---------------- #

    page.get_by_role(
        "button",
        name="Active"
    ).click()

    page.get_by_role(
        "option",
        name=status,
        exact=True
    ).click()

    # ---------------- SUBMIT ---------------- #

    page.get_by_role(
        "button",
        name="Add Cost Center",
        exact=True
    ).click()

    # ---------------- VALIDATION LOGS ---------------- #

    print("\nCost Center Created Successfully")

    print(f"Cost Code: {cost_code}")
    print(f"Cost Type: {cost_type}")
    print(f"Cost Name: {cost_name}")
    print(f"Description: {description}")
    print(f"Status: {status}")
