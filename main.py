from fastapi import FastAPI



from src.router.get_all_invoices import get_all_invoice_routes
from src.router.get_invoice_num import get_invoice_num_router



app = FastAPI()

@app.get("/")
async def index():
    return {
        "message" : "this is index"
    }

@app.get("/invoice")
async def get_all_invoice():
    return await get_all_invoice_routes()

@app.get("/invoice/{invoice_number}")
async def get_invoice (invoice_number: str):
    return get_invoice_num_router(invoice_number)



