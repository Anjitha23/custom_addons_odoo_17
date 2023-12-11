{
    'name': "Website Combo Products",
    'version': '17.0.1.0.0',
    'depends': ['website','website_sale'],
    'author': "Anjitha",
    'category': 'Category',
    'description': """Buying combo products of the logged in user online""",
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/combo_product_menu.xml',
        'views/res_partners_view.xml',
        'views/combo_views.xml',
        'views/combo_product_menu_aside.xml',
        'views/website_sale_combos_menu.xml',
        'views/website_sale_combo_views.xml',
        'views/combo_products_views.xml',
         ],

    'installable': True,
    'application': True,
}
