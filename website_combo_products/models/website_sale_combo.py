# -*- coding: utf-8 -*-
"""adding a field product to customers"""
from odoo import api, fields, models, _


class WebsiteSaleCombo(models.Model):
    """class for website sale combo model"""
    _name = 'website.sale.combo'
    _inherit = 'mail.thread'

    name = fields.Char(readonly=True, default=lambda self: _('New'))
    combo_name = fields.Char(string='Combo Name')
    product_ids = fields.Many2many("product.template",
                                 string="Combo Products")


    def create(self, vals):
        """ GENERATING SEQUENCE FOR MATERIAL REQUEST"""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'website.sale.combo') or _('New')
        return super().create(vals)


