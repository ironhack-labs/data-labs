
-- cantidad de id students comunes entre ra y students-- 

SELECT *
FROM student
INNER JOIN RA
on student.student_id=RA.student_id;


-- Mostrar la relacion que existe entre la popularidad y capacidad de los profesores, ordenado por lo capaz que sean -- 

SELECT popularity, capability, prof.prof_id
FROM prof
INNER JOIN RA
ON prof.prof_id=RA.prof_id
ORDER BY capability DESC;



-- Crear una temporary table que me relacione la inteligencia de los estudiantes con la registration y una vez sacada esta relacion que me ordene la inteligencia de mayor a menos-- 


CREATE TEMPORARY TABLE IF NOT EXISTS University_intelligence1 
SELECT student.student_id, student.intelligence, registration.sat 
FROM student 
INNER JOIN registration
ON student.student_id=registration.student_id; 

SELECT *
FROM university_intelligence1
ORDER BY intelligence ASC;
