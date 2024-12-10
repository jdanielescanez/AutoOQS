# Daniel Escanez-Exposito <jdanielescanez@gmail.com>
# Universidad de La Laguna - CryptULL
# Script para la automatización de las instalaciones necesarias para la ejecución del Entorno de pruebas de Open Quantum Safe

sudo apt-get -y update
sudo apt-get -y upgrade

# Wireshark
## Instalación
sudo apt -y install wireshark
## Debe añadirse el usuario que desee utilizar el programa al grupo Wireshark
sudo usermod -aG wireshark $USER

# Tshark
sudo apt-get install tshark

# Docker
## Instalación previa
sudo apt-get -y install ca-certificates curl gnupg lsb-release
## GPG oficial de Docker
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
## Configuración del repositorio
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Adición del repositorio
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update
# Instalación de la última versión de Docker Engine
sudo apt -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Open Quantum Safe - Liboqs
## Instalación previa
sudo apt -y install astyle cmake gcc git ninja-build libssl-dev python3-pytest python3-pytest-xdist unzip xsltproc doxygen graphviz python3-yaml

## Descarga del proyecto desde GitHub
cd /usr/local/
rm -rf liboqs
git clone --branch main https://github.com/open-quantum-safe/liboqs.git

## Instalación
cd liboqs
mkdir build && cd build
cmake -GNinja ..
sudo ninja

# Comandos de pull de los diferentes contenedores a utilizar
docker pull openquantumsafe/httpd
docker pull openquantumsafe/wireshark
docker pull openquantumsafe/curl
docker pull openquantumsafe/epiphany

# Crear red de docker
sudo docker network create httpd-test

# Access control disabled, clients can connect from any host
xhost +

# Eliminar paquetes innecesarios
sudo apt -y autoremove
