from src.lib.manageDB import ManageDB
from fastapi import HTTPException

md = ManageDB()

def put_invoice_router(invoice_number, new_invoice_num):
    invoices = md.read_invoice()  # Leemos todas las facturas

    for index, inv in enumerate(invoices):
        if inv["invoice_num"] == invoice_number:
            # Convertimos el nuevo modelo en diccionario
            updated_invoice = new_invoice_num.model_dump()

            # Si algún campo viene vacío, conservamos el valor anterior
            if new_invoice_num.name == "":
                updated_invoice["name"] = inv["name"]

            if new_invoice_num.phone == "":
                updated_invoice["phone"] = inv["phone"]

            # Reemplazamos la factura antigua con la actualizada
            invoices[index] = updated_invoice

            # Guardamos los cambios
            md.write_invoice(invoices)

            return {"success": True, "message": "Invoice updated successfully"}

    # Si no se encontró la factura
    raise HTTPException(status_code=404, detail="Invoice not found")
