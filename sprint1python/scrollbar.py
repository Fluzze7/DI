#import de clase para interfaces gráficas
import tkinter as tk

#crear y dimensionar ventana principal
root = tk.Tk()
root.geometry("800x500")
root.title("Ejercicio10 ")

#crear un frame que ocupe toda la pantalla
frame = tk.Frame(root)
frame.pack(fill="both",expand=True)

#crear un textbox en el frame con un texto muy largo
textbox = tk.Text(frame, wrap="word",width=50)
textbox.grid(row=0, column=0, sticky="nsew")
textbox.insert(tk.END,  """
Lorem ipsum dolor sit amet consectetur adipiscing elit vivamus praesent curae, sociis dapibus torquent cubilia quam varius dictum gravida senectus donec, suscipit facilisi interdum mus eget laoreet malesuada dictumst ad. Tincidunt nullam euismod feugiat porta litora bibendum massa, maecenas pellentesque tempor sociis fringilla taciti, class ullamcorper ante aenean risus dui. Aliquet dui nisl senectus inceptos vel elementum aliquam facilisis pretium, natoque habitant enim montes litora nascetur orci massa, rutrum ante nibh taciti ullamcorper aptent lacus mollis. Elementum dapibus sed eleifend maecenas consequat dis magnis hendrerit, senectus posuere nibh felis suscipit et diam facilisis, urna parturient aenean cras velit congue cubilia.
Blandit massa pretium rhoncus est nulla netus interdum cubilia vestibulum, hac urna sollicitudin molestie accumsan sociosqu rutrum iaculis nisi, quam enim ornare nec ultrices tempor neque maecenas. Viverra natoque conubia justo, et habitant, posuere curae. Placerat porta viverra turpis curabitur lacinia quam ridiculus, aenean malesuada netus pulvinar ullamcorper molestie sed potenti, ad dignissim vitae mauris congue tincidunt. Dui taciti gravida est aliquet dictumst at cum, aptent mollis felis lobortis posuere tempor ac ridiculus, porta ultrices neque lectus arcu primis.
A lectus bibendum netus convallis nunc orci, tristique justo posuere praesent commodo, phasellus fames quisque dignissim sociis. Etiam placerat fusce fames bibendum feugiat nunc aptent urna conubia primis, neque odio faucibus purus ullamcorper sagittis lacinia class mattis, magnis dignissim molestie pharetra hac venenatis varius pulvinar nec. Ut montes phasellus inceptos maecenas sagittis justo conubia nullam curae non elementum diam magna leo nisi, eget lectus lacinia dictum rutrum cras hendrerit risus feugiat a quam laoreet aenean. Rhoncus mus molestie sed volutpat dictumst malesuada hendrerit, dignissim porttitor proin laoreet a lectus ante, sagittis suscipit condimentum metus ornare cras.
Imperdiet nulla natoque ridiculus arcu porttitor class viverra, habitasse lacinia tincidunt inceptos iaculis nisl, varius habitant ac himenaeos suscipit condimentum. Iaculis ut himenaeos leo scelerisque non tincidunt habitant ultricies tempus sociis, inceptos fusce rutrum tellus sollicitudin venenatis aliquet erat. Venenatis vehicula himenaeos leo et feugiat tortor mi urna semper, rhoncus accumsan libero fusce hac non lacinia per, bibendum fames ullamcorper elementum neque augue platea penatibus. Hendrerit primis aenean torquent dignissim vel hac sem, sollicitudin libero ut volutpat velit nisl mollis, rutrum dictumst mus faucibus habitant dapibus.
""")
#crear scrollbar vertical para moverse por el texto
vert_scroll = tk.Scrollbar(frame,orient="vertical", command=textbox.yview)
vert_scroll.grid(row=0, column=1, sticky="ns")

#iniciar el programa
root.mainloop()