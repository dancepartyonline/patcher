# DanceParty Patcher (Without Python)

This tool will help you patch your **main.dol** files (which contains contents of the original servers) and replace the original servers with DanceParty ones.

You don't need to install [Python 3](https://www.python.org/downloads/ "Python 3") to run this script.

After installing the `patcher.exe` file in the latest release of this repo, double click to run it and it will open up a GUI where you have to select the DOL file you extracted from your game.

------------

### What is a DOL file and where can I find it?

DOL files contain game's source code and by patching it with our tool it replaces old server URLs with ours which builds a connection between you and the servers.

### Services explanation
- NAS: Authentication server by Nintendo
- WS: Game servers
- Tracking: Used by the game to report bugs, issues and errors. It helps us improve the service, you can comment it out if you want to.
- ECS: Store server

------------

You can extract the DOL file by dumping the files of your **legally** owned game. You can find it in `DATA/sys` folder.
For Dolphin users; you need to dump the ENTIRE disc from the root on.

### Games supported

- [X] Just Dance 2014
- [X] Just Dance 2015
- [X] Just Dance 2016
- [X] Just Dance 2017
- [X] Just Dance 2018

Just Dance 2019 and 2020 don't have World Dance Floor.

### Mods supported

- [X] Just Dance Japan *(by Yunyl)*
- [X] Just Dance Beats *(by SquareJDBR)*

------------

## VirusTotal Result:

- Windows (v3.0): [Click here](https://www.virustotal.com/gui/file/5bae531a6946adfec071d267dc0637c43bb5f4bced4e6fd13c830a3f963b9239) *(Some software detects it as a virus, but it is only a [python](https://github.com/Exorcism0666/patcher-without-python/blob/main/patcher.py) script turned into an executable with Pyinstaller directly compiled on [Github](https://github.com/Exorcism0666/patcher-without-python/actions/runs/3993994779/jobs/6851212586))*
- Ubuntu (v3.0): [Click here](https://www.virustotal.com/gui/file/b7e1bff3059c14be8784d0e95ce57e58cdab51bf796c0789c606589a962f2bdd)
- MacOS (v3.0): [Click here](https://www.virustotal.com/gui/file/9219d48995054c2aa025b62e999722fa46d29c3f37da64bbb36e83f21489b1b2)
- Python Program (From the original repo) (v3.0): [Click here](https://www.virustotal.com/gui/file/6d04e0fdcecb62e7e10ccd1a052bb8714b923b6137a4f0740bc100aacb2fdd74)

If you need further help, you can join our [Discord server.](https://discord.gg/msKfjrqfCm)
----

Created by [Eliott](https://github.com/MZommer)
