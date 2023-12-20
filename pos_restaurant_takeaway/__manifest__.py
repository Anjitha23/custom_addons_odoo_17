{
    'name': "POS Restaurant Dine-in/TakeAway",
    'version': '17.0.1.0.0',
    'depends': ['point_of_sale'],
    'author': "Anjitha",
    'category': 'Category',
    'description': """The POS user can make orders as Dine-in or Take away, and it will create separate token for Take away orders.""",
    'data': [
        'views/pos_config_view.xml',
        'views/pos_order_view.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_restaurant_takeaway/static/src/xml/order_type_takeaway.xml',
            'pos_restaurant_takeaway/static/src/js/takeaway.js',
            'pos_restaurant_takeaway/static/src/js/takeaway_btn.js',
            'pos_restaurant_takeaway/static/src/xml/takeaway_btn_view.xml',
            'pos_restaurant_takeaway/static/src/xml/takeaway_receipt_screen.xml',
        ],
    },

    'installable': True,
    'application': True,
}
