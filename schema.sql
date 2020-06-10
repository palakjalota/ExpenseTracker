
drop table if exists expenseman;
           create table expenseman ((id INT AUTO_INCREMENT PRIMARY KEY,date date NOT NULL ,
		   category text NOT NULL,sub_category text NOT NULL,expense integer NOT NULL));

