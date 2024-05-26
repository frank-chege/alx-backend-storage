--compute average score
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN _user_id INT)
BEGIN

DECLARE average FLOAT;
SELECT AVG(score) INTO average
    FROM corrections 
    WHERE user_id = _user_id;
UPDATE  users
SET average_score = average
WHERE id = _user_id;

END $$
DELIMITER;