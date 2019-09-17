# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
import operator

class inher_user(models.Model):
	_inherit = "res.users"

	menu_ids = fields.Many2many('ir.ui.menu',string="Display Name")

class inher_menus(models.Model):
	_inherit = 'ir.ui.menu'

	@api.model
	@tools.ormcache_context('self._uid', 'debug', keys=('lang',))
	def load_menus(self, debug):

		main_list = []
		lat_list = []
		fields = ['name', 'sequence', 'parent_id', 'action', 'web_icon', 'web_icon_data']

		menu_roots = self.get_user_roots()

		menu_roots_ids = self.get_user_roots()
		for i in menu_roots_ids:
			main_list.append(i.id)

		users = self.env.user

		if users.menu_ids:
			for menus in users.menu_ids:
				lat_list.append(menus.id)
				b = set(main_list) - set(lat_list)

			menu_roots = self.browse(b)
		
		menu_roots_data = menu_roots.read(fields) if menu_roots else []
		menu_root = {
			'id': False,
			'name': 'root',
			'parent_id': [-1, ''],
			'children': menu_roots_data,
			'all_menu_ids': menu_roots.ids,
		}

		if not menu_roots:
			return menu_root

		menus = self.search([('id', 'child_of', menu_roots.ids)])
		menu_items = menus.read(fields)
		
		menu_items.extend(menu_roots_data)
		menu_root['all_menu_ids'] = menus.ids
		
		menu_items_map = {menu_item["id"]: menu_item for menu_item in menu_items}
		for menu_item in menu_items:
			parent = menu_item['parent_id'] and menu_item['parent_id'][0]
			if parent in menu_items_map:
				menu_items_map[parent].setdefault(
					'children', []).append(menu_item)

		for menu_item in menu_items:
			menu_item.setdefault('children', []).sort(key=operator.itemgetter('sequence'))

		(menu_roots + menus)._set_menuitems_xmlids(menu_root)

		return menu_root