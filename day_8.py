# Ceasar Cipher Code_1
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# new_word = ""

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

cipher_arr = []


def encrypt(text, shift):
  cipher_text = ""
  for letter in text:
    index_of = alphabet.index(letter) + shift
    if index_of > 25:
      index_of = index_of - 25
    else:
      new_letter = alphabet[index_of]
      cipher_arr.append(new_letter)
      cipher_text = "".join(cipher_arr)
  print(f"The encoded text is {cipher_text}")

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)

# Part 2 Ceasar Cipher
# Solution
def decrypt(text, shift):
  plain_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_post = position - shift
    plain_text += alphabet[new_post]
  print(f"Decoded text is {plain_text}")

# Part 3 : Clean up code
# Solution


def caesar(text, shift, direction):
  final_word = ""
  for letter in text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position + shift
      final_word += alphabet[new_position]
    if direction == "decode":
      new_position = position - shift
      final_word += alphabet[new_position]

  print(f"The result is {final_word}")


caesar(text, shift, direction)
