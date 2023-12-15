# -*- coding: utf-8 -*-
"""adding a discount tag field  to product form"""
from odoo import fields, models


class PosConfiguration(models.Model):
    """class to inherit the pos.config"""
    _inherit = 'pos.config'

    is_takeaway = fields.Boolean(
        string='Pos TakeAway',
        help="TakeAway,Dine-in on Restaurant")
    token = fields.Boolean(
        string='Generate Token',
        help="This Token number starts from 1")


