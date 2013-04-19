import pygtk
pygtk.require('2.0')
import gtk
# -*- coding: utf-8 -*-


class Analizador_Lexicografico:
    def callback(self, widget, entrada, boton1, boton2, etiquetafin, respuesta, imagensad,imagentroll):
        boton1.hide()
        boton2.hide()
        etiquetafin.hide()
        respuesta.set_text("")
        entrada.set_text("")
        imagensad.hide()
        imagentroll.hide()

    def enter_callback(self, widget, entry, label, label2, button, button2,imagensad, imagentroll): #del entry
        #hide
        imagentroll.hide()
        imagensad.hide()
        
        entrada = entry.get_text()
        #### AQUI EMPEZAREMOS LO DEL AUTOMATA ###
        palabras_reservadas = {'int':'ok', 'float':'ok', 'switch':'ok', 'if':'ok', 'else':'ok', 'for':'ok',
                               'do':'ok', 'while':'ok', 'case':'ok', 'long':'ok', 'break':'ok', 'continue':'ok',
                               'sizeof':'ok', 'enum':'ok', 'typedef':'ok', 'struct':'ok', 'goto':'ok', 'default':'ok',
                               'signed':'ok', 'unsigned':'ok', 'return':'ok', 'union':'ok', 'auto':'ok', 'void':'ok',
                               'register':'ok', 'double':'ok', 'char':'ok', 'const':'ok', 'extern':'ok', 'short':'ok',
                               'volatile':'ok', 'static':'ok'}
        pal = palabras_reservadas.get(entrada, None)
        if pal == 'ok':
            imagentroll.show()
            label.set_text("""La Cadena si es un componente lexico valido.
        Corresponde a una Palabra reservada""")
            label2.show()
            button.show()
            button2.show()
            return
        entrada = entrada+"\n"
        #Que empiece el automata aqui
        #      L        
        #      e    
        #      t    
        #      r                       D
        #      a     A                 i
        #      s     B                 g
        #      G     C                 i                       *                                    
        #      -     D                 t                       /                             >      
        #      Z     F     H     E     o     .     +     -     %     =     &     |     !     <    [FDC]

        f = (( 1  ,  1  ,  1  ,  1  ,  2  ,  3  , 12  , 13  , 16  , 23  , 18  , 19  , 21  , 22  ,  -1 ),  #q0
             ( 1  ,  1  ,  1  ,  1  ,  1  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q1
             (-2  ,  10 ,  8  , 11  ,  2  ,  3  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q2
             (-2  , -2  , -2  , -2  ,  4  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  -1 ),  #q3
             (-2  , -2  ,  5  , -2  ,  4  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q4
             (-2  , -2  , -2  , -2  ,  7  , -2  ,  6  ,  6  , -2  , -2  , -2  , -2  , -2  , -2  ,  -1 ),  #q5
             (-2  , -2  , -2  , -2  ,  7  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  -1 ),  #q6
             (-2  , -2  , -2  , -2  ,  7  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q7
             (-2  , 10  , 10  , 11  ,  9  , -2  ,  6  ,  6  , -2  , -2  , -2  , -2  , -2  , -2  ,  -1 ),  #q8
             (-2  , 10  , 10  , 11  ,  9  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q9
             (-2  , 10  , 10  , 11  , 10  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  -1 ),  #q10
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q11
             (-2  , -2  , -2  , -2  , 14  ,  3  , 15  , -2  , -2  , 17  , -2  , -2  , -2  , -2  ,  100),  #q12
             (-2  , -2  , -2  , -2  , 14  ,  3  , -2  , 15  , -2  , 17  , -2  , -2  , -2  , -2  ,  100),  #q13
             (-2  , -2  ,  5  , -2  , 14  ,  3  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q14
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q15
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , 17  , -2  , -2  , -2  , -2  ,  100),  #q16
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q17
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , 20  , -2  , -2  , -2  ,   -1),  #q18
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , 20  , -2  , -2  ,   -1),  #q19
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100),  #q20
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , 24  , -2  , -2  , -2  , -2  ,  100),  #q21
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , 24  , -2  , -2  , -2  , -2  ,  100),  #q22
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , 24  , -2  , -2  , -2  , -2  ,  100),  #q23
             (-2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  , -2  ,  100))  #q24
        
        estado = 0
        while estado != 100:
            for simbolo in entrada:
                opcion = {'g':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,
                          'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,
                          'G':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,
                          'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,'_':0,
                          'a':1,'b':1,'c':1,'d':1,'f':1,'A':1,'B':1,'C':1,'D':1,'F':1,
                          'e':2,'E':2,
                          'H':3,'h':3,
                          '0':4,'1':4,'2':4,'3':4,'4':4,'5':4,'6':4,'7':4,'8':4,'9':4,
                          '.':5,
                          '+':6,
                          '-':7,
                          '*':8, '%':8, '/':8,
                          '=':9,
                          '&':10,
                          '|':11,
                          '!':12,
                          '<':13,'>':13,
                          '\n':14}
                
                entrada = opcion.get(simbolo, -100)
                if entrada == -100:
                    imagensad.show()
                    label.set_markup('<span foreground="red"><b>Error:</b> Cadena Invalida! (Caracter invalido)</span>')
                    label2.show()
                    button.show()
                    button2.show()
                    return
                else:
                    estadox = estado
                    estado = f[estado][entrada]
                    
                if estado == -2:
                    imagensad.show()
                    label.set_markup('<span foreground="red"><b>Error:</b> Cadena Invalida! (Caracter en una posicion inadecuada)</span>')
                    label2.show()
                    button.show()
                    button2.show()
                    return
                    
                if estado == -1:
                    imagensad.show()
                    label.set_markup('<span foreground="red"><b>Error:</b> Cadena Invalida! (Cadena incompleta)</span>')
                    label2.show()
                    button.show()
                    button2.show()
                    return

                if estado == 100:
                    #print "Cadena Valida! \n  Corresponde a: "
                    if estadox == 1:
                        #print "Identificador"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Identificador""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 2:
                        #print "Numero Entero"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Numero Entero""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 4:
                        #print "Numero Flotante"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Numero Flotante""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 7:
                        #print "Numero Exponencial"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Numero Exponencial""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 9:
                        #print "Numero Exponencial"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Numero Exponencial""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 11:
                        #print "Numero Hexadecimal"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Numero Hexadecimal""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 12:
                        #print "Operador Aritmetico"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Aritmetico""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 13:
                        #print "Operador Aritmetico"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Aritmetico""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 14:
                        #print "Numero Entero"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Numero Entero""")
                        label2.show()
                        button.show()
                        button2.show()                        
                    elif estadox == 15:
                        #print "Operador de Incremento o Decremento"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador de Incremento o Decremento""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 16:
                        #print "Operador Aritmetico"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Aritmetico""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 17:
                        #print "Operador Aritmetico y Asignacion"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Aritmetico y de Asignacion""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 20:
                        #print "Operador Logico"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Logico""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 21:
                        #print "Operador Logico"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Logico""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 22:
                        #print "Operador Relacional"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Relacional""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 23:
                        #print "Operador de Asignacion"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador de Asignacion""")
                        label2.show()
                        button.show()
                        button2.show()
                    elif estadox == 24:
                        #print "Operador Relacional"
                        imagentroll.show()
                        label.set_text("""La Cadena si es un componente lexico valido.
                Corresponde a un Operador Relacional""")
                        label2.show()
                        button.show()
                        button2.show()

        

        
        
    
    def get_main_menu(self, window): #del menubar
        accel_group = gtk.AccelGroup()
        item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
        item_factory.create_items(self.menu_items)
        window.add_accel_group(accel_group)
        self.item_factory = item_factory
        return item_factory.get_widget("<main>")

    def ventanita(self,w,data):
        ventanaprov = gtk.Window(gtk.WINDOW_TOPLEVEL)
        ventanaprov.set_size_request(300,170)
        ventanaprov.set_title("Creditos")
        ventanaprov.connect("delete_event", lambda w,e: ventanaprov.hide())
        #y aqui el cagadero de los creditos
        vbox = gtk.VBox(gtk.FALSE,0)
        ventanaprov.add(vbox)
        vbox.show()
        
        #imagen
        pixbufanim = gtk.gdk.PixbufAnimation("dancing.gif")
        imagen = gtk.Image()
        imagen.set_from_animation(pixbufanim)
        vbox.pack_start(imagen, gtk.TRUE, gtk.FALSE, 0)
        imagen.show()
        
        label = gtk.Label(" ")
        label.set_markup("""                             <b>Proyecto en Python</b>
    <b>LENGUAJES DE PROGRAMACION COMPARADOS</b>
                        <span foreground="blue"><b>Analizador Lexicografico</b></span>
                    Arturo Ivan Ramirez Martinez
                                   207617402
                            Lic. en Informatica""")
        vbox.pack_start(label, gtk.TRUE, gtk.FALSE, 0)
        label.show()
        ventanaprov.show()
        
    def __init__(self):
##       Creo los menus pa mi barra de menu
        self.menu_items = (
            ("/_Creditos", None, None, 0, "<Branch>"),
            ("/Creditos/Ver Creditos", None, self.ventanita, 0, None)
        )
        
##      Creo la ventana  
        ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)
        ventana.set_size_request(520,170)
        ventana.set_title("Analizador Lexicografico")
        ventana.connect("delete_event", lambda w,e: gtk.main_quit())

##      VBOX PRINCIPAL  
        vbox = gtk.VBox(gtk.FALSE, 0)
        ventana.add(vbox)
        vbox.show()

##      VBOX1 DENTRO DE VBOX
        vbox1 = gtk.VBox(gtk.FALSE, 1)
        vbox1.set_border_width(1)
        vbox.add(vbox1)
        vbox1.show()

        # procedemos a hacer el menubar
        menubar = self.get_main_menu(ventana)
        vbox1.pack_start(menubar, gtk.FALSE, gtk.TRUE, 0)
        menubar.show()

##      HBOXTITLE DENTRO DE VBOX
        hboxtitle = gtk.HBox(gtk.FALSE, 0)
        hboxtitle.set_border_width(1)
        vbox.add(hboxtitle)
        hboxtitle.show()

        # procedemos a hacer la label
        label2 = gtk.Label("")
        label2.set_markup("<b>RECONOCEDOR DE COMPONENTES LEXICOS</b>")
        hboxtitle.pack_start(label2, gtk.TRUE, gtk.FALSE, 0)
        label2.show()
        

##      HBOX1 DENTRO DE VBOX
        hbox1 = gtk.HBox(gtk.FALSE, 0)
        hbox1.set_border_width(1)
        vbox.add(hbox1)
        hbox1.show()

        # procedemos a hacer la label
        label = gtk.Label("")
        label.set_markup("<i>Cadena a evaluar:</i>")
        hbox1.pack_start(label, gtk.TRUE, gtk.FALSE, 0) #inicialmente era FALSE TRUE
        label.show()

##      HBOX2 DENTRO DE VBOX
        hbox2 = gtk.HBox(gtk.FALSE, 0)
        vbox.add(hbox2)
        hbox2.show()

        ##      HBOX3 DENTRO DE VBOX
        hbox3 = gtk.HBox(gtk.FALSE, 0)
        hbox3.set_border_width(1) #label
        vbox.add(hbox3)
        hbox3.show()

        respuesta = gtk.Label("")
        hbox3.pack_start(respuesta, gtk.TRUE, gtk.FALSE, 0)
        respuesta.show()



##      HBOXfinal DENTRO DE VBOX
        hboxFINAL = gtk.HBox(gtk.FALSE, 0)
        vbox.add(hboxFINAL)
        hboxFINAL.show()

        etiquetafin = gtk.Label("Deseas analizar una cadena? ")
        hboxFINAL.pack_start(etiquetafin, gtk.TRUE, gtk.FALSE, 0)
        etiquetafin.hide()
        

        boton2 = gtk.Button("No")
        boton2.connect("clicked", lambda w: gtk.main_quit())
        hboxFINAL.pack_start(boton2, gtk.FALSE, gtk.TRUE, 0)
        boton2.hide()
        boton1 = gtk.Button("Si")
        hboxFINAL.pack_start(boton1, gtk.FALSE, gtk.TRUE, 0)
        boton1.hide()

        pixbufanim = gtk.gdk.PixbufAnimation("sadface.png")
        imagensad = gtk.Image()
        imagensad.set_from_animation(pixbufanim)
        hbox3.pack_start(imagensad, gtk.TRUE, gtk.FALSE, 0)
        imagensad.hide()

        pixbufanim = gtk.gdk.PixbufAnimation("trollface.png")
        imagentroll = gtk.Image()
        imagentroll.set_from_animation(pixbufanim)
        hbox3.pack_start(imagentroll, gtk.TRUE, gtk.FALSE, 0)
        imagentroll.hide()

        # procedemos a hacer el entry
        entrada = gtk.Entry()
        entrada.set_max_length(32) #el maximo que acepta / def 50
        entrada.connect("activate", self.enter_callback, entrada, respuesta, etiquetafin, boton1, boton2,imagensad,imagentroll)
        hbox2.pack_start(entrada, gtk.TRUE, gtk.FALSE, 0) #inicialmente era TRUE TRUE
        entrada.show()


        boton1.connect("clicked", self.callback, entrada, boton1, boton2, etiquetafin, respuesta, imagensad, imagentroll)        
        ventana.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    Analizador_Lexicografico()
    main()

