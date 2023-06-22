from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
from pgpy import PGPKey, PGPUID

# Generate new key
new_key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)

# Add uid for key user
uid = PGPUID.new('Arthur Davis <arthurdavis@example.com>')
new_key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
                ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
                compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP,
                             CompressionAlgorithm.Uncompressed])

# Generate  private and public key
private_key = new_key
public_key = new_key.pubkey

# Export keys
file_private_key = 'clave_privada.asc'
file_public_key = 'clave_publica.asc'

with open(file_private_key, 'wb') as file:
    file.write(str(private_key).encode('utf-8'))

with open(file_public_key, 'wb') as file:
    file.write(str(public_key).encode('utf-8'))
