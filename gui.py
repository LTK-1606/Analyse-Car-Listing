import os
import customtkinter as ctk
import main  # Import main.py

# Rest of your GUI code goes here

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("350x720")

# Get the current working directory
working_directory = os.getcwd()

def run_main_function():
    main.main(working_directory)  # Call the function from main.py
    print("Analysis started")
    
def run_scraper():
    motorist_urls = [motorist_entry1.get(), motorist_entry2.get(), motorist_entry3.get(), motorist_entry4.get()]
    sgcar_urls = [sgcar_entry1.get(), sgcar_entry2.get(), sgcar_entry3.get(), sgcar_entry4.get()]

    # Ensure that at least one URL is provided before writing to the file
    if any(motorist_urls) or any(sgcar_urls):
        with open(os.path.join(working_directory, "urls.txt"), "w") as file:
            file.write("\n".join(motorist_urls + sgcar_urls))
        print("URLs written to urls.txt successfully")
    else:
        print("No URLs provided. URLs.txt will not be created.")

def run_scraper_and_main():
    run_scraper()  # Run the scraper function first
    run_main_function()  # Then run the main function


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Car Listings Analysis", font=("Roboto", 24))
label.grid(row=0, column=0, columnspan=2, pady=12, padx=10)

motorist_label = ctk.CTkLabel(master=frame, text="Motorist URLs", font=("Roboto", 16))
motorist_label.grid(row=1, column=0, columnspan=2, pady=12, padx=10)

motorist_entry1 = ctk.CTkEntry(master=frame, placeholder_text="Motorist URL 1")
motorist_entry1.grid(row=2, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

motorist_entry2 = ctk.CTkEntry(master=frame, placeholder_text="Motorist URL 2")
motorist_entry2.grid(row=3, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

motorist_entry3 = ctk.CTkEntry(master=frame, placeholder_text="Motorist URL 3")
motorist_entry3.grid(row=4, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

motorist_entry4 = ctk.CTkEntry(master=frame, placeholder_text="Motorist URL 4")
motorist_entry4.grid(row=5, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

sgcar_label = ctk.CTkLabel(master=frame, text="SG Car Mart URLs", font=("Roboto", 16))
sgcar_label.grid(row=6, column=0, columnspan=2, pady=12, padx=10)

sgcar_entry1 = ctk.CTkEntry(master=frame, placeholder_text="SG Car Mart URL 1")
sgcar_entry1.grid(row=7, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

sgcar_entry2 = ctk.CTkEntry(master=frame, placeholder_text="SG Car Mart URL 2")
sgcar_entry2.grid(row=8, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

sgcar_entry3 = ctk.CTkEntry(master=frame, placeholder_text="SG Car Mart URL 3")
sgcar_entry3.grid(row=9, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

sgcar_entry4 = ctk.CTkEntry(master=frame, placeholder_text="SG Car Mart URL 4")
sgcar_entry4.grid(row=10, column=0, columnspan=2, pady=12, padx=10, sticky="ew")

button = ctk.CTkButton(master=frame, text="Run Analysis", command=run_scraper_and_main)
button.grid(row=11, column=0, columnspan=2, pady=12, padx=10)


root.mainloop()
