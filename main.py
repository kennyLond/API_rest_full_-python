from fastapi import FastAPI
from pydantic import BaseModel




from src.router.get_all_invoices import get_all_invoice_routes
from src.router.get_invoice_num import get_invoice_num_router
from src.router.post_invoice import post_invoice_router
from src.router.put_invoice import put_invoice_router
from src.router.delete_invoice import delete_invoice_router


class InvoiceModel(BaseModel):
    id:str
    invoice_num: str
    name: str
    phone: str


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

@app.post("/invoice")
async def add_invoice(new_invoice_num : InvoiceModel):
    return post_invoice_router(new_invoice_num)

@app.put("/invoice/{invoice_num}")
async def update_invoice(invoice_num:str, new_invoice_num:InvoiceModel):
    return put_invoice_router(invoice_num, new_invoice_num)

@app.delete("/invoice/{invoice_num}")
async def remove_invoice(invoice_num:str):
    return delete_invoice_router(invoice_num)