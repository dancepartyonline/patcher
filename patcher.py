import logging, shutil, os, tkinter as tk
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

SERVERS_JD5 = {
    # NAS #
    "https://naswii.nintendowifi.net/ac": "http://na-lgc.danceparty.online/ac",
    "https://naswii.nintendowifi.net/pr": "http://na-lgc.danceparty.online/pr",
    # Shop #
    "https://ecs.shop.wii.com/ecs/services/ECommerceSOAP": "http://shop-lgc.danceparty.online/ecs/ECommerceSOAP",
    # WDF #
    "https://tracking-wii-dance.ubisoft.com/wdf/": "http://wii01-lgc.danceparty.online/wdf/",
    # Tracking #
    "https://tracking-wii-dance.ubisoft.com/": "http://trk-wii-dance.danceparty.online",
}

GAMES = 2018, 2017, 2016, 2015, 2014

def patch_exec(path, output):
    jdver = 9999
    
    with open(path, "rb") as main:
        main_dol = main.read()
    logging.info("DOL file loadded successfully.")

    logging.debug("Getting the Just Dance version")
    # Gets the jdver
    for game in GAMES:
        # Engine desc JD{game}_{platform}_LEGACY
        # JD5 (legacy) does not have this flag, so we check the Title Just Dance Just Dance® {game}
        if f"JD{game}".encode("ASCII") in main_dol or b"Just Dance\xAE " + str(game).encode("ASCII") in main_dol:
            jdver = game
            logging.debug(f"{jdver=}")
            break

    if jdver == 2015:
        return logging.error("Sorry, but Just Dance 2015 is not supported yet.")
    
    if jdver not in GAMES:
        return logging.error("Either the game is not supported, or you have a broken game dump.")

    # If version is 2014 replace servers with JD5
    if jdver == 2014:
        SERVERS = SERVERS_JD5
    
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
    print("DanceParty Patcher")
    root = tk.Tk()
    root.withdraw()
    dol_path = filedialog.askopenfilename( title = "Select the main.dol file", filetypes = ( ( "DOL Files", "*.dol" ), ( "all files","*.*" ) ) )
    if not os.path.exists(dol_path):
        logging.error("Please provide a correct path to your DOL file!")
        exit()
    
    shutil.copy(dol_path, dol_path.rstrip(".dol") + "_original.dol")
    patch_exec(dol_path, dol_path)
