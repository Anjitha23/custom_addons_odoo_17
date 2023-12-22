# -*- coding: utf-8 -*-
"""adding a Takeaway  boolean field to pos orders"""
from odoo import fields, models

class PosOrder(models.Model):
    """declaring class for PosOrder"""
    _inherit = 'pos.order'

    is_takeaway = fields.Boolean(
        string='TakeAway',
        help='TakeAway, Dine-in on Restaurant',
        readonly=True
    )
    token_number = fields.Integer(string="Token Number",
                               help="Token number starts from 1")
