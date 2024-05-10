import tkinter as tk
import ipaddress

def calculate_subnet():
    ip = ip_entry.get()
    subnet_mask = mask_entry.get()
    try:
        ip_obj = ipaddress.IPv4Address(ip)
        subnet_obj = ipaddress.IPv4Network(ip+'/'+subnet_mask, strict=False)

        # Determine the class
        ip_class = get_ip_class(ip_obj)

        # Get the subnet address
        subnet_address = str(subnet_obj.network_address)

        # Get binary representation of IP address and subnet mask
        binary_ip = get_binary_representation(ip_obj)
        binary_mask = get_binary_representation(ipaddress.IPv4Address(subnet_mask))
        binary_subnet = get_binary_representation(subnet_obj.network_address)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"IP Address Class: {ip_class}\n")
        result_text.insert(tk.END, f"Subnet Address: {subnet_address}\n")
        result_text.insert(tk.END, f"Binary IP Address: {binary_ip}\n")
        result_text.insert(tk.END, f"Binary Subnet Mask: {binary_mask}\n")
        result_text.insert(tk.END, f"Binary Subnet: {binary_subnet}\n")
    except (ipaddress.AddressValueError, ValueError):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid IP address or subnet mask")

def get_ip_class(ip_obj):
    first_octet = int(ip_obj) >> 24
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    else:
        return 'Unknown'

def get_binary_representation(ip_obj):
    return ".".join(format(int(octet), '08b') for octet in ip_obj.packed)

# Create the main window
root = tk.Tk()
root.title("IP Address and Subnet Mask Calculator")

# Create and pack widgets
ip_label = tk.Label(root, text="Enter IP Address:")
ip_label.grid(row=0, column=0, padx=5, pady=5)

ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

mask_label = tk.Label(root, text="Enter Subnet Mask:")
mask_label.grid(row=1, column=0, padx=5, pady=5)

mask_entry = tk.Entry(root)
mask_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_subnet)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

result_text = tk.Text(root, height=6, width=40)
result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
