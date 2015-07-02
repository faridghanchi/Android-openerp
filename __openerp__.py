# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 - Probuse Consulting Services Pvt.Ltd.(<http://probuse.com>).
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
{
    'name': 'Memco projects',
    'category': '',
    'version': '1.0',
    'author': 'Probuse CS & Amazing Bizs',
    'depends': ['crm','purchase','sale','stock','delivery','mrp','mrp_operations','account','sale_after_service','probuse_product_search','memco_po_discount'],
    'website': '',

    'description': """ 
    Improved Purchase, Production, Sale
    """,
    'summary':"""""",
    'data': [
        'security/memco_security.xml',
        'security/ir.model.access.csv',
        'views/purchase.xml',
        'views/report_purchasequotation1.xml',
        'views/report_purchaseorder.xml',
        'views/report_jobcard.xml',
        'template/purchase_manager.xml',
        'views/sale_view.xml',
        'wizard/stock_move_view.xml',
        'views/move_view.xml',
#        'wizard/request_lesser.xml',
        'wizard/stock_move_release_view.xml',
        'wizard/stockmove_assign_to_project_view.xml',
        'wizard/request_lesser_view.xml',
        'views/mrp_view.xml',
        'views/product_view.xml',
        'views/partner_view.xml',
        'views/report_saleorder.xml',
        'views/account_view.xml',
        'views/report_mrporder.xml',
        'views/report_mrporder1.xml',
        'views/report_mrporder_additional.xml',
        'views/report_invoice.xml',
#        'views/incoming_view.xml',
        'views/report_mrpbomstructure.xml',
        'views/report_mrpbomstructure_technical.xml',
        'reports/report.xml',
        'template/create_job_card.xml',
        'views/crm_view.xml',
        'views/oppo_stage_data.xml',
        'template/design_gm_action_data.xml',
        'wizard/create_internation_carrier_invoice.xml',
        'wizard/create_local_carrier_invoice.xml',
        'views/picking_view.xml',
        'views/commission.xml',
        'views/report_commission.xml',
        'views/stock_quant_view.xml',
        'wizard/stock_transfer_details.xml',
        'views/lc_form_view.xml',
        'template/notification_shipment.xml',
        'views/memco_cron.xml',
        'views/report_project_concept_auto.xml',
        'views/report_project_concept_design.xml',
        'views/lesser_view.xml',
        'template/production_manager_template.xml',
#        'memco_po_discount/purchase.xml',
        'views/purchase_discount.xml',
        'views/stock_data.xml',
    ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
