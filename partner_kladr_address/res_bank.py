# -*- coding: UTF-8 -*-

##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-2017 Libre Comunication (<>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    name = fields.Char(string='Bank Account',
                       size=256)
    bank_name = fields.Char(string='Bank Name',
                            size=256)

    def onchange_partner_id_kladr(self, partner_id):
        result = {}
        if partner_id:
            part = self.env['res.partner'].browse(partner_id)
            result['owner_name'] = part.name
            result['street'] = part.street or False
            result['city'] = part.city or False
            result['zip'] = part.zip or False
            result['country_id'] = part.country_id.id
            result['state_id'] = part.state_id.name
        return {'value': result}


class Bank(models.Model):
    _inherit = 'res.bank'

    name = fields.Char(string='Bank Account',
                       size=256)
