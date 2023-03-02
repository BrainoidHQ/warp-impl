#!/bin/bash
set -euxo pipefail

echo "$(dirname "${BASH_SOURCE[0]}")"

cd "$(dirname "${BASH_SOURCE[0]}")"

# mkcert -cert-file localhost.crt -key-file localhost.key localhost 127.0.0.1 ::1
mkcert -cert-file certificate.pem -key-file certificate.key localhost 127.0.0.1 ::1
