<h2 align="center">Authorization-Stub</h2>

### Запуск

<details>
<summary>Docker (recommended)</summary>

```shell
docker run -d --name authorization-stub -p 5000:5000 ampetelin/authorization-stub:latest
```

</details>

<details>

<summary>systemd</summary>

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
sudo ln -s /opt/authorization-stub/authorization-stub.service /etc/systemd/system/
```
Запускаем службу
```shell
sudo systemctl start authorization-stub.service
sudo systemctl enable authorization-stub.service
```
</details>

