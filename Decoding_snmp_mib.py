#!/usr/bin/python3
import sys

def hex_string_to_decimal(hex_string):
    return int(hex_string, 16)

def decode_snmp_message(message_hex):
    """
    Decode an SNMP message given in hexadecimal format.
    Returns a dictionary containing the Size of Message, Version, Community,
    PDU Type, Request ID, Error Status, and Error Index.
    """

    # Convert the hex string to bytes
    message = bytes.fromhex(message_hex)
    index = 0
    size_of_message = 0

    # Decode Size of Message
    if message[index] != 0x30:  # SEQUENCE
        return "The PDU message should start with 0x30 "
    index = 1
    if message[index] < 128:
        l = message[index]
        size_of_message = message[index] + 2
        index = 1
    else:
        l = message[index] - 128
        temp = l
        start_index = 2
        end_index = 2 + l
        while l != 0:
            l -= 1
            index += 1
            selected_values = [format(x, '02x') for x in message[start_index:end_index]]
            concatenated_hex = "".join(selected_values)
            decimal_result = hex_string_to_decimal(concatenated_hex)
        size_of_message = decimal_result + 2 + temp
   
    # Decode Version
    index += 1
    if message[index] != 0x02:  # INTEGER
        return "The version type must be integer"
    index += 1
    version_length = message[index]
    index += 1
    version = int.from_bytes(message[index:index + version_length], "big")
    index += version_length

    # Decode Community
    if message[index] != 0x04:  # OCTET STRING
        return "The community type must be octet string"
    index += 1
    community_length = message[index]
    index += 1
    community = message[index:index + community_length].decode()
    index += community_length

    # Decode PDU Type
    pdu_type = message[index]

    # Mapping PDU type to its name
    pdu_type_mapping = {
        0xA0: "Get Request",
        0xA1: "Get Next Request",
        0xA2: "Get Response",
        0xA3: "Set Request",
        0xA4: "Obsolete",
        0xA5: "Get Bulk Request",
        0xA6: "Inform Request",
        0xA7: "Trapv2",
        0xA8: "Report"
    }
    pdu_type_name = pdu_type_mapping.get(pdu_type, "Unknown")

    index += 1
    if message[index] < 128:
        index += 1
    else:
        l = message[index] - 128
        temp = l + 1
        index += temp

    # Decode Request ID
    if message[index] != 0x02:  # INTEGER
        return "The request ID type must be integer"
    index += 1
    request_id_length = message[index]
    index += 1
    request_id = int.from_bytes(message[index:index + request_id_length], "big")
    index += request_id_length

    # Decode Error Status
    if message[index] != 0x02:  # INTEGER
        return "Error status type must be in integer"
    index += 1
    error_status_length = message[index]
    index += 1
    error_status = int.from_bytes(message[index:index + error_status_length], "big")
    index += error_status_length

    # Decode Error Index
    if message[index] != 0x02:  # INTEGER
        return "Error index type must be in integer"
    index += 1
    error_index_length = message[index]
    index += 1
    error_index = int.from_bytes(message[index:index + error_index_length], "big")

    return {
        "Size of Message": size_of_message,
        "Version": version + 1,
        "Community": community,
        "PDU Type": pdu_type_name,
        "Request ID": request_id,
        "Error Status": error_status,
        "Error Index": error_index
    }

# Read the SNMP message from a file
def read_snmp_message_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().replace("\n", "").replace(" ", "")
    except IOError as e:
        return f"reading Error {e}"

# Main function to execute the script
# Main function to execute the script
# Main function to execute the script
def main():
    if len(sys.argv) != 2:
        print("The command format must be like this: python3 ./ID-140552.py msg.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    snmp_message_hex = read_snmp_message_from_file(file_path)

    if not snmp_message_hex.startswith("Error"):
        decoded_message = decode_snmp_message(snmp_message_hex)

        if isinstance(decoded_message, dict):
            print("Field           Value")
            print("--------------- -----------")
            for key, value in decoded_message.items():
                if key == "Size of Message":
                    print(f"{key:<15} {value} Bytes")
                else:
                    print(f"{key:<15} {value}")
        else:
            print(decoded_message)
    else:
        print(snmp_message_hex)

if __name__ == "__main__":
    main()
