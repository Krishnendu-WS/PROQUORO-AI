import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize(
    "first_name, last_name, email, role_search, role_name, dept_search, department_name, location_search, location_name",
    [
        (
            "krishanu",
            "saha",
            "krishanusaha769@gmail.com",
            "Dept",
            "Dept User",
            "da",
            "Data Aanalyst",
            "kol",
            "kolkata, kolkata, wb,"
        ),
        (
            "rahul",
            "sharma",
            "rahulsharma123@gmail.com",
            "Dept",
            "Dept User",
            "da",
            "Data Aanalyst",
            "kol",
            "kolkata, kolkata, wb,"
        ),
        (
            "amit",
            "das",
            "amitdas456@gmail.com",
            "Dept",
            "Dept User",
            "da",
            "Data Aanalyst",
            "kol",
            "kolkata, kolkata, wb,"
        )
    ]
)
def test_invite_team_member(
    page: Page,
    first_name,
    last_name,
    email,
    role_search,
    role_name,
    dept_search,
    department_name,
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
        name="Team Management"
    ).click()

    # ---------------- INVITE MEMBER ---------------- #

    page.get_by_role(
        "button",
        name="Invite Member"
    ).click()

    # ---------------- FIRST NAME ---------------- #

    page.get_by_role(
        "textbox",
        name="Enter first name"
    ).fill(first_name)

    # ---------------- LAST NAME ---------------- #

    page.get_by_role(
        "textbox",
        name="Enter last name"
    ).fill(last_name)

    # ---------------- EMAIL ---------------- #

    page.get_by_role(
        "textbox",
        name="colleague@company.com"
    ).fill(email)

    # ---------------- ROLE ALLOCATION ---------------- #

    page.get_by_role(
        "button",
        name="Role allocation"
    ).click()

    role_search_box = page.get_by_role(
        "textbox",
        name="Search roles…"
    )

    role_search_box.fill(role_search)

    page.get_by_role(
        "listbox"
    ).get_by_text(role_name).click()

    # ---------------- DEPARTMENT ---------------- #

    page.get_by_label(
        "Department"
    ).click()

    dept_search_box = page.get_by_role(
        "textbox",
        name="Search departments…"
    )

    dept_search_box.fill(dept_search)

    page.get_by_role(
        "listbox"
    ).get_by_text(department_name).click()

    # ---------------- LOCATION ---------------- #

    page.get_by_role(
        "button",
        name="Location",
        exact=True
    ).click()

    location_search_box = page.get_by_role(
        "textbox",
        name="Search locations…"
    )

    location_search_box.fill(location_search)

    page.get_by_text(location_name).click()

    # ---------------- SUBMIT ---------------- #

    page.get_by_role(
        "button",
        name="Send Invitation",
        exact=True
    ).click()

    # ---------------- VALIDATION LOGS ---------------- #

    print("\nInvitation Sent Successfully")

    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Email: {email}")
    print(f"Role: {role_name}")
    print(f"Department: {department_name}")
    print(f"Location: {location_name}")
