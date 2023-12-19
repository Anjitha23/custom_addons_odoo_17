from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_takeaway = fields.Boolean(
        string='Pos TakeAway',
        related="pos_config_id.is_takeaway",
        help="TakeAway, Dine-in on Restaurant",
        readonly=False)
    generate_token = fields.Boolean(
        string='Generate Token',
        related="pos_config_id.token",
        help="This Token number starts from 1")
