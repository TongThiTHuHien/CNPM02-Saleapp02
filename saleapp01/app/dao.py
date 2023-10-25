

def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 1,
        'name': 'Tablet'
    }]

def load_products(kw):
    products = [{
        'id': 1,
        'name': 'Iphone 15 Promax',
        'price': 2000000,
        'image': "https://cdn1.viettelstore.vn/Images/Product/ProductImage/325815861.jpeg"

    }, {
        'id': 2,
        'name': 'Iphone 15 Promax',
        'price': 2000000,
        'image': "https://cdn1.viettelstore.vn/Images/Product/ProductImage/325815861.jpeg"

    },{
        'id': 1,
        'name': 'Ipad',
        'price': 2000000,
        'image': "https://cdn1.viettelstore.vn/Images/Product/ProductImage/325815861.jpeg"

    }, {
        'id': 1,
        'name': 'Iphone 15 Promax',
        'price': 2000000,
        'image': "https://cdn1.viettelstore.vn/Images/Product/ProductImage/325815861.jpeg"

    }, {
        'id': 1,
        'name': 'Iphone 15 Promax',
        'price': 2000000,
        'image': "https://cdn1.viettelstore.vn/Images/Product/ProductImage/325815861.jpeg"

    }, {
        'id': 1,
        'name': 'Iphone 15 Promax',
        'price': 2000000,
        'image': "https://cdn1.viettelstore.vn/Images/Product/ProductImage/325815861.jpeg"

    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >=0]

    return products