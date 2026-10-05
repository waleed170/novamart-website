from playwright.sync_api import Page, expect


def test_products_page_displays_products(page: Page):
    page.goto("/products.html")

    products = page.locator(".product-card")

    expect(products.first).to_be_visible()