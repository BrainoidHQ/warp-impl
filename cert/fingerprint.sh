#!/bin/bash
set -euo pipefail

HOST="localhost"

cd "$(dirname "${BASH_SOURCE[0]}")"

openssl x509 -pubkey -noout -in "${HOST}.crt" |
	openssl rsa -pubin -outform der 2>/dev/null |
	openssl dgst -sha256 -binary |
	base64
