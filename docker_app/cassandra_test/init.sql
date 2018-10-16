CREATE KEYSPACE mnistkeyspace WITH REPLICATION = { 'class' : 'SimpleStrategy' , 'replication_factor' : 1 };

USE mnistkeyspace;

CREATE TABLE mnist_record(
	graph_value text,
	eval_value int,
	rcd_time timestamp,
	PRIMARY KEY((rcd_time), eval_value)
);

INSERT INTO mnist_record (graph_value, eval_value, rcd_time) VALUES ('0,0,0,0,1,0', 2, 140002827);