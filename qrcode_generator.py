import tkinter as tk
import qrcode
from PIL import Image, ImageTk

class QRCodeGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("QR Code Generator")
        self.pack()
        self.create_widgets()


  
        #set background color of each widget separately
        self.input_label.configure(bg="#add8e6")
        self.input_entry.configure(bg="#8b00ff", fg="yellow")
        self.generate_button.configure(bg="#8b00ff", fg="yellow")
        self.size_label.configure(bg="#add8e6")
        self.size_entry.configure(bg="#add8e6",fg="green")
        self.color_label.configure(bg="#add8e6")
        self.color_entry.configure(bg="#add8e6",fg="green")
        self.error_label.configure(bg="#add8e6", fg="red")
        self.qr_label.configure(bg="#add8e6")

    def create_widgets(self):
        self.configure(bg="#add8e6")
        self.input_label = tk.Label(self, text="Enter text or URL:", anchor="w")
        self.input_label.pack(fill="x")  # align to left and fill horizontally
        self.input_entry = tk.Entry(self)
        self.input_entry.pack(fill="x")  # align to left and fill horizontally
        self.generate_button = tk.Button(self, text="Create",anchor="w", width=5, height=0,command=self.generate_qr)
        self.generate_button.pack(fill="y", padx=0, pady=5)
        self.generate_button.pack(side="top", padx=40, pady=5)  # align to left and fill horizontally
        self.size_label = tk.Label(self, text="Size:", anchor="w")
        self.size_label.pack(fill="x")  # align to left and fill horizontally
        self.size_entry = tk.Entry(self)
        self.size_entry.insert(0, "200")
        self.size_entry.pack(fill="x")  # align to left and fill horizontally
        self.color_label = tk.Label(self, text="Color:", anchor="w")
        self.color_label.pack(fill="x")  # align to left and fill horizontally
        self.color_entry = tk.Entry(self)
        self.color_entry.insert(0, "black")
        self.color_entry.pack(fill="x")  # align to left and fill horizontally
        self.error_label = tk.Label(self, fg="red")
        self.error_label.pack(fill="x")  # align to left and fill horizontally
        self.qr_label = tk.Label(self)




    def generate_qr(self):
        input_text = self.input_entry.get()
        if not input_text:
            self.error_label.config(text="Error: Input text is empty.")
            return
        try:
            size = int(self.size_entry.get())
            color = self.color_entry.get()
            qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(input_text)
            qr.make(fit=True)
            img = qr.make_image(fill_color=color, back_color="white")
            img = img.resize((size, size), Image.ANTIALIAS)
            self.qr_img = ImageTk.PhotoImage(img)
            self.qr_label = tk.Label(self, image=self.qr_img)
            self.qr_label.pack( padx=10, pady=5)
        except ValueError:
            self.error_label.config(text="Error: Size must be an integer.")
        except Exception as e:
            self.error_label.config(text="Error: " + str(e))

root = tk.Tk()
app = QRCodeGenerator(master=root)
app.mainloop()