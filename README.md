# NovaMart

A small realistic e-commerce training application for SQA/SDET practice.

## Run locally

From the project folder:

```powershell
python -m http.server 8000
```

Then open:

`http://127.0.0.1:8000`

## Pages

- Home
- Product listing with search/filter/sort
- Product detail
- Shopping cart
- Checkout
- Order confirmation
- Demo login

The application is intentionally frontend-only and uses `localStorage` for the cart. Payment is simulated; never enter real card details.

## SQA training goal

After the first application version is stable, use Playwright/Pytest to test realistic customer journeys, then connect those tests to GitHub Actions and the deployed site.
