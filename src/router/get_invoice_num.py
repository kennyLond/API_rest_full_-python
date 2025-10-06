from fastapi import HTTPException
from src.lib.manageDB import ManageDB

def get_invoice_num_router(invoice_number):

    md = ManageDB()
    invoice_num = md.read_invoice()

    for invoice in invoice_num:
        if invoice["invoice_num"] == invoice_number:
            return invoice
    
    raise HTTPException(status_code=404, detail="INVOICE not found")
