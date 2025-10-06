from fastapi import HTTPException
from src.lib.manageDB import ManageDB

md = ManageDB()

def delete_invoice_router(invoice_number):
    invoices = md.read_invoice()

    for index, invoice in enumerate(invoices):
        if invoice["invoice_num"] == invoice_number:
            invoices.pop(index)

            md.write_invoice(invoices)

            return {
                "success" : True,
                "message" : "delete contact"
            }
    raise HTTPException(status_code=404,detail="contact not found")