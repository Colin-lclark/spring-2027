DROP DATABASE IF EXISTS registrar;
CREATE DATABASE registrar;
USE registrar;

CREATE TABLE course(
       id INT UNSIGNED,
       name VARCHAR(50) NOT NULL,
       PRIMARY KEY (id)
);

CREATE TABLE department(
       id INT UNSIGNED,
       name VARCHAR(50) NOT NULL,
       budget DECIMAL(12,2) CHECK (budget > 0),
       PRIMARY KEY (id)
);

CREATE TABLE instructor(
       id INT UNSIGNED,
       name VARCHAR(50) NOT NULL,
       salary DECIMAL(8,2) NOT NULL,
       dept_id INT UNSIGNED,
       PRIMARY KEY (id),
       FOREIGN KEY (dept_id) REFERENCES department (id)
);

CREATE TABLE student(
       id INT UNSIGNED,
       name VARCHAR(50) NOT NULL,
       credits INT UNSIGNED NOT NULL,
       advisor INT UNSIGNED,
       PRIMARY KEY (id),
       FOREIGN KEY (advisor) REFERENCES instructor (id)
);

CREATE TABLE instructor_teaches_course(
       instructor_id INT UNSIGNED,
       course_id INT UNSIGNED,
       FOREIGN KEY (instructor_id) REFERENCES instructor (id),
       FOREIGN KEY (course_id) REFERENCES course (id)
);       

CREATE TABLE student_takes_course(
       student_id INT UNSIGNED,
       course_id INT UNSIGNED,
       FOREIGN KEY (student_id) REFERENCES student (id),
       FOREIGN KEY (course_id) REFERENCES course (id)
);
