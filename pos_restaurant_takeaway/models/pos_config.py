# -*- coding: utf-8 -*-
"""adding a Takeaway and generate toke boolean field to pos settings"""
from odoo import api, fields, models

class PosConfiguration(models.Model):
    """declaring the class for PosConfiguration """
    _inherit = 'pos.config'

    is_takeaway = fields.Boolean(
        string='Pos TakeAway',
        help='TakeAway, Dine-in on Restaurant',
    )
    token = fields.Boolean(
        string='Generate Token',
        help='This Token number starts from 1',
        default=True,
    )
    token_number = fields.Integer(
        string="Token Number",
        help="Token number starts from 1",
        default=1
    )

    @api.model
    def generate_token(self, uid):

        """
        This function checks whether the order is a take-away order or a dine-in.
        If it is a take-away order, it will create the token number for that
        order and return it.
        :param uid: the pos order id
        :return: order.token_number: token number of the pos order having the
        order reference uid
        """
        uid = "Order " + uid[0]

        # Directly search for pos.order instead of pos.config
        order = self.env['pos.order'].search([('pos_reference', 'ilike', uid)], limit=1)
        if order:
            # Find the associated pos.config record
            pos_config = order.config_id

            if pos_config and pos_config.token:
                pos_config.token_number = pos_config.token_number + 1
                self.env['ir.config_parameter'].sudo().set_param(
                    'pos_restaurant_takeaway.pos_token',
                    pos_config.token_number)
                return pos_config.token_number
            else:
                return 0
        else:
            return 0
