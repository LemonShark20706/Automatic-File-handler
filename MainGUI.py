import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("File handler GUI")
        self.geometry("800x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ===== HEADER =====
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#1a1a1a")
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.header_frame.grid_columnconfigure(0, weight=1)

        self.header_label = ctk.CTkLabel(
            self.header_frame,
            text="File Handler Application",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.header_label.grid(row=0, column=0, padx=20, pady=10)

        # ===== SIDEBAR =====
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#1a1a1a")
        self.sidebar_frame.grid(row=1, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.sidebar_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="Menu",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.sidebar_label.grid(row=0, column=0, padx=20, pady=(20,10))

        # Sidebar buttons
        self.button1 = ctk.CTkButton(self.sidebar_frame, text="Dashboard", command=self.show_dashboard)
        self.button1.grid(row=1, column=0, padx=20, pady=10)

        self.button2 = ctk.CTkButton(self.sidebar_frame, text="Settings", command=self.show_settings)
        self.button2.grid(row=2, column=0, padx=20, pady=10)

        self.button3 = ctk.CTkButton(self.sidebar_frame, text="Exit", command=self.quit)
        self.button3.grid(row=3, column=0, padx=20, pady=10)

        # ===== MAIN CONTENT =====
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.main_label = ctk.CTkLabel(
            self.main_frame,
            text="Welcome to the main content area!",
            font=ctk.CTkFont(size=16)
        )
        self.main_label.grid(row=0, column=0, padx=20, pady=20)

    # ===== Button actions =====
    def show_dashboard(self):
        self.main_label.configure(text="Dashboard view loaded.")

    def show_settings(self):
        self.main_label.configure(text="Settings view loaded.")

app = App()
app.mainloop()
