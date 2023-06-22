from pgpy import PGPKey
from pgpy import PGPMessage


class EncryptFilePGP:
    def __init__(self, public_key_path, file_input_enc, file_output_enc, private_key_path, file_input_dec,
                 file_output_dec):
        self.public_key = None
        self.public_key_path = public_key_path
        self.private_key = None
        self.private_key_path = private_key_path
        self.file_input_enc = file_input_enc
        self.file_output_enc = file_output_enc
        self.file_input_dec = file_input_dec
        self.file_output_dec = file_output_dec
        self.load_message_enc = None
        self.load_message_dec = None
        self.message_encrypt = None
        self.message_decrypt = None

    def __load_public_key(self):
        self.public_key, _ = PGPKey.from_file(self.public_key_path)

    def __create_message(self):
        self.load_message_enc = PGPMessage.new(self.file_input_enc, file=True)

    def __encrypt_content(self):
        self.message_encrypt = self.public_key.encrypt(self.load_message_enc)

    def __write_file_encrypt(self):
        with open(self.file_output_enc, 'wb') as f:
            f.write(str(self.message_encrypt).encode('utf-8'))

    def encrypt_file(self):
        self.__load_public_key()
        self.__create_message()
        self.__encrypt_content()
        self.__write_file_encrypt()

    def __load_private_key(self):
        self.private_key, _ = PGPKey.from_file(self.private_key_path)

    def __read_message(self):
        self.load_message_dec = PGPMessage.from_file(self.file_input_dec)

    def __decrypt_content(self):
        self.message_decrypt = self.private_key.decrypt(self.load_message_dec).message

    def __write_file_decrypt(self):
        with open(self.file_output_dec, 'wb') as f:
            f.write(str(self.message_decrypt).encode('utf-8'))

    def decrypt_file(self):
        self.__load_private_key()
        self.__read_message()
        self.__decrypt_content()
        self.__write_file_decrypt()


pgp_enc = EncryptFilePGP('public_key.asc', 'file_input.txt', 'file_enc.pgp', 'private_key.asc', 'file_enc.pgp',
                         'file_dec.txt')
pgp_enc.encrypt_file()
pgp_enc.decrypt_file()
