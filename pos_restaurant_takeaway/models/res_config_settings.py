import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
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
    pos_token = fields.Char(
        string="Token",
        help="The token will start from 1.",
        related="pos_config_id.token_number"
    )
