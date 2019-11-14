Drop table if exists feature_values;
Drop table if exists staedte_de;
Drop table  if exists staedte_de_tiny;
Drop table if exists features;

Create table staedte_de_tiny(
	id bigint auto_increment,
	stadt varchar(60),
	plz varchar(5),
	lng float, 
	lat float,
	Primary Key(id)
)ENGINE = INNODB;


Create table staedte_de(
	id bigint auto_increment,
	stadt varchar(60),
	plz varchar(5),
	bundesland varchar(60),
	landkreis varchar(60),
	lng float,
	lat float,
	Primary Key(id)
)ENGINE = INNODB;

Create table features(
	feature_id bigint auto_increment,
	name varchar(100),
	unit varchar(20),
	Primary Key(feature_id)
)ENGINE = INNODB;

Create table feature_values(
	city_id bigint,
	feature_id bigint, 
	f_value float,
	create_date date,
	Primary key(city_id, feature_id)
)ENGINE = INNODB;

ALTER TABLE feature_values ADD CONSTRAINT fk_feature_id 
FOREIGN KEY (feature_id) REFERENCES features(feature_id);

ALTER TABLE feature_values ADD CONSTRAINT fk_city_id 
FOREIGN KEY (city_id) REFERENCES staedte_de_tiny(id);