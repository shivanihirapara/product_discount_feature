{
    'name': 'Product Discount Feature',
    'version': '1.0',
    'summary': 'Adds discount functionality to products in the eCommerce store',
    'author': 'Shivani',
    'category': 'Website',
    'depends': ['website_sale', 'product'],
    'data': [
        'views/product_template_views.xml',
        'views/ecommerce_product_template.xml',
        'views/ecommerce_cart_template.xml',
    ],
    'installable': True,
    'application': True,
}
