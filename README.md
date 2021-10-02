# docker-with-ansible
Напишите ansible playbook, который бы запускал на локальной машине docker контейнер с ssh, устанавливал туда nginx, поднимал сайт из одной странички, куда выводил бы количество ядер CPU, памяти и дискового пространства в этом контейнере

#### Notice: замените ip в inventory

```git clone git@github.com:AnastasiyaGapochkina01/system-docker-info.git```

```cd system-docker-info && ansible-playbook -i inventory main.yaml```