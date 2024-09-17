-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema univ
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `univ` ;

-- -----------------------------------------------------
-- Schema univ
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `univ` DEFAULT CHARACTER SET utf8 ;
USE `univ` ;

-- -----------------------------------------------------
-- Table `univ`.`college`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`college` ;

CREATE TABLE IF NOT EXISTS `univ`.`college` (
  `idcollege` INT NOT NULL,
  `college_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcollege`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `univ`.`departament`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`departament` ;

CREATE TABLE IF NOT EXISTS `univ`.`departament` (
  `iddepartament` INT NOT NULL,
  `departament_name` VARCHAR(45) NOT NULL,
  `departament_code` VARCHAR(10) NOT NULL,
  `idcollege` INT NOT NULL,
  PRIMARY KEY (`iddepartament`, `idcollege`),
  INDEX `fk_departament_college_idx` (`idcollege` ASC) VISIBLE,
  CONSTRAINT `fk_departament_college`
    FOREIGN KEY (`idcollege`)
    REFERENCES `univ`.`college` (`idcollege`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `univ`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`course` ;

CREATE TABLE IF NOT EXISTS `univ`.`course` (
  `idcourse` INT NOT NULL,
  `course_num` INT NOT NULL,
  `course_title` VARCHAR(45) NOT NULL,
  `course_credit` INT NOT NULL,
  `iddepartament` INT NOT NULL,
  `idcollege` INT NOT NULL,
  PRIMARY KEY (`idcourse`, `iddepartament`, `idcollege`),
  INDEX `fk_course_departament1_idx` (`iddepartament` ASC, `idcollege` ASC) VISIBLE,
  CONSTRAINT `fk_course_departament1`
    FOREIGN KEY (`iddepartament` , `idcollege`)
    REFERENCES `univ`.`departament` (`iddepartament` , `idcollege`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `univ`.`faculty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`faculty` ;

CREATE TABLE IF NOT EXISTS `univ`.`faculty` (
  `idfaculty` INT NOT NULL,
  `faculty_fname` VARCHAR(45) NOT NULL,
  `faculty_lname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idfaculty`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `univ`.`term`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`term` ;

CREATE TABLE IF NOT EXISTS `univ`.`term` (
  `idterm` INT NOT NULL,
  `term_name` VARCHAR(8) NOT NULL,
  `term_year` YEAR NOT NULL,
  PRIMARY KEY (`idterm`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `univ`.`section`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`section` ;

CREATE TABLE IF NOT EXISTS `univ`.`section` (
  `idsection` INT NOT NULL,
  `section_capacity` VARCHAR(45) NOT NULL,
  `section_num` VARCHAR(45) NOT NULL,
  `idcourse` INT NOT NULL,
  `iddepartament` INT NOT NULL,
  `idcollege` INT NOT NULL,
  `idterm` INT NOT NULL,
  `idfaculty` INT NOT NULL,
  PRIMARY KEY (`idsection`, `idcourse`, `iddepartament`, `idcollege`, `idterm`, `idfaculty`),
  INDEX `fk_section_course1_idx` (`idcourse` ASC, `iddepartament` ASC, `idcollege` ASC) VISIBLE,
  INDEX `fk_section_term1_idx` (`idterm` ASC) VISIBLE,
  INDEX `fk_section_faculty1_idx` (`idfaculty` ASC) VISIBLE,
  CONSTRAINT `fk_section_course1`
    FOREIGN KEY (`idcourse` , `iddepartament` , `idcollege`)
    REFERENCES `univ`.`course` (`idcourse` , `iddepartament` , `idcollege`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_term1`
    FOREIGN KEY (`idterm`)
    REFERENCES `univ`.`term` (`idterm`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_faculty1`
    FOREIGN KEY (`idfaculty`)
    REFERENCES `univ`.`faculty` (`idfaculty`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `univ`.`student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`student` ;

CREATE TABLE IF NOT EXISTS `univ`.`student` (
  `idstudent` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gender` ENUM("M", "F") NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(2) NOT NULL,
  `birthdate` DATE NULL,
  PRIMARY KEY (`idstudent`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `univ`.`enrollement`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `univ`.`enrollement` ;

CREATE TABLE IF NOT EXISTS `univ`.`enrollement` (
  `idstudent` INT NOT NULL,
  `idsection` INT NOT NULL,
  `idcourse` INT NOT NULL,
  `iddepartament` INT NOT NULL,
  `idcollege` INT NOT NULL,
  PRIMARY KEY (`idstudent`, `idsection`, `idcourse`, `iddepartament`, `idcollege`),
  INDEX `fk_enrollement_section1_idx` (`idsection` ASC, `idcourse` ASC, `iddepartament` ASC, `idcollege` ASC) VISIBLE,
  CONSTRAINT `fk_enrollement_student1`
    FOREIGN KEY (`idstudent`)
    REFERENCES `univ`.`student` (`idstudent`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_enrollement_section1`
    FOREIGN KEY (`idsection` , `idcourse` , `iddepartament` , `idcollege`)
    REFERENCES `univ`.`section` (`idsection` , `idcourse` , `iddepartament` , `idcollege`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- Queryes

-- college table
INSERT INTO college VALUES
	(1, "College of Physical Science and Engineering"),
    (2, "College of Business and Communication"),
    (3, "College of Language and Letters");


-- departament table
INSERT INTO departament VALUES
	(1, "Computer Information Technology", "CIT", 1),
    (2, "Economics", "ECON", 2),
    (3, "Humanities and Philosophy", "HUM", 3);

-- couse table
INSERT INTO course VALUES
	(1, 111, "Intro to Databases", 3, 1, 1),
    (2, 388, "Econometrics", 4, 2, 2),
    (3, 150, "Micro Economics", 3, 2, 2),
    (4, 376, "Classical Heritage", 2, 3, 3);

-- faculty table
INSERT INTO faculty VALUES
	(1, 'Marty', "Morning"),
    (2, 'Nate', 'Norris'),
    (3, 'Ben', 'Barrus'),
    (4, 'John', 'Jensen'),
    (5, 'Bill', 'Barney');
    
-- Term table
INSERT INTO term VALUES
	(1, "Fall", 2019),
    (2, "Winter", 2018);
    
-- Student Table
INSERT INTO student VALUES
	(1, "Paul",	"Miller", "M",	"Dallas",	"TX",	'1996-02-22'),
	(2, 'Katie',	'Smith',	'F',	'Provo',	'UT',	'1995-07-22'),
	(3, 'Kelly',	'Jones',	'F',	'Provo',	'UT',	'1998-06-22'),
	(4, 'Devon',	'Merrill',	'M',	'Mesa',	'AZ',	'2000-07-22'),
	(5, 'Mandy',	'Murdock',	'F',	'Topeka',	'KS',	'1996-11-22'),
	(6, 'Alece',	'Adams',	'F',	'Rigby',	'ID',	'1997-05-22'),
	(7, 'Bryce',	'Carlson',	'M',	'Bozeman',	'MT',	'1997-11-22'),
	(8, 'Preston',	'Larsen',	'M',	'Decatur',	'TN',	'1996-09-22'),
	(9, 'Julia',	'Madsen',	'F',	'Rexburg',	'ID',	'1998-09-22'),
	(10, 'Susan',	'Sorensen',	'F',	'Mesa',	'AZ',	'1998-08-09');
    
-- Section Table 
INSERT INTO section VALUES
	(1, 30, 1, 1, 1, 1, 1, 1), -- PK, CAP, SECTION 1,  111, CTI X, FALL 2019
    (2, 50, 1, 3, 2, 2, 1, 2), -- PK, CAP, SECTION 1, 150, ECON X, FALL 2019
    (3, 50, 2, 3, 2, 2, 1, 2), -- PK, CAP, SECTION 2, 150, ECON X, FALL 2019
    (4, 35, 1, 2, 2, 2, 1, 3), -- PK, CAP, SECTION 1, 388, ECON X, FALL 2019
    (5, 30, 1, 4, 3, 3, 1, 4), -- PK, CAP, SECTION 1, 376, HUM X, FALL 2019
    (6, 30, 2, 1, 1, 1, 2, 1), -- PK, CAP, SECTION 2, 111, CTI X, WINTER 2018
    (7, 35, 3, 1, 1, 1, 2, 5), -- PK, CAP, SECTION 3, 111, CTI X, WINTER 2018
    (8, 50, 1, 3, 2, 2, 2, 2), -- PK, CAP, SECTION 1, 150, ECON X, WINTER 2018
    (9, 50, 2, 3, 2, 2, 2, 2), -- PK, CAP, SECTION 2, 150, ECON X, WINTER 2018
    (10, 30, 1, 4, 3, 3, 2, 4); -- PK, CAP, SECTION 1, 376, HUM X, WINTER 2018
    
-- Enrollement table
INSERT INTO enrollement VALUES
	(6, 7, 1, 1, 1),
    (7, 6, 1, 1, 1),
    (7, 8, 3, 2, 2),
    (7, 10, 4, 3, 3),
    (4, 5, 4, 3, 3),
    (9, 9, 3, 2, 2),
    (2, 4, 2, 2, 2),
    (3, 4, 2, 2, 2),
    (5, 4, 2, 2, 2),
    (5, 5, 4, 3, 3),
    (1, 1, 1, 1, 1),
    (1, 9, 3, 2, 2),
    (8, 9, 3, 2, 2),
    (10, 6, 1, 1, 1);
    
    
    
-- #1
SELECT first_name,last_name, CONCAT(
									MONTHNAME(birthdate), ' ', DAY(birthdate), ', ', YEAR(birthdate)) 
									AS Sept_Birthdays
FROM student
WHERE MONTH(birthdate) = 9;


-- #2
SELECT last_name, first_name, floor(datediff('2017-01-05', birthdate)/365) as Years,
	datediff('2017-01-05', birthdate) % 365 as days,
	concat(floor(datediff('2017-01-05', birthdate)/365), ' - Yrs, ', datediff('2017-01-05', birthdate) % 365, ' - Days' ) as Years_and_Days
from student order by Years Desc;

-- #3
SELECT first_name, last_name
FROM student s
	join enrollement e
    on e.idstudent = s.idstudent
    join section sec
    on sec.idsection = e.idsection
    join faculty f
    on f.idfaculty = sec.idfaculty
where faculty_fname = 'John'
order by last_name;

-- #4
SELECT faculty_fname, faculty_lname
from faculty f
	join section s
	on f.idfaculty = s.idfaculty
    join enrollement e
    on e.idsection = s.idsection
    join student st
    on st.idstudent = e.idstudent
Where first_name = 'Bryce'
order by faculty_lname;

-- #5
SELECT first_name, last_name
from section s
	join enrollement e
    on s.idsection = e.idsection
    join student st
    on st.idstudent = e.idstudent
where s.idcourse = 2
order by last_name;

-- #6
SELECT DISTINCT departament_code,  course_num, course_title
FROM section s
	join course c
    on c.idcourse = s.idcourse
	join departament d
    on c.iddepartament = d.iddepartament
where idterm = 2
ORDER BY course_title;

-- #7
SELECT DISTINCT term_name, term_year, (select count(idstudent)
										from enrollement e
											join section s
											on s.idsection = e.idsection
										where idterm = 1 ) AS Enrollement
from enrollement e
	join section s
    on s.idsection = e.idsection
    join term t
    on t.idterm = s.idterm
where term_name = 'Fall'
;

-- #8
SELECT  college_name, count(*) as courses
from course c
	join departament d
    on c.iddepartament = d.iddepartament
    join college co
    on co.idcollege = d.idcollege
group by college_name
order by college_name;



-- #9

SELECT faculty_fname, faculty_lname, sum(section_capacity) as TeachingCapacity
from student st
	join enrollement e
    on st.idstudent = e.idstudent
	join section s
    on s.idsection = e.idsection
	join faculty f
    on s.idfaculty = f.idfaculty
group by faculty_fname
order by TeachingCapacity;

-- #10
select last_name, first_name,  term_name, sum(course_credit) as Credits
from student st
	join enrollement e
    on st.idstudent = e.idstudent
	join section s
    on s.idsection = e.idsection
    join course c
    on c.idcollege = s.idcourse
    join term t
    on s.idterm = t.idterm

where term_name = "Fall"
group by st.first_name, st.last_name
order by Credits Desc;