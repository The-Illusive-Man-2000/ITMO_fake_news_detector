### Сборка docker-образа
1. `cd /itmo_fake_news`
2. Создание образа: `sudo docker build -t itmo_fake_news:v0.1 itmo_fake_news/`
3. Запуск контейнера на основе подготовленного образа: `sudo docker run -it -d -p 8080:8080 itmo_fake_news:v0.1`
4. Остановка запущегого контейнера: `sudo docker container stop itmo_fake_news:v0.1`
5. Просмотр списка запущеных контейнеров: `sudo docker container ls`
6. Просмотр списка созданных образов: `sudo docker image ls`
7. Удаление созданного образа: `sudo docker image itmo_fake_news:v0.1`
8. Расположение файлов по умолчанию (нужны root-права):  
   ubuntu: `/var/lib/docker/voluems/`

### Deploy
1. Устанавливаем докер: см инструкцию под конкретную ОС
2. Выгрузка образа для преноса на другую машину: `sudo docker save -o ./itmo_fake_news_v0.1.tar itmo_fake_news:v0.1`
3. Копируем получившийся архив на целевую машину
4. Подгружаем скопированный образ: `docker load -i ./itmo_fake_news_v0.1.tar`
5. Запуск контейнера на основе подготовленного образа:  
`sudo docker run -itd -p :8080:8080 itmo_fake_news:v0.1`  
**EX:** `sudo docker run -itd -p 8080:8080 itmo_fake_news:v0.1`
6. Подключиться к контейнеру [см. attach](https://docs.docker.com/engine/reference/commandline/attach/):  
   `sudo docker contailer ls` - смотрим список запущеных контейнеров и выбираем ID нашего  
   `sudo docker attach ID(из предыдущей команды)` - возможность посмотреть что выводится в консоли докера (без истории)  
   `CTRL-p CTRL-q` - отключиться от консоли докера оставив его запущеным  

