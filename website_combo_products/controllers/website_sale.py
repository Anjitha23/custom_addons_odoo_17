# -- coding: utf-8 --
from odoo import http, fields
from odoo.addons.website_sale.controllers.main import WebsiteSale, QueryURL, lazy, TableCompute
from odoo.http import request


class WebsiteComboVisibility(WebsiteSale):
    """Inherit the website sale controller"""

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, combo_products=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):

        result = super(WebsiteComboVisibility, self).shop(page=page, category=category, search=search,
                                                          min_price=min_price, max_price=max_price, ppg=ppg, **post)
        print(result.qcontext)
        partner = http.request.env.user.partner_id
        combo_ids = partner.combo_ids

        website = http.request.env['website'].get_current_website()
        pricelist = http.request.env['product.pricelist'].browse(
            http.request.session.get('website_sale_current_pl'))

        filter_by_price_enabled = website.is_view_active('website_sale.filter_products_price')
        if filter_by_price_enabled:
            company_currency = website.company_id.currency_id
            conversion_rate = http.request.env['res.currency']._get_conversion_rate(
                company_currency, website.currency_id, request.website.company_id, fields.Date.today())
        else:
            conversion_rate = 1

        options = self._get_search_options(
            category=category,
            min_price=min_price,
            max_price=max_price,
            conversion_rate=conversion_rate,
            display_currency=website.currency_id,
            **post
        )

        if combo_ids:
            combo_names = [combo.name for combo in combo_ids]
            result.qcontext['combo_products'] = combo_names

            if combo_products:
                combo_products = [combo_products] if isinstance(combo_products, str) else combo_products

                selected_combos = http.request.env['website.sale.combo'].search(
                    [('name', 'in', combo_products)])
                if selected_combos:
                    combo_product_templates = selected_combos.mapped(
                        'product_ids')
                else:
                    combo_product_templates = http.request.env['product.template']
            else:
                combo_product_templates = http.request.env['product.template'].search([])

            combo_product_templates = combo_product_templates.filtered(
                lambda t: t.website_published and t.sale_ok)

            if not combo_product_templates:
                return result

            ppg = website.shop_ppg or 20
            ppr = website.shop_ppr or 4

            pager = website.pager(url='/shop',
                                  total=len(combo_product_templates),
                                  page=page, step=ppg, scope=7, url_args=post)
            offset = pager['offset']
            products = combo_product_templates[offset:offset + ppg]

            fiscal_position_sudo = website.fiscal_position_id.sudo()
            products_prices = lazy(lambda: products._get_sales_prices(pricelist,
                                                                      fiscal_position_sudo))

            # Apply currency conversion to the product prices
            for product_id, price_info in products_prices.items():
                price_info['price_reduce'] *= conversion_rate

            print(products)

            result.qcontext['bins'] = lazy(
                lambda: TableCompute().process(products, ppg, ppr))
            result.qcontext['get_product_prices'] = lambda product: lazy(
                lambda: products_prices[product.id])
            result.qcontext['ppr'] = ppr
            result.qcontext['ppg'] = ppg
            result.qcontext['pager'] = pager
            result.qcontext['products'] = products
            result.qcontext['products_prices'] = products_prices
            result.qcontext['fiscal_position'] = fiscal_position_sudo
            result.qcontext[
                'template_to_render'] = 'website_combo_products.combo_products_website_aside'

            if filter_by_price_enabled:
                # Accessing additional filter values
                min_price = result.qcontext.get('min_price', 0.0)
                max_price = result.qcontext.get('max_price', 0.0)
                available_min_price = result.qcontext.get('available_min_price', 0.0)
                available_max_price = result.qcontext.get('available_max_price', 0.0)


                result.qcontext['min_price']= min_price or available_min_price
                result.qcontext['max_price']: max_price or available_max_price
                result.qcontext['available_min_price']: fields.Float.round(available_min_price, 2)
                result.qcontext['available_max_price']: fields.Float.round(available_max_price, 2)


        return result
