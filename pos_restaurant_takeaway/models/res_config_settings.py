from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    class ResConfSettings(models.TransientModel):
        """class to inherit the res.config.settings"""
        _inherit = 'res.config.settings'

        is_dine_in = fields.Boolean(
            string='Pos TakeAway',
            related="pos_config_id.is_dine_in",
            help="TakeAway,Dine-in on Restaurant",
            readonly=False)
        generate_token = fields.Boolean(
            string='Generate Token',
            default=True,
            help="This Token number starts from 1")