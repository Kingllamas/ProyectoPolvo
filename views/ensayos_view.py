def reinicio(self):
    self.ocultar()
    self.inicio()
        
    
def buscar_muestra(self):
    self.ocultar()
    self.frame_buscar.pack(expand=True,fill='BOTH')

def nueva_muestra(self):
    self.ocultar()

def ocultar(self):
    for frame in self.frames:
        frame.pack_forget()
    self.frame_buscar.pack_forget()