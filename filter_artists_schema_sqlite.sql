-- ---------------------------------------------------------------------------
-- ---------------------------------------------------------------------------
-- script :        schema.sql
-- database:       artist
-- contributors :  Gabor Maksay (gmy)
-- history :       when       | ver | who | what
--                 2023-01-18 | 1.1 | gmy | unified schema & data
--                 2022-08-09 | 1.0 | gmy | creation for sqlite

-- ---------------------------------------------------------------------------
-- ------------------------------------------------------------------ removal

DROP TABLE IF EXISTS artist;

-- ---------------------------------------------------------------------------
-- ------------------------------------------------------------------- tables

CREATE TABLE artist (
	id			INTEGER NOT NULL,
	stage_name	TEXT NOT NULL,
	start_date	TEXT NOT NULL,
	type_of		TEXT NOT NULL,
	last_name	TEXT,
	first_name	TEXT,
	birth_date	TEXT,
	PRIMARY KEY	(id)
);

-- ---------------------------------------------------------------------------
-- --------------------------------------------------------------------- data

DELETE FROM artist;

INSERT INTO artist (id, stage_name, start_date, type_of, last_name, first_name, birth_date) VALUES
	( 1, 'Beatles',         '1960-06-01', 'group',  '-',          '-',               '1960-06-01'),
	( 2, 'Paul Mc Cartney', '1957-07-06', 'single', 'Mc Cartney', 'Paul',             '1942-06-18'),
	( 3, 'John Lennon',     '1957-07-06', 'single', 'Lennon',     'John Winston',     '1940-10-09'),
	( 4, 'George Harrison', '1958-02-01', 'single', 'Harrison',   'George',           '1943-02-25'),
	( 5, 'Ringo Starr',     '1959-01-01', 'single', 'Starkey',    'Richard',          '1940-07-07'),
	( 6, 'Supertramp',      '1969-01-01', 'group',  '-',           '-',               '1969-01-01'),
	( 7, 'Rick Davies',     '1956-01-01', 'single', 'Davies',     'Richard',          '1944-07-22'),
	( 8, 'Rodger Hodgson',  '1967-01-01', 'single', 'Hodgson',    'Charles Roger',    '1950-03-21'),
	( 9, 'John Helliwell',  '1970-01-01', 'single', 'Helliwell',  'John',             '1945-02-15'),
	(10, 'Dougie Thomson',  '1971-09-01', 'single', 'Campbell',   'Douglas',          '1951-03-24'),
	(11, 'Bob C. Benberg',  '1970-01-01', 'single', 'Siebengerg', 'Bob',              '1949-10-31'),
	(12, 'Elton John',      '1970-01-01', 'single', 'Dwight',     'Reginald Kenneth', '1947-03-25'),
	(13, 'Bernie Taupin',   '1970-01-01', 'other',  'Taupin',     'Bernard John',     '1950-05-22'),
	(14, 'Peter Townshend', '1970-01-01', 'other',  'Taupin',     'Bernard John',     '1950-05-22');