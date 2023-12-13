# -*- coding: utf-8 -*-
"""adding a field product to customers"""
from odoo import fields, models


class ResPartner(models.Model):
    """class for inherited model"""
    _inherit = 'res.partner'

    combo_ids = fields.Many2many("website.sale.combo",
                                        string="Combo Products")
