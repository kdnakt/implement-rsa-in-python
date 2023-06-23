#!/bin/sh

# Encrypt with RSA
echo -n "112233445566778899aabbccddeeff00" | \
  xxd -pr -r | \
  openssl rsautl -encrypt -raw -pubin -inkey pub.key | \
  hexdump -Cv

# Decrypt with RSA
echo -n "5e922f0e4c43903e9f5854385d40f8d2" | \
  xxd -pr -r | \
  openssl rsautl -decrypt -raw -inkey dummy.key | \
  hexdump -Cv
