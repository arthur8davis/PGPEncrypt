from pgpy import PGPKey
from pgpy import PGPMessage


class EncryptFilePGP:
    def __init__(self, public_key_path, file_input_enc, file_output_enc, ):
        self.public_key = None
        self.public_key_path = public_key_path
        self.private_key = None
        self.file_input_enc = file_input_enc
        self.file_output_enc = file_output_enc
        self.load_message_enc = None
        self.message_encrypt = None

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


pgp_enc = EncryptFilePGP('public_key.pub', 'file_input', 'file_enc.pgp')
pgp_enc.encrypt_file()
