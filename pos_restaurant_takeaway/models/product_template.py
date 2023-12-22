# -*- coding: utf-8 -*-
"""adding a discount tag field  to product form"""
from odoo import fields, models


class ComboProduct(models.Model):
    """class for inherit the product_product"""
    _inherit = 'product.template'

    is_addons = fields.Boolean(
        string='is Add-ons', help="Allow Add-ons")

    has_addons = fields.Boolean(
        string='has Add-ons', help="Enable to Add Add-ons")

    product_ids = fields.Many2many("product.product",string="Add-ons",
                                  help="Add products in this field")