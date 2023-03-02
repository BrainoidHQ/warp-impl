# Warp Impl
## Server
- Generate certificate stuff as TLS is required on QUIC Connection
```bash
#at the root dir
cd ./cert
mkcert -cert-file certificate.pem -key-file certificate.key localhost 127.0.0.1 ::1
openssl x509 -pubkey -noout -in "certificate.pem" |
	openssl rsa -pubin -outform der 2>/dev/null |
	openssl dgst -sha256 -binary |
	base64
```

- Start up
```bash
#at the root dir
python main.py ../cert/certificate.pem ../cert/certificate.key
```

## Client
```
#at the root dir
cd ./client
yarn install
yarn dev
```
