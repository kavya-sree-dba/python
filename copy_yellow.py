from openpyxl import load_workbook, Workbook
from copy import copy

source = r"C:\Users\Dell\Downloads\python_class\Book1.xlsx"
destination = r"C:\Users\Dell\Downloads\python_class\Book4.xlsx"

wb = load_workbook(source)
ws = wb.active

new_wb = Workbook()
new_ws = new_wb.active

for row in ws.iter_rows():
    for cell in row:
        if cell.fill.fill_type == "solid":
            new_cell = new_ws.cell(
                row=cell.row,
                column=cell.column,
                value=cell.value
            )
            new_cell.fill = copy(cell.fill)
            new_cell.font = copy(cell.font)
            new_cell.border = copy(cell.border)
            new_cell.alignment = copy(cell.alignment)

new_wb.save(destination)

print("Done! Check copy_yellow.xlsx")