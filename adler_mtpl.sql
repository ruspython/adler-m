# ************************************************************
# Sequel Pro SQL dump
# Версия 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Адрес: 127.0.0.1 (MySQL 5.6.17)
# Схема: adler
# Время создания: 2014-10-29 21:35:13 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Дамп таблицы email_templates_emailtemplate
# ------------------------------------------------------------

DROP TABLE IF EXISTS `email_templates_emailtemplate`;

CREATE TABLE `email_templates_emailtemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `slug` varchar(128) NOT NULL,
  `recipients` varchar(512) NOT NULL,
  `subject` varchar(256) NOT NULL,
  `template` longtext NOT NULL,
  `description` longtext,
  `sender` varchar(256),
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `email_templates_emailtemplate` WRITE;
/*!40000 ALTER TABLE `email_templates_emailtemplate` DISABLE KEYS */;

INSERT INTO `email_templates_emailtemplate` (`id`, `name`, `slug`, `recipients`, `subject`, `template`, `description`, `sender`)
VALUES
	(1,'Сообщение со страницы «Контакты»','feedback','scriptosaur@gmail.com','Сообщение с сайта Adler-M','Сообщение в отдел {{ department }} города {{ city }}, отправлено в {{ add_time }}.\r\n\r\n{{ message }}\r\n\r\n--\r\n{{ name }}\r\n{{ contact }}','{{ department }} — подразделение\r\n{{ city }} — город\r\n{{ add_time }} — время создания\r\n{{ message }} — сообщение\r\n{{ name }} — имя\r\n{{ contact }} — телефон или email',''),
	(2,'Новый вопрос в FAQ','faq','scriptosaur@gmail.com','Новый вопрос в FAQ','{{ name }} задал вопрос:\r\n\r\n{{ question }}','{{ name }} — имя\r\n\r\n{{ question }} — вопрос',''),
	(3,'Новый заказ','new_order','nasty.pacman@yandex.ru','Новый заказ на сайте Adler-M','Сделан новый заказ.\r\n<br><br>\r\nПокупатель: {{ data.client_name }} {{ data.client_second_name }} {{ data.client_last_name }}<br>\r\nАдрес: {{ data.address_city }} {{ data.address_street }} {{ data.address_house }} {{ data.address_building }} {{ data.address_flat }} {{ data.address_zipcode }}<br>\r\nТелефон: {{ data.phone }}<br>\r\nE-mail: {{ data.email }}<br><br>\r\nСостав заказа:\r\n<table border=1 cellspacing=0 cellpadding=8>\r\n{% for item in data.orderitem_set.all %}\r\n<tr>\r\n<td>{{ item.name }}</td>\r\n<td>{{ item.price }}</td>\r\n<td>{{ item.quantity }}</td>\r\n<td>{{ item.get_total_price }}</td>\r\n</tr>\r\n{% endfor %}\r\n</table>','','');

/*!40000 ALTER TABLE `email_templates_emailtemplate` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
