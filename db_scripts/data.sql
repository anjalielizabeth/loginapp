CREATE TABLE IF NOT EXISTS `users` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`firstname` varchar(50) NOT NULL,
    `lastname` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    `phone` int(12) NOT NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO `users` (`id`, `firstname`,`lastname`, `password`, `email`,`phone`) VALUES (1, 'anjali', 'elizabeth', 'anjali','anjali@test.com','74569');
CREATE TABLE IF NOT EXISTS `categories` (
	`categoryid` int(11) NOT NULL AUTO_INCREMENT,
  	`name` varchar(50) NOT NULL,
    `description` varchar(50) NOT NULL,
    PRIMARY KEY (`categoryid`)
    
);

INSERT INTO `categories` (`categoryid`, `name`,`description`) VALUES (1, 'category1', 'category 1 description');
