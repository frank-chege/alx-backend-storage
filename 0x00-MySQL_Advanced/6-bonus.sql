--addbonus
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
DECLARE project_id INT;

IF NOT EXISTS (SELECT 1 FROM projects WHERE name=project_name) THEN
    INSERT INTO projects (name) 
        VALUES(project_name);
END IF;
SELECT id INTO project_id FROM projects WHERE name=project_name;
INSERT INTO corrections(user_id,project_id,score)
    VALUES(user_id, project_id,score);
END $$
DELIMITER ;