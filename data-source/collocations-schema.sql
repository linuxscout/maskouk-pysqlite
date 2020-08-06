CREATE TABLE "collocations" (
	"id" INTEGER PRIMARY KEY  NOT NULL , 
	"vocalized" VARCHAR,
	"unvocalized" VARCHAR,
	"rule" VARCHAR, 
	"category" VARCHAR, 
	"note" VARCHAR,
	"first" VARCHAR,
	"second" VARCHAR
	);
CREATE INDEX "unv_index" on collocations (vocalized ASC);
CREATE INDEX "first_indx" on collocations (first ASC, second ASC);
CREATE INDEX "secindx" on collocations (second ASC);
CREATE INDEX "one2idx" on collocations (first ASC, second ASC);
