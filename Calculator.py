from tkinter import END, Button, Entry, Tk;

window = Tk();
window.title("Calculator");

i = 0;

# Entrada de los Datos

e_text = Entry(window, font= ("Calibri 20"));
e_text.grid(row = 0, columnspan = 4, padx = 5, pady = 5);


# Funcionalidad
def click_button(valor):
  global i;
  e_text.insert(i, valor);
  i += 1;


def delete():
  e_text.delete(0, END);
  i = 0;


def operation():
  equation = e_text.get();
  result = eval(equation);
  e_text.delete(0, END);
  e_text.insert(0, result);
  i = 0;


# Numeros
button1 = Button(window, text = "1", width = 5, height = 2, command = lambda: click_button(1));
button2 = Button(window, text = "2", width = 5, height = 2, command = lambda: click_button(2));
button3 = Button(window, text = "3", width = 5, height = 2, command = lambda: click_button(3));
button4 = Button(window, text = "4", width = 5, height = 2, command = lambda: click_button(4));
button5 = Button(window, text = "5", width = 5, height = 2, command = lambda: click_button(5));
button6 = Button(window, text = "6", width = 5, height = 2, command = lambda: click_button(6));
button7 = Button(window, text = "7", width = 5, height = 2, command = lambda: click_button(7));
button8 = Button(window, text = "8", width = 5, height = 2, command = lambda: click_button(8));
button9 = Button(window, text = "9", width = 5, height = 2, command = lambda: click_button(9));
button0 = Button(window, text = "0", width = 15, height = 2, command = lambda: click_button(0));

# Botones
button_Delete = Button(window, text = "AC", width = 5, height = 2, command = lambda: delete());
button_Parentesis1 = Button(window, text= "(", width = 5, height = 2, command = lambda: click_button('('));
button_Parentesis2 = Button(window, text = ")", width = 5, height = 2, command = lambda: click_button(")"));
button_Punto = Button(window, text = ".", width = 5, height = 2, command = lambda: click_button("."));

# Operaciones
button_Div = Button(window, text = "/", width = 5, height = 2,command = lambda: click_button("/"));
button_Mult = Button(window, text = "x", width = 5, height = 2, command = lambda: click_button("*"));
button_Sum = Button(window, text = "+", width = 5, height = 2, command = lambda: click_button("+"));
button_Rest = Button(window, text = "-", width = 5, height = 2, command = lambda: click_button("-"));
button_Igual = Button(window, text = "=", width = 5, height = 2, command = lambda: operation());

# Mostrar Botonoes en la Pantalla
# Fila1
button_Delete.grid(row = 1, column = 0, padx = 5, pady = 5);
button_Parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5);
button_Parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5);
button_Div.grid(row = 1, column = 3, padx = 5, pady = 5);

# Fila2
button7.grid(row = 2, column = 0, padx = 5, pady = 5);
button8.grid(row = 2, column = 1, padx = 5, pady = 5);
button9.grid(row = 2, column = 2, padx = 5, pady = 5);
button_Mult.grid(row = 2, column = 3, padx = 5, pady = 5);

# Fila3
button4.grid(row = 3, column = 0, padx = 5, pady = 5);
button5.grid(row = 3, column = 1, padx = 5, pady = 5);
button6.grid(row = 3, column = 2, padx = 5, pady = 5);
button_Rest.grid(row = 3, column = 3, padx = 5, pady = 5);

# Fila4
button1.grid(row = 4, column = 0, padx = 5, pady = 5);
button2.grid(row = 4, column = 1, padx = 5, pady = 5);
button3.grid(row = 4, column = 2, padx = 5, pady = 5);
button_Sum.grid(row = 4, column = 3, padx = 5, pady = 5);

# Fila5
button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5);
button_Punto.grid(row = 5, column = 2, padx = 5, pady = 5);
button_Igual.grid(row = 5, column = 3, padx = 5, pady = 5);

window.mainloop();