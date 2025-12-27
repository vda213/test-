from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ]
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1920, "height": 1200},
        locale="vi-VN"
    )

    page = context.new_page()

    page.route("**/*", lambda route, request: (
        route.abort() if request.resource_type in ["image", "font", "media"]
        else route.continue_()
    ))

    page.goto(
        "https://www.galaxycine.vn/rap-gia-ve/galaxy-kinh-duong-vuong/",
        wait_until="commit",
        timeout=60000
    )

    print(page.title())

    browser.close()
