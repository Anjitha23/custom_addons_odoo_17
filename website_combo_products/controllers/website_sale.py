# -- coding: utf-8 --
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale, QueryURL, \
    lazy, TableCompute


class WebsiteComboVisibility(WebsiteSale):
    """Inherit the website sale controller"""

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, combo_products=None, search='',
             min_price=0.0, max_price=0.0, ppg=False, **post):

        result = super(WebsiteComboVisibility, self).shop(page=page,
                                                          category=category,
                                                          search=search,
                                                          min_price=min_price,
                                                          max_price=max_price,
                                                          ppg=ppg, **post)
        partner = http.request.env.user.partner_id
        combo_ids = partner.combo_ids

        website = http.request.env['website'].get_current_website()
        result.qcontext['selected_combos'] = []

        if combo_ids:
            combo_names = [combo.name for combo in combo_ids]
            result.qcontext['combo_products'] = combo_names

            if combo_products:
                combo_products = [combo_products] if isinstance(combo_products,
                                                                str) else combo_products
                combine_filters = combo_products[0].split(',')
                result.qcontext['selected_combos'] = combine_filters
                selected_combos = http.request.env['website.sale.combo'].search(
                    [('name', 'in', combine_filters)])
                if selected_combos:
                    combo_product_templates = selected_combos.mapped(
                        'product_ids')
                else:
                    combo_product_templates = http.request.env[
                        'product.template']

                products = combo_product_templates.filtered(
                    lambda t: t.website_published and t.sale_ok
                )
                pager = website.pager(url='/shop',
                                      total=len(products),
                                      page=page, step=result.qcontext['ppg'],
                                      scope=7, url_args=post)
                offset = pager['offset']
                products = products[offset:offset + result.qcontext['ppg']]
                products = products.filtered(
                    lambda t: t.website_published and t.sale_ok
                )
                products_prices = lazy(lambda: products._get_sales_prices(
                    result.qcontext['pricelist'],
                    result.qcontext['fiscal_position']))

                result.qcontext['bins'] = lazy(
                    lambda: TableCompute().process(products,
                                                   result.qcontext['ppg'],
                                                   result.qcontext['ppr']))
                result.qcontext['get_product_prices'] = lambda product: lazy(
                    lambda: products_prices[product.id])
                result.qcontext['pager'] = pager
                result.qcontext['products_prices'] = products_prices
                result.qcontext[
                    'template_to_render'] = 'website_combo_products.combo_products_website_aside'

        return result
