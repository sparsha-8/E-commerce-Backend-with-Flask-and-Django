# E-commerce Backend (Django + DRF + JWT)

Features:
- JWT Auth (login with /api/token/)
- Products & Categories (search, ordering)
- Cart (add/update/delete items)
- Orders (create from cart, mock payment, list my orders)
- Simple content-based Recommender (TF-IDF over product text)

## Quickstart

```bash
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata data/products.json  # optional if provided
# or load CSV via the helper script below
python manage.py runserver
```

### Auth
- Obtain token: POST /api/token/ with {"username":"...", "password":"..."}
- Refresh token: POST /api/token/refresh/

### Products
- GET /api/products/items/?search=phone
- POST/PUT/DELETE requires staff (is_staff=True)

### Cart
- GET /api/cart/ (must be authenticated)
- POST /api/cart/add/ {"product_id":1, "quantity":2}
- PATCH /api/cart/item/<id>/ {"quantity":3}
- DELETE /api/cart/item/<id>/

### Orders
- POST /api/orders/create/
- GET /api/orders/mine/

### Recommender
- Train: `python manage.py build_recommender`
- GET /api/recommender/similar/<product_id>/

## Load sample data (CSV)
Use the provided `data/products.csv` then run this Django shell snippet:

```bash
python manage.py shell
```
```python
import csv
from products.models import Product, Category
from django.utils.text import slugify
with open('data/products.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    cats = {}
    for row in reader:
        cat = row['category']
        if cat not in cats:
            from products.models import Category
            cats[cat], _ = Category.objects.get_or_create(name=cat, slug=slugify(cat))
        Product.objects.get_or_create(
            id=int(row['id']),
            defaults=dict(
                name=row['name'],
                slug=slugify(row['name']) + '-' + row['id'],
                description=row['description'],
                price=row['price'],
                category=cats[cat],
                brand=row.get('brand',''),
                stock=int(row['stock'])
            )
        )
print("Loaded products.")
```