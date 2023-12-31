# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Controller, request, route

class ComboProductMenu(Controller):
    """class for Combo product menu"""
    @route(route='/combos', auth='public', website=True)
    def combo_product(self):
        """To generate the combo products of the logged in user"""
        partner = request.env.user.partner_id
        combo_product = partner.combo_ids  # Assuming combo_ids is a One2many field
        return request.render(
            'website_combo_products.website_combo_product_template',
            {
                'combo_product': combo_product,
            })

    @http.route('/combo_product/<int:combo_id>', type='http', auth="public",
                website=True)
    def combo_product_page(self, combo_id, **kw):
        """To display the corresponding products of the selected combo"""
        combo = request.env['website.sale.combo'].browse(combo_id)
        products = combo.product_ids
        return request.render('website_combo_products.combo_product_page',
                              {'combo': combo, 'products': products})

    @route(route='/add_to_cart/<int:combo_id>', type='http', auth='public',
           website=True)
    def add_to_cart(self, combo_id, **post):
        """Add all the products into cart at one click of Add to cart buttton"""
        if not request.env.user:
            return request.redirect('/combos')

        partner = request.env.user.partner_id
        combo = request.env['website.sale.combo'].browse(combo_id)

        order = request.website.sale_get_order()
        if not order:
            order = request.env['sale.order'].sudo().create({
                'partner_id': partner.id,
                'website_id': request.website.id,
            })

        for product_variant in combo.product_ids:
            existing_line = order.order_line.filtered(
                lambda
                    line: line.product_id == product_variant.product_variant_id
            )

            if existing_line:
                # Update quantity if the product already exists in the cart
                existing_line.write(
                    {'product_uom_qty': existing_line.product_uom_qty + 1})
            else:
                # Add a new line if the product is not in the cart
                request.env['sale.order.line'].sudo().create({
                    'order_id': order.id,
                    'product_id': product_variant.product_variant_id.id,
                    'product_uom_qty': 1,
                    'name': product_variant.name,
                    'price_unit': product_variant.list_price,
                })

        return request.redirect('/shop/cart')
