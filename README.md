<h2 align="center">Authorization-Stub</h2>

### Установка

Клонируем репозиторий
```shell
sudo git clone https://github.com/ampetelin/authorization-stub.git /opt/authorization-stub/
```
Создаем виртуальное окружение
```shell
sudo python3 -m venv /opt/authorization-stub/venv
```
Устанавливаем зависимости
```shell
sudo /opt/authorization-stub/venv/bin/pip install -r /opt/authorization-stub/requirements.txt
```
Создаем ссылку на службу
```shell
sudo ln -s /opt/authorization-stub/authorization_stub.service /etc/systemd/system/
```
Запускаем службу
```shell
sudo systemctl start authorization_stub.service
sudo systemctl enable authorization_stub.service
```