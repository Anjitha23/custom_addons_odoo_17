# -*- coding: utf-8 -*-
"""adding a discount tag field  to product form"""
from odoo import fields, models


class PosConfiguration(models.Model):
    """class to inherit the pos.config"""
    _inherit = 'pos.config'

    dine_in = fields.Boolean(
        string='Pos TakeAway',
        help="TakeAway,Dine-in on Restaurant")
    token = fields.Boolean(
        string='Generate Token',
        help="This Token number starts from 1")


class ResConfSettings(models.TransientModel):
    """class to inherit the res.config.settings"""
    _inherit = 'res.config.settings'

    dine_in = fields.Boolean(
        related="pos_config_id.dine_in",
        string='Pos TakeAway',
        help="TakeAway,Dine-in on Restaurant",
        readonly=False)
    token = fields.Boolean(
        string='Generate Token',
        help="This Token number starts from 1")
