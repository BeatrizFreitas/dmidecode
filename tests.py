import os

from dmidecode import parse_dmi


def test_bios():
    output = """
Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
	Vendor: Dell Inc.
	Version: A04
	Release Date: 09/11/2010
	Address: 0xF0000
	Runtime Size: 64 kB
	ROM Size: 8192 kB
	Characteristics:
		PCI is supported
		PNP is supported
		APM is supported
		BIOS is upgradeable
		BIOS shadowing is allowed
		ESCD support is available
		Boot from CD is supported
		Selectable boot is supported
		EDD is supported
		Japanese floppy for Toshiba 1.2 MB is supported (int 13h)
		3.5"/720 kB floppy services are supported (int 13h)
		Print screen service is supported (int 5h)
		8042 keyboard services are supported (int 9h)
		Serial services are supported (int 14h)
		Printer services are supported (int 17h)
		ACPI is supported
		USB legacy is supported
		BIOS boot specification is supported
		Function key-initiated network boot is supported
		Targeted content distribution is supported
	BIOS Revision: 0.0
"""
    assert parse_dmi(output)[0] == ('bios',  {
            '_title': "BIOS Information",
            "Vendor": "Dell Inc.",
            "Version": "A04",
            "Release Date": "09/11/2010",
            "Address": "0xF0000",
            "Runtime Size": "64 kB",
            "ROM Size": "8192 kB",
            "Characteristics": [
		"PCI is supported",
		"PNP is supported",
		"APM is supported",
		"BIOS is upgradeable",
		"BIOS shadowing is allowed",
		"ESCD support is available",
		"Boot from CD is supported",
		"Selectable boot is supported",
		"EDD is supported",
		"Japanese floppy for Toshiba 1.2 MB is supported (int 13h)",
		"3.5\"/720 kB floppy services are supported (int 13h)",
		"Print screen service is supported (int 5h)",
		"8042 keyboard services are supported (int 9h)",
		"Serial services are supported (int 14h)",
		"Printer services are supported (int 17h)",
		"ACPI is supported",
		"USB legacy is supported",
		"BIOS boot specification is supported",
		"Function key-initiated network boot is supported",
		"Targeted content distribution is supported",
                ],
            "BIOS Revision": "0.0",
            })


def test_system():
    output = """
Handle 0x0100, DMI type 1, 27 bytes
System Information
	Manufacturer: Dell Inc.
	Product Name: OptiPlex 980                 
	Version: Not Specified
	Serial Number: 35K213X
	UUID: 4C4C4544-0035-4B10-8032-B3C04F313358
	Wake-up Type: Power Switch
	SKU Number: Not Specified
	Family: Not Specified
"""
    assert parse_dmi(output)[0] == ('system', {
            "_title": "System Information",
            "Manufacturer": "Dell Inc.",
            "Product Name": "OptiPlex 980",
            "Version": "Not Specified",
            "Serial Number": "35K213X",
            "UUID": "4C4C4544-0035-4B10-8032-B3C04F313358",
            "Wake-up Type": "Power Switch",
            "SKU Number": "Not Specified",
            "Family": "Not Specified",
            })

def test_cpu_vm():
    output = """
Handle 0x0004, DMI type 4, 42 bytes
Processor Information
	Socket Designation: CPU #000
	Type: Central Processor
	Family: Unknown
	Manufacturer: GenuineIntel
	ID: F0 06 03 00 FF FB AB 1F
	Version: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
	Voltage: 3.3 V
	External Clock: Unknown
	Max Speed: 30000 MHz
	Current Speed: 2600 MHz
	Status: Populated, Enabled
	Upgrade: ZIF Socket
	L1 Cache Handle: 0x0018
	L2 Cache Handle: 0x001C
	L3 Cache Handle: Not Provided
	Serial Number: Not Specified
	Asset Tag: Not Specified
	Part Number: Not Specified
	Core Count: 4
	Core Enabled: 4
	Characteristics:
		64-bit capable
		Multi-Core
		Execute Protection
"""
    assert parse_dmi(output)[0] == ('processor',
 {'Asset Tag': 'Not Specified',
  'Characteristics': ['64-bit capable', 'Multi-Core', 'Execute Protection'],
  'Core Count': '4',
  'Core Enabled': '4',
  'Current Speed': '2600 MHz',
  'External Clock': 'Unknown',
  'Family': 'Unknown',
  'ID': 'F0 06 03 00 FF FB AB 1F',
  'L1 Cache Handle': '0x0018',
  'L2 Cache Handle': '0x001C',
  'L3 Cache Handle': 'Not Provided',
  'Manufacturer': 'GenuineIntel',
  'Max Speed': '30000 MHz',
  'Part Number': 'Not Specified',
  'Serial Number': 'Not Specified',
  'Socket Designation': 'CPU #000',
  'Status': 'Populated, Enabled',
  'Type': 'Central Processor',
  'Upgrade': 'ZIF Socket',
  'Version': 'Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz',
  'Voltage': '3.3 V',
  '_title': 'Processor Information'})
