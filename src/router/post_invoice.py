from src.lib.manageDB import ManageDB

md = ManageDB()

def post_invoice_router(new_invoice_num):
    invoice = md.read_invoice()
    new_invoice_num = new_invoice_num.model_dump()

    invoice.append(new_invoice_num)

    md.write_invoice(invoice)
    return{
        "success": True,
        "message": "Added new Invoice"
    }