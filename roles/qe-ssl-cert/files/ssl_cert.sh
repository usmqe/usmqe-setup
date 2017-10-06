#!/usr/bin/env bash
#
# ssl_cert.sh DEST_DIR CERT_NAME CERN_CN
#   DEST_DIR   - destination directory
#   CERT_NAME  - base of filename of the key and csr file (eg. server)
#   CERT_CN    - canonical name of the certificate for this key (default hostname)

# ###########################################################################
# mrg_ssl_create_key(CERT_NAME, CERN_CN)
#   CERT_NAME  - base of filename of the key and csr file (eg. server)
#   CERT_CN    - canonical name of the certificate for this key
#
#  Creates OpenSSL rsa keypair along wiht cert. signing request file (csr).
# ###########################################################################
function mrg_ssl_create_key() {
  local CERT_NAME=$1
  local CERT_CN=$2
  test -f /etc/cron.d/redhat-ddns && \
    local DDNS_NAME=$(head -1 /etc/cron.d/redhat-ddns | sed 's|.*name=\([-a-zA-Z0-9]*\)&.*|\1|').usersys.redhat.com
  host ${CERT_CN} && local IP=$(host ${CERT_CN} | sed 's|[-0-9a-zA-Z.]* has address \([0-9.]*\)|\1|')


  # Prepare openssl.cnf
  :> /tmp/openssl.cnf
  echo "[req]" >> /tmp/openssl.cnf
  echo "default_bits = 2048" >> /tmp/openssl.cnf
  echo "distinguished_name = req_distinguished_name" >> /tmp/openssl.cnf
  echo "req_extensions = v3_ca" >> /tmp/openssl.cnf
  echo "dirstring_type = nobmp" >> /tmp/openssl.cnf
  echo "" >> /tmp/openssl.cnf
  echo "[req_distinguished_name]" >> /tmp/openssl.cnf
  echo "emailAddress = root@localhost" >> /tmp/openssl.cnf
  echo "emailAddress_max = 40" >> /tmp/openssl.cnf
  echo "" >> /tmp/openssl.cnf
  echo "[v3_ca]" >> /tmp/openssl.cnf
  echo "basicConstraints = CA:FALSE" >> /tmp/openssl.cnf
  echo "keyUsage = nonRepudiation, digitalSignature, keyEncipherment" >> /tmp/openssl.cnf
  echo "subjectAltName = @alt_names" >> /tmp/openssl.cnf
  echo "" >> /tmp/openssl.cnf
  echo "[alt_names]" >> /tmp/openssl.cnf
  echo "DNS.1 = ${CERT_CN}" >> /tmp/openssl.cnf
  echo "DNS.2 = $(hostname -f)" >> /tmp/openssl.cnf
  [[ -n ${DDNS_NAME} ]] && echo "DNS.3 = ${DDNS_NAME}" >> /tmp/openssl.cnf
  [[ -n ${IP} ]] && echo "IP.1 = ${IP}" >> /tmp/openssl.cnf

  dd count=1 bs=4096 if=/dev/urandom of=/tmp/MRG_NOISE_FILE
  openssl genrsa -out ${CERT_NAME}.key 2048
  [ $? -ne 0 ] && err=$((${err} + 1))
  #echo -e ".\n.\n.\n.\n.\n${CERT_CN}\n.\n.\n.\n" \
  #| openssl req -new -nodes -key ${CERT_NAME}.key  -out ${CERT_NAME}.csr
  openssl req -new -nodes -key ${CERT_NAME}.key -out ${CERT_NAME}.csr -config /tmp/openssl.cnf \
    -subj "/C=CZ/ST=CZ/L=Brno/O=Red Hat/OU=USM - QE/CN=${CERT_CN}"
  [ $? -ne 0 ] && err=$((${err} + 1))
}

DEST_DIR="${1}"
CERT_NAME="${2:-server}"
CERT_CN="${3:-$(hostname)}"

[[ "${DEST_DIR}" ]] && pushd "${DEST_DIR}"
mrg_ssl_create_key "${CERT_NAME}" "${CERT_CN}"
[[ "${DEST_DIR}" ]] && popd

# request certificate
curl --data-binary @${DEST_DIR}/${CERT_NAME}.csr \
  http://usm-ssl-ca.usersys.redhat.com/mrg_openssl_ca/get_cert > ${DEST_DIR}/${CERT_NAME}.crt
