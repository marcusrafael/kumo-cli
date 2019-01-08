![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/kumo.png)
<h2 align="center">Kumo Command Line Interface</h2>

## Instalation

```bash
sudo apt update
```
```bash
sudo apt -y install python3-pip
```
```bash
sudo pip3 install virtualenv
```
```bash
virtualenv -p python3 ~/.venv/kumo
```
```bash
source ~/.venv/kumo/bin/activate
```
```bash
git clone https://github.com/marcusrafael/kumo-cli
```
```bash
cd kumo-cli
```
```bash
pip3 install -r requirements.txt
```
```bash
pip3 install . --upgrade
```
```bash
kumo configure
```

## Credentials

### Amazon Web Services

![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/amazon_1.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/amazon_2.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/amazon_3.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/amazon_4.png)

### Google Cloud Platform

![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_1.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_2.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_3.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_4.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_5.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_6.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_7.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_8.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_9.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_10.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_11.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_12.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/google_13.png)

### Microsoft Azure

```bash
pip install azure-cli
```
```bash
az login
```
```bash
az ad sp create-for-rbac --sdk-auth
```
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/microsoft_1.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/microsoft_2.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/microsoft_3.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/microsoft_4.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/microsoft_5.png)
![kumo](https://github.com/marcusrafael/kumo-cli/blob/master/images/microsoft_6.png)

## Configuration

```bash
vim ~/.kumo/kumo.conf
```
```properties
[kumo]
url = http://localhost:5000

[red]
cloud = amazon
bucket =
region =
availability_zone =
instance_type =
aws_access_key_id =
aws_secret_access_key =

[blue]
cloud = amazon
bucket =
region =
availability_zone =
instance_type =
aws_access_key_id =
aws_secret_access_key =

[white]
cloud = google
bucket =
zone =
system =
machine_type =
type =
project_id =
private_key_id =
client_email =
client_id =
auth_uri =
token_uri =
auth_provider_x509_cert_url =
client_x509_cert_url =
private_key =

[black]
cloud = google
bucket =
zone =
system =
machine_type =
type =
project_id =
private_key_id =
client_email =
client_id =
auth_uri =
token_uri =
auth_provider_x509_cert_url =
client_x509_cert_url =
private_key =

[green]
cloud = microsoft
container =
location =
zones =
virtual_machine_size =
network =
subnet =
resource_group_name =
client_id =
client_secret =
subscription_id =
tenant_id =
active_directory_endpoint_url =
resource_manager_endpoint_url =
active_directory_graph_resource_id =
sql_management_endpoint_url =
gallery_endpoint_url =
management_endpoint_url =
storage_account_name =
storage_account_key =

[yellow]
cloud = microsoft
container =
location =
zones =
virtual_machine_size =
resource_group_name =
client_id =
client_secret =
subscription_id =
tenant_id =
active_directory_endpoint_url =
resource_manager_endpoint_url =
active_directory_graph_resource_id =
sql_management_endpoint_url =
gallery_endpoint_url =
management_endpoint_url =
storage_account_name =
storage_account_key =
```

## Usage

```bash
vim templates/template.yaml
```

```yaml
---
migration:
  source_account: <source_account>
  destination_account: <destination_account>
  virtual_machine: <virtual_machine>
```

```bash
kumo migrate templates/template.yaml
```

## Kernel update

```bash
ssh ubuntu@instance
```
```bash
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15/linux-headers-4.15.0-041500_4.15.0-041500.201802011154_all.deb
```
```bash
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15/linux-headers-4.15.0-041500-generic_4.15.0-041500.201802011154_amd64.deb
```
```bash
wget https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15/linux-image-4.15.0-041500-generic_4.15.0-041500.201802011154_amd64.deb
```
```bash
sudo dpkg -i *.deb
```
```bash
sudo dpkg -l | grep linux-image
```
```bash
sudo apt purge linux-image-
```
```bash
sudo update-grub
```
