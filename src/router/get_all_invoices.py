from src.lib.manageDB import ManageDB

async def get_all_invoice_routes():
    md = ManageDB()
    return  md.read_invoice()