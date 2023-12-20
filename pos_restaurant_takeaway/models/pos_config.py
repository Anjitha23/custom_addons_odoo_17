from odoo import fields, models, api

class PosConfiguration(models.Model):
    _inherit = 'pos.config'

    is_takeaway = fields.Boolean(
        string='Pos TakeAway',
        help="TakeAway, Dine-in on Restaurant"
    )
    token = fields.Boolean(
        string='Generate Token',
        help="This Token number starts from 1",
        default=True
    )
    token_number = fields.Char(
        string="Token Number",
        help="Token number starts from 1"
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

        # Check if the order exists
        if order:
            # Find the associated pos.config record
            pos_config = self.env['pos.config'].search([('id', '=', order.config_id.id)], limit=1)

            if pos_config:
                pos_config.is_takeaway = True

                if not pos_config.token_number and pos_config.token:
                    if pos_config.token_number:
                        pos_config.token_number = int(pos_config.token_number) + 1
                    else:
                        pos_config.token_number = 1
                    self.env['ir.config_parameter'].sudo().set_param(
                        'pos_restaurant_takeaway.pos_token',
                        pos_config.token_number)

                    # Print statements for debugging
                    print(f"Token generated: {pos_config.token_number}")
                    print(f"Is Takeaway: {pos_config.is_takeaway}")
                    print(
                        f"Token Configuration: {pos_config.token}, Token Number: {pos_config.token_number}")
                    return pos_config.token_number
                else:
                    return 0
            else:
                print(f"No pos.config found for order with pos_reference: {uid}")
                return 0
        else:
            print(f"No order found with pos_reference: {uid}")
            return 0
