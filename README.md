# maplestory-ip-hexedit
A simple python script to help change localhost ip to ip of your liking to target your server

## Requirements

- Python 3

## Usage 
Use -h on the script to generate help if required:
```
usage: change_ip.py [-h] [--output output_file] exe_file ip

Replace an IP address in an EXE file.

positional arguments:
  exe_file              Path to the EXE file to modify.
  ip                    New IP address to replace the old one (in standard IP format).

options:
  -h, --help            show this help message and exit
  --output output_file  Optional: Path to save the modified EXE (if not provided, the 
                        original EXE will be overwritten).
```

## Note
Your antivirus may flag the newly created exe as a threat, so do add that into exclusions or restore it.

I only tested it on the HeavenMS client from [Link](https://github.com/ronancpl/HeavenMS)