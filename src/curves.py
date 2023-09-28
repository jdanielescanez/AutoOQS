
# https://openquantumsafe.org/liboqs/algorithms/kem/bike.html
# https://openquantumsafe.org/liboqs/algorithms/kem/kyber.html
# https://openquantumsafe.org/liboqs/algorithms/kem/frodokem.html
# https://openquantumsafe.org/liboqs/algorithms/kem/hqc.html

CURVES = [
    'bikel1', 'bikel3',
    'p256_bikel1', 'p384_bikel3',

    'kyber512', 'kyber768', 'kyber1024',
    'kyber90s512', 'kyber90s768', 'kyber90s1024',
    'p256_kyber512', 'p384_kyber768', 'p521_kyber1024',
    'p256_kyber90s512', 'p384_kyber90s768', 'p521_kyber90s1024',

    'frodo640aes', 'frodo640shake',
    'frodo976aes', 'frodo976shake',
    # 'frodo1344aes',
    'frodo1344shake',
    'p256_frodo640aes', 'p256_frodo640shake',
    'p384_frodo976aes', 'p384_frodo976shake',
    # 'p521_frodo1344aes', 
    'p521_frodo1344shake',

    'hqc128', 'hqc192',
    'p256_hqc128', 'p384_hqc192',
]
