import tkinter as tk
from tkinter import filedialog
import configparser

def determine_ai(model):
    if "traffic_" in model:
        return "fixed"
    else:
        return "none"

def process_input(input_file):
    config = configparser.ConfigParser(allow_no_value=True)
    config.optionxform = str  # Preserve the case sensitivity of keys
    config.read(input_file)

    output = []
    for section in config.sections():
        model = config[section]['MODEL']
        ai = determine_ai(model)
        config[section]['AI'] = ai
        if ai == 'fixed':
            config[section]['SKIN'] = ''

        output.append(f"[{section}]\n")
        for key, value in config[section].items():
            output.append(f"{key}={value}\n")
        output.append('\n')

    return output

def save_file(output_file, config):
    with open(output_file, 'w') as configfile:
        config.write(configfile)

def select_input_file():
    input_file = filedialog.askopenfilename(filetypes=[("INI files", "*.ini")])  # Filter for .ini files
    if input_file:
        input_label.config(text=f"Input File: {input_file}")
        root.input_file = input_file

def select_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".ini", filetypes=[("INI files", "*.ini")])  # Filter for .ini files
    if output_file:
        output_label.config(text=f"Output File: {output_file}")
        root.output_file = output_file

def save_file():
    if hasattr(root, 'input_file') and hasattr(root, 'output_file'):
        output = process_input(root.input_file)
        with open(root.output_file, 'w') as file:
            file.writelines(output)
        status_label.config(text="File saved successfully.")
    else:
        status_label.config(text="Please select input and output files.")

root = tk.Tk()
root.title("Car Configuration Modifier")

select_input_button = tk.Button(root, text="Select Input File", command=select_input_file)
select_input_button.pack()

select_output_button = tk.Button(root, text="Select Output File", command=select_output_file)
select_output_button.pack()

save_button = tk.Button(root, text="Save Modified File", command=save_file)
save_button.pack()

input_label = tk.Label(root, text="")
input_label.pack()

output_label = tk.Label(root, text="")
output_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.protocol("WM_DELETE_WINDOW")
root.mainloop()


# Inside the save_file function where you call process_input function:
def save_file():
    if hasattr(root, 'input_file') and hasattr(root, 'output_file'):
        config = process_input(root.input_file)
        save_file(root.output_file, config)
        status_label.config(text="File saved successfully.")
    else:
        status_label.config(text="Please select input and output files.")
