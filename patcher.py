import os
import logging, tkinter as tk, shutil
from tkinter import filedialog
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

SERVERS = {
    # NAS #
    "https://naswii.nintendowifi.net/ac": "http://na-lgc.danceparty.online/ac",
    "https://naswii.nintendowifi.net/pr": "http://na-lgc.danceparty.online/pr",
    # Shop #
    "https://ecs.shop.wii.com/ecs/services/ECommerceSOAP": "http://shop-lgc.danceparty.online/ecs/ECommerceSOAP",
    # WS #
    "https://wii-dance6-ws1.ubisoft.com": "http://wii01-lgc.danceparty.online",
    "https://wii-dance6-ws2.ubisoft.com": "http://wii02-lgc.danceparty.online",
    "wii-dance6-ws1.ubisoft.com": "wii01-lgc.danceparty.online",
    "wii-dance6-ws2.ubisoft.com": "wii02-lgc.danceparty.online",
    # Tracking #
    "https://tracking-wii-dance.ubisoft.com": "http://trk-wii-dance.danceparty.online",
}

GAMES = 2018, 2017, 2016#, 2015, 2014

def patch_exec(path, output):
    jdver = 9999
    
    with open(path, "rb") as main:
        main_dol = main.read()
    print("DanceParty Patcher")
    logging.info("DOL file loadded successfully.")

    logging.debug("Getting the Just Dance version")
    # Gets the jdver
    for game in GAMES:
        # Engine desc JD{game}_{platform}_LEGACY
        if f"JD{game}".encode("ASCII") in main_dol:
            jdver = game
            logging.debug(f"{jdver=}")
            break
    
    if jdver not in GAMES:
        return logging.error("Game not supported!")
    
    logging.debug("Patching DOL...")
    for key, value in SERVERS.items():
        key_len, value_len = len(key), len(value)
        key, value = key.encode("ASCII"), value.encode("ASCII")
        if key_len < value_len:
            # logging.warning(f"String to replace is longer than expected")
            key += b"\x00" * (value_len - key_len)
        elif key_len > value_len:
            value += b"\x00" * (key_len - value_len)
         
        main_dol = main_dol.replace(key, value)
        logging.debug(f"Replaced {key} by {value}")
    logging.info("DOL file was patched successfully.")
    logging.info("You can now enjoy DanceParty!")

    with open(output, "wb") as main:
        main.write(main_dol)


    

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    dol_path = filedialog.askopenfilename( title = "Select the main.dol file", filetypes = ( ( "DOL Files", "*.dol" ), ( "all files","*.*" ) ) )
    
    path_exists = os.path.exists(dol_path)
    if not path_exists:
        logging.error("Please provide a correct path to your DOL file!")
        exit()
    
    shutil.copy(dol_path, dol_path.rstrip(".dol") + "_original.dol")
    patch_exec(dol_path, dol_path)
