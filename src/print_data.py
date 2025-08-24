import win32print

def print_text_file(filename, printer_name=None, feed_lines=5, cut=True):
    # If no printer specified, use default
    if not printer_name:
        printer_name = win32print.GetDefaultPrinter()
    print("Printing to:", printer_name)

    # Read the file as raw bytes
    with open(filename, "rb") as f:
        raw_data = f.read()

    # Append feed + cut commands if enabled
    if cut:
        # Feed paper out a bit (ESC d n → feed n lines)
        raw_data += b"\x1B\x64" + bytes([feed_lines])
        # Full cut (GS V 0)
        raw_data += b"\x1D\x56\x00"

    # Open printer
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Raw File Print", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)

        # Send file contents + cut commands to printer
        win32print.WritePrinter(hPrinter, raw_data)

        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)



