# -*- coding: utf-8 -*-
"""adding a Takeaway and generate toke boolean field to pos settings"""
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """declaring a class for ResConfigSettings"""
    _inherit = 'res.config.settings'

    pos_is_takeaway = fields.Boolean(
        string='Pos TakeAway',
        related="pos_config_id.is_takeaway",
        help="TakeAway, Dine-in on Restaurant",
        readonly=False
    )
    generate_token = fields.Boolean(
        string='Generate Token',
        related="pos_config_id.token",
        default=True,
        help="This Token number starts from 1",
        readonly=False
    )
    pos_token = fields.Integer(
        string="Token",
        help="The token will start from 1.",
        related="pos_config_id.token_number"
    )
