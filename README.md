# MOQT Impl
Implementation of [Media over QUIC Transport](https://datatracker.ietf.org/doc/draft-ietf-moq-transport/) Streaming Protocol.
## Server
- Generating TLS 1.3 Certificate is required on QUIC Connection
```bash
#at the root dir
cd ./cert
mkcert -ecdsa -cert-file certificate.pem -key-file certificate.key localhost 127.0.0.1 ::1 0.0.0.0
```

- Start up
```bash
#at the root dir
python ./server/main.py ./cert/certificate.pem ./cert/certificate.key
```

### Media over QUIC Transport
in ./server/moqt

Interface definition and Encoder/Decoder (not yet implemented) of draft-ietf-moq-transport-01 in Python

## Client
```bash
#at the root dir
cd ./client
yarn install
yarn dev
```

## Run Chrome Canary
```bash
/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary --origin-to-force-quic-on=0.0.0.0:4443
```
