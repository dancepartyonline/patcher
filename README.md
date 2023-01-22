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

------------

## VirusTotal Result:

- Windows (v2.0): https://www.virustotal.com/gui/file/66cb0abcab95626241ec48c6471408bf6a33fcc913e2ca0ab6d889094e9cd177 *(Some software detects it as a virus, but it is only a [python](https://github.com/Exorcism0666/patcher-without-python/blob/main/patcher.py) script turned into an executable with Pyinstaller directly compiled on [Github](https://github.com/Exorcism0666/patcher-without-python/actions/runs/3974282791/jobs/6813457347))*
- Ubuntu (v2.0): https://www.virustotal.com/gui/file/13721f565ea2506fa7d96956e97f70d28b81bc8b9841a2dd86897bbf9283baee
- MacOS (v2.0): https://www.virustotal.com/gui/file/170b679c98b0c5fff1cff7d1dd1271c77287f9504af9df22682053ceba37b287
- Python Program (From the original repo) (v2.0): https://www.virustotal.com/gui/file/e44f2473359db8f96585e5c1560d6380e8661a4c5dcf3d6023fb2fcbe011b8c6

If you need further help, you can join our [Discord server.](https://discord.gg/msKfjrqfCm)
----

Created by [Eliott](https://github.com/MZommer)
