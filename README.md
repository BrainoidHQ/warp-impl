# Warp Impl
## Server
- Generate certificate stuff as TLS is required on QUIC Connection
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

## Client
```
#at the root dir
cd ./client
yarn install
yarn dev
```

## Run Chrome Canary
```
/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary --origin-to-force-quic-on=0.0.0.0:4443
```
