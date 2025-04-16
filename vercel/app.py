with open("output.assets", "wb") as outfile:
    for i in range(6):  # split0～split5
        with open(f"file.assets.split{i}", "rb") as infile:
            outfile.write(infile.read())
