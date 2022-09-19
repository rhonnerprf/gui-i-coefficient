import math
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Coeficiente de influencia I")
root.geometry('400x200')

title = ttk.Label(root, text="¡Bienvenidos al programa para encontrar el coeficiente de influencia I!", justify="center").grid(row=0, columnspan=2)

title_2 = ttk.Label(root, text="Desarrollado por Rhonner Ramírez", justify="center").grid(row=1, columnspan=2)

label1 = ttk.Label(root, text="B = ").grid(row=2)
label2 = ttk.Label(root, text="L = ").grid(row=3)
label3 = ttk.Label(root, text="z = ").grid(row=4)

B_var = DoubleVar(root, value=1.000)
L_var = DoubleVar(root, value=1.000)
z_var = DoubleVar(root, value=1.000)

def coeficiente_i(B_var, L_var, z_var):
    B = float(B_var.get())
    L = float(L_var.get())
    z = float(z_var.get())
    m = B/z
    n = L/z
    D = m**2+n**2-m**2*n**2+1
    acrescentador = math.pi*(D-abs(D))/(2*D)
    I = (1/(4*math.pi))*((2*m*n*math.sqrt(m**2+n**2+1))/(m**2+n**2+m**2*n**2+1)*(m**2+n**2+2)/(m**2+n**2+1)+math.atan((2*m*n*math.sqrt(m**2+n**2+1))/(m**2+n**2-m**2*n**2+1))+acrescentador)
    control = math.atan((2*m*n*math.sqrt(m**2+n**2+1))/(m**2+n**2-m**2*n**2+1))
    return [round(m,3), round(n,3), round(I,3)]

entry_B = ttk.Entry(root, width = 20, textvariable=B_var).grid(row=2, column=1)
entry_L = ttk.Entry(root, width = 20, textvariable=L_var).grid(row=3, column=1)
entry_z = ttk.Entry(root, width = 20, textvariable=z_var).grid(row=4, column=1)

def button_command():
    result_m = ttk.Label(root, text="m = " + str(coeficiente_i(B_var, L_var, z_var)[0]), justify="center").grid(row=6, column=0)
    result_n = ttk.Label(root, text="n = " + str(coeficiente_i(B_var, L_var, z_var)[1]), justify="center").grid(row=6, column=1)
    result_i = ttk.Label(root, text="I = " + str(coeficiente_i(B_var, L_var, z_var)[2]), justify="center").grid(row=7, columnspan=2)

button = ttk.Button(root, text="Calcular", command=button_command).grid(row=5, columnspan=2)

root.mainloop()
