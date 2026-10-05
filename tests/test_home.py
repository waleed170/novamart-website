from playwright.sync_api import Page, expect


def test_homepage_loads(page: Page):
    page.goto("/")

    expect(page).to_have_title("NovaMart — Modern Essentials")