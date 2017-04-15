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

ADDRESS_KLADR_FIELDS = ('street', 'street2', 'zip',
                        'city', 'state_id', 'country_id',
                        'house', 'office', 'district',
                        'state_id_kladr')


class ResPartner(models.Model):
    _inherit = "res.partner"

    district = fields.Char(string='District',
                           size=128)
    state_id_kladr = fields.Char(string='State',
                                 size=128)
    house = fields.Char(string='House', size=64)
    office = fields.Char(string='Office', size=64)
    full_r_address = fields.Char(compute='z_full_r_address',
                                 string="Full address")
    # Real address
    real_use_main = fields.Boolean(string=u'Исп.юр.адр.')
    country_id_real = fields.Many2one('res.country',
                                      string='Country',
                                      ondelete='restrict')
    city_real = fields.Char(string='City',
                            size=128)
    street_real = fields.Char(string='Street',
                              size=128)
    zip_real = fields.Char(string='Zip',
                           change_default=True,
                           size=24)
    district_real = fields.Char(string='District',
                                size=128)
    state_id_real = fields.Char(string='State',
                                size=128)
    house_real = fields.Char(string='House',
                             size=64)
    office_real = fields.Char(string='Office',
                              size=64)
    full_real_address = fields.Char(compute='z_full_real_address',
                                    string="Full address")
    # Post address
    post_use_main = fields.Boolean(string=u'Исп.юр.адр.')
    country_id_post = fields.Many2one('res.country',
                                      string='Country',
                                      ondelete='restrict')
    city_post = fields.Char(string='City',
                            size=128)
    street_post = fields.Char(string='Street',
                              size=128)
    zip_post = fields.Char(string='Zip',
                           change_default=True,
                           size=24)
    district_post = fields.Char(string='District',
                                size=128)
    state_id_post = fields.Char(string='State',
                                size=128)
    house_post = fields.Char(string='House',
                             size=64)
    office_post = fields.Char(string='Office',
                              size=64)
    full_post_address = fields.Char(compute='z_full_post_address',
                                    string="Full address")

    def _address_fields(self):
        """ Returns the list of address fields that are synced from the parent
        when the `use_parent_address` flag is set. """
        return list(ADDRESS_KLADR_FIELDS)

    def z_full_r_address(self):
        res = {}
        if self.ids:
            for obj in self.browse(self.ids):
                partner = obj
                partner_address = ''
                if partner:
                    if partner.zip:
                        partner_address = partner.zip
                    if partner.state_id_kladr:
                        if partner_address != '':
                            if partner.state_id_kladr:
                                partner_address += ', ' + partner.state_id_kladr
                        else:
                            if partner.state_id_kladr:
                                partner_address = partner.state_id_kladr
                    if partner.district:
                        if partner_address != '':
                            partner_address += ', ' + partner.district
                        else:
                            partner_address = partner.district
                    if partner.city:
                        if partner_address != '':
                            partner_address += ', ' + partner.city
                        else:
                            partner_address = partner.city
                    if partner.street:
                        if partner_address != '':
                            partner_address += ', ' + partner.street
                        else:
                            partner_address = partner.street
                    if partner.house:
                        if partner_address != '':
                            partner_address += ', ' + partner.house
                        else:
                            partner_address = partner.house
                    if partner.office:
                        if partner_address != '':
                            partner_address += ', ' + partner.office
                        else:
                            partner_address = partner.office
                res[obj.id] = partner_address
        return res

    def z_full_real_address(self):
        res = {}
        if self.ids:
            for obj in self.browse(self.ids):
                partner = obj
                partner_address = ''
                if partner:
                    if partner.zip_real:
                        partner_address = partner.zip_real
                    if partner.state_id_real:
                        if partner_address != '':
                            if partner.state_id_real:
                                partner_address += ', ' + partner.state_id_real
                        else:
                            if partner.state_id_real:
                                partner_address = partner.state_id_real
                    if partner.district_real:
                        if partner_address != '':
                            partner_address += ', ' + partner.district_real
                        else:
                            partner_address = partner.district_real
                    if partner.city_real:
                        if partner_address != '':
                            partner_address += ', ' + partner.city_real
                        else:
                            partner_address = partner.city_real
                    if partner.street_real:
                        if partner_address != '':
                            partner_address += ', ' + partner.street_real
                        else:
                            partner_address = partner.street_real
                    if partner.house_real:
                        if partner_address != '':
                            partner_address += ', ' + partner.house_real
                        else:
                            partner_address = partner.house_real
                    if partner.office_real:
                        if partner_address != '':
                            partner_address += ', ' + partner.office_real
                        else:
                            partner_address = partner.office_real

                res[obj.id] = partner_address
        return res

    def z_full_post_address(self):
        res = {}
        if self.ids:
            for obj in self.browse(self.ids):
                partner = obj
                partner_address = ''
                if partner:
                    if partner.zip_post:
                        partner_address = partner.zip_post
                    if partner.state_id_post:
                        if partner_address != '':
                            if partner.state_id_post:
                                partner_address += ', ' + partner.state_id_post
                        else:
                            if partner.state_id_post:
                                partner_address = partner.state_id_post
                    if partner.district_post:
                        if partner_address != '':
                            partner_address += ', ' + partner.district_post
                        else:
                            partner_address = partner.district_post
                    if partner.city_post:
                        if partner_address != '':
                            partner_address += ', ' + partner.city_post
                        else:
                            partner_address = partner.city_post
                    if partner.street_post:
                        if partner_address != '':
                            partner_address += ', ' + partner.street_post
                        else:
                            partner_address = partner.street_post
                    if partner.house_post:
                        if partner_address != '':
                            partner_address += ', ' + partner.house_post
                        else:
                            partner_address = partner.house_post
                    if partner.office_post:
                        if partner_address != '':
                            partner_address += ', ' + partner.office_post
                        else:
                            partner_address = partner.office_post

                res[obj.id] = partner_address
        return res

    def onchange_state(self, state_name):
        result = {}
        state_ids = self.env['res.country.state'].search(
            [('name', '=', state_name)])
        if state_ids:
            state_obj = self.env['res.country.state'].browse(state_ids)
            if state_ids:
                result['state_id'] = state_obj[0].id
        return {'value': result}

    def real_change(self, check, country_id, city, district,
                    state_id_kladr, street, house, office, zip):
        if check:
            return {'value': {'country_id_real': country_id,
                              'city_real': city,
                              'street_real': street,
                              'zip_real': zip,
                              'district_real': district,
                              'state_id_real': state_id_kladr,
                              'house_real': house,
                              'office_real': office}}
        return {}

    def post_change(self, check, country_id, city, district,
                    state_id_kladr, street, house, office, zip):
        if check:
            return {'value': {'country_id_post': country_id,
                              'city_post': city,
                              'street_post': street,
                              'zip_post': zip,
                              'district_post': district,
                              'state_id_post': state_id_kladr,
                              'house_post': house,
                              'office_post': office}}
        return {}
