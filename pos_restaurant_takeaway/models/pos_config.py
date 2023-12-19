# -*- coding: utf-8 -*-
"""adding a boolean fields into pos configuration settings"""
from odoo import fields, models


class PosConfiguration(models.Model):
    """class to inherit the pos.config"""
    _inherit = 'pos.config'

    is_takeaway = fields.Boolean(
        string='Pos TakeAway',
        help="TakeAway, Dine-in on Restaurant")
    token = fields.Boolean(
        string='Generate Token',
        help="This Token number starts from 1",default=True)
    token_number = fields.Char(string="Token Number",
                               help="Token number starts from 1")


