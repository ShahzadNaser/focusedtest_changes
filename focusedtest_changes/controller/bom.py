import frappe
from frappe import _
from frappe.utils import flt
from erpnext.manufacturing.doctype.bom.bom import BOM

class BOMCUSTOM(BOM):
    def calculate_cost(self, save_updates=False, update_hour_rate=False):
        """Calculate bom totals"""
        self.calculate_op_cost(update_hour_rate)
        self.calculate_rm_cost()
        self.calculate_sm_cost()
        if save_updates:
            # not via doc event, table is not regenerated and needs updation
            self.calculate_exploded_cost()

        self.total_cost = self.production_cost + self.operating_cost + self.raw_material_cost - self.scrap_material_cost
        self.base_total_cost = (
            self.base_operating_cost + self.base_raw_material_cost - self.base_scrap_material_cost
        )

    def calculate_rm_cost(self, save=False):
        """Fetch RM rate as per today's valuation rate and calculate totals"""
        total_rm_cost = 0
        base_total_rm_cost = 0

        for d in self.get("items"):
            old_rate = d.rate
            rate = frappe.db.get_value("Purchase Order Item", {"item_code":d.item_code}, "MAX(rate)") or self.get_rm_rate(
                {
                    "company": self.company,
                    "item_code": d.item_code,
                    "bom_no": d.bom_no,
                    "qty": d.qty,
                    "uom": d.uom,
                    "stock_uom": d.stock_uom,
                    "conversion_factor": d.conversion_factor,
                    "sourced_by_supplier": d.sourced_by_supplier,
                }
            )

            
            d.rate = rate * 1.15
            d.base_rate = flt(d.rate) * flt(self.conversion_rate)
            d.amount = flt(d.rate, d.precision("rate")) * flt(d.qty, d.precision("qty"))
            d.base_amount = d.amount * flt(self.conversion_rate)
            d.qty_consumed_per_unit = flt(d.stock_qty, d.precision("stock_qty")) / flt(
                self.quantity, self.precision("quantity")
            )

            total_rm_cost += d.amount
            base_total_rm_cost += d.base_amount
            if save and (old_rate != d.rate):
                d.db_update()

        self.raw_material_cost = total_rm_cost
        self.base_raw_material_cost = base_total_rm_cost