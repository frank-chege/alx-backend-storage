--addbonus
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
DECLARE project_id INT;

IF NOT EXISTS (SELECT 1 FROM projects WHERE name=project_name) THEN
    INSERT INTO projects (name) 
        VALUES(project_name);
END IF;
SELECT id INTO project_id FROM projects WHERE name=project_name;
IF EXISTS (SELECT 1 FROM corrections WHERE project_id = project_id AND user_id=user_id) THEN
        UPDATE corrections
        SET score=score
        WHERE user_id=user_id AND project_id = project_id;
ELSE
    INSERT INTO corrections(user_id,project_id,score)
        VALUES(user_id, project_id,score);
END IF;
END $$
DELIMITER ;