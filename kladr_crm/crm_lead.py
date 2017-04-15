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
from odoo.addons.base.res.res_partner import FormatAddress
from odoo import tools
from datetime import datetime
import time


class CrmLead(FormatAddress, models.Model):
    _name = "crm.lead"
    _inherit = "crm.lead"

    district = fields.Char(string='District',
                           size=128)
    state_id_kladr = fields.Char(string='State',
                                 size=128)
    house = fields.Char(string='House',
                        size=64)
    office = fields.Char(string='Office',
                         size=64)

    def onchange_state(self, state_name):
        result = {}
        state_ids = self.pool.get('res.country.state').search(
            [('name', '=', state_name)])
        if state_ids:
            state_obj = self.pool.get('res.country.state').browse(state_ids)
            if state_ids:
                result['state_id'] = state_obj[0].id
        return {'value': result}

    def _lead_create_contact(self, lead, name, is_company, parent_id=False):
        partner = self.pool.get('res.partner')
        vals = {'name': name,
                'user_id': lead.user_id.id,
                'comment': lead.description,
                'section_id': lead.section_id.id or False,
                'parent_id': parent_id,
                'phone': lead.phone,
                'mobile': lead.mobile,
                'email': tools.email_split(lead.email_from)
                         and tools.email_split(lead.email_from)[0] or False,
                'fax': lead.fax,
                'title': lead.title and lead.title.id or False,
                'function': lead.function,
                'street': lead.street,
                'street2': lead.street2,
                'zip': lead.zip,
                'city': lead.city,
                'country_id': lead.country_id and lead.country_id.id or False,
                'state_id': lead.state_id and lead.state_id.id or False,
                'is_company': is_company,
                'district': lead.district,
                'state_id_kladr': lead.state_id_kladr,
                'house': lead.house,
                'office': lead.office,
                'type': 'contact'}
        partner = partner.create(vals)
        return partner
