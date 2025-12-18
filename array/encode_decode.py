"""
Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        Args:
            strs: List of strings to encode

        Returns:
            A single encoded string containing all input strings
        """
        encoded_parts = []

        # For each string, prepend its length as a 4-character fixed-width field
        for string in strs:
            # Format length as 4 digits with leading spaces if needed
            length_prefix = f"{len(string):4}"
            # Append length prefix followed by the actual string
            encoded_parts.append(length_prefix + string)

        # Join all encoded parts into a single string
        return "".join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.

        Args:
            s: The encoded string to decode

        Returns:
            List of decoded strings
        """
        decoded_strings = []
        index = 0
        total_length = len(s)

        # Process the encoded string by reading length prefixes and extracting strings
        while index < total_length:
            # Read the 4-character length prefix
            string_length = int(s[index:index + 4])
            index += 4

            # Extract the string of the specified length
            decoded_string = s[index:index + string_length]
            decoded_strings.append(decoded_string)
            index += string_length

        return decoded_strings


if __name__ == '__main__':
    codec = Codec()

    inp = ["we", "say", ":", "yes"]
    encode_string = codec.encode(inp)
    decoded_string = codec.decode(encode_string)
    print(encode_string, decoded_string)