import logging, shutil, os, tkinter as tk
from tkinter import filedialog
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def patch_exec(path, output):
    STRINGS = {
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

    STRINGS_JD5 = {
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
    
    STRINGS_JD15 = {
        # NAS #
        "https://naswii.nintendowifi.net/ac": "http://na-lgc.danceparty.online/ac",
        "https://naswii.nintendowifi.net/pr": "http://na-lgc.danceparty.online/pr",
        # Shop #
        "https://ecs.shop.wii.com/ecs/services/ECommerceSOAP": "http://shop-lgc.danceparty.online/ecs/ECommerceSOAP",
        # WS #
        "https://wii-dance6-ws1.ubisoft.com/wdfjd6/": "http://wii01-lgc.danceparty.online/wdf15/",
        "https://wii-dance6-ws1.ubisoft.com": "http://wii01-lgc.danceparty.online",
        
        "https://wii-dance6-ws2.ubisoft.com": "http://wii02-lgc.danceparty.online",
        "wii-dance6-ws1.ubisoft.com": "wii01-lgc.danceparty.online",
        "wii-dance6-ws2.ubisoft.com": "wii02-lgc.danceparty.online",
        "wdfjd6": "wdfjd15",
        # Tracking #
        "https://tracking-wii-dance.ubisoft.com": "http://trk-wii-dance.danceparty.online",
    }

    GAMES = 2018, 2017, 2016, 2015, 2014
    IDS = "SJOP41", "SJOE41", "SJME89"

    jdver = 9999
    
    with open(path, "rb") as main:
        main_dol = main.read()
    logging.info("DOL file loaded successfully.")

    logging.debug("Fetching the Just Dance version...")
    # Gets the jdver
    for game in GAMES:
        # Engine desc JD{game}_{platform}_LEGACY
        # JD5 (legacy) does not have this flag, so we check the Title Just Dance Just Dance® {game}
        if f"JD{game}".encode("ASCII") in main_dol or b"Just Dance\xAE " + str(game).encode("ASCII") in main_dol:
            jdver = game
            logging.debug(f"{jdver=}")
            break
    
    if jdver not in GAMES:
        return logging.error("Either the game is not supported, or you have a broken game dump.")
    
    # 2014 games and 2014 mods have the same DOL but different ID
    # and we can't detect ID from DOL so we check for boot.bin file
    if jdver == 2014:
        sys_path = os.path.dirname(path)
        boot_path = os.path.join(sys_path, "boot.bin")
        if not os.path.exists(sys_path) or not os.path.exists(boot_path):
            return logging.error("Are you sure you selected a DOL file that's located in DATA/sys? Can't find boot.bin file...")
        
        with open(boot_path, 'rb') as f:
            id = f.read(6).decode()
            if not id in IDS:
                return logging.error("Your 'main.dol' ID " + id + " is not available to patch.")
            if id == "SJME89":
                logging.info("JDJAPAN detected!")
                STRINGS_JD5["wiitracking"] = "jdjapantrkw"
                STRINGS_JD5["2399fff0497ae598539ccb3a61387f67833055ad"] = "a09302313bd087b88a54fe1a010eb62ea3edbfad"
                STRINGS_JD5["JejDUqq7"] = "DFe3qab8"

    # If version is 2014 replace STRINGS with JD5
    if jdver == 2014:
        STRINGS = STRINGS_JD5
    if jdver == 2015:
        STRINGS = STRINGS_JD15
    
    logging.debug("Patching DOL...")
    for key, value in STRINGS.items():
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
