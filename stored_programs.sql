CREATE TABLE IF NOT EXISTS franchise (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL
);

DELIMITER //
CREATE TRIGGER before_insert_amusement_park
BEFORE INSERT
ON amusement_park
FOR EACH ROW
BEGIN
    DECLARE franchise_count INT;

   SELECT COUNT(*) INTO franchise_count FROM franchise WHERE id = NEW.franchise_id;

    IF franchise_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'There is no franchise with this id';
    END IF;
END
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insert_default_franchises()
BEGIN
	DECLARE counter INT DEFAULT 1;
	WHILE counter <= 10 DO
		INSERT INTO franchise (name) VALUES (CONCAT('Noname', counter));
        SET counter = counter  + 1;
    END WHILE;
END //

DELIMITER ;

DELIMITER //
CREATE TRIGGER before_delete_franchise
BEFORE DELETE
ON franchise
FOR EACH ROW
BEGIN
    DECLARE amusement_park_count INT;

    SELECT COUNT(*) INTO amusement_park_count FROM amusement_park WHERE franchise_id = OLD.id;

    IF amusement_park_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Unable to delete franchise because there are related parks.';
    END IF;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER forbid_update_role_permission
BEFORE UPDATE
ON role_has_permission
FOR EACH ROW
BEGIN
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Forbidden action: Not allowed to update';
END //
DELIMITER ;


CREATE TABLE log_person (
  id INT NOT NULL AUTO_INCREMENT,
  person_id INT NOT NULL,
  PRIMARY KEY (id, person_id)
);

DELIMITER //
CREATE TRIGGER log_people_on_update
AFTER UPDATE
ON person
FOR EACH ROW
BEGIN
	INSERT INTO log_person (`person_id`) VALUES
	(OLD.id, CURRENT_TIMESTAMP);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER allowed_insert_countries
BEFORE INSERT
ON `location`
FOR EACH ROW
BEGIN
	IF NEW.country IN ('Russia', 'Belarus', 'Hungary') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Your country is FORBIDDEN';
	END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insert_role(IN role_name VARCHAR(30))
BEGIN
    INSERT INTO role (`name`) VALUES (role_name);
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE insert_role_permission(
	IN role_id INT,
	IN permission_id INT
)
BEGIN
	DECLARE permission_count INT;
    DECLARE role_count INT;

    SELECT COUNT(*) INTO permission_count FROM permission WHERE permission.id = permission_id;
    SELECT COUNT(*) INTO role_count FROM role WHERE role.id = role_id;

	IF permission_count = 0 OR role_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'There is no role or permission with this id';
    END IF;

	INSERT INTO role_has_permission (role_id, permission_id) VALUES (role_id, permission_id);
END //

DELIMITER ;

DELIMITER //
CREATE FUNCTION get_park_with_max_visitors()
RETURNS DECIMAL(6,1)
deterministic
BEGIN
	DECLARE result DECIMAL(6, 1);

    SELECT MAX(max_visitors) INTO result FROM amusement_park;

    RETURN result;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS create_tables_from_role;

DELIMITER //
CREATE PROCEDURE create_tables_from_role()
BEGIN
	DECLARE done int DEFAULT false;
	DECLARE role_name varchar(45);

    DECLARE Role_Cursor CURSOR
		FOR SELECT name FROM role;

	DECLARE CONTINUE HANDLER
		FOR NOT FOUND SET done = true;

    OPEN Role_Cursor;

    createTable: LOOP
		FETCH Role_Cursor INTO role_name;
        IF done=true THEN LEAVE createTable;
        END IF;
        SET @temp_query=CONCAT(
			"CREATE TABLE ",
            role_name,
            "_",
            REPLACE(CURRENT_DATE(), "-", "_"),
			" (
				id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
				`name` VARCHAR(45) NOT NULL
			);
			"
        );
        PREPARE SQLString FROM @temp_query;
        EXECUTE SQLString;
        DEALLOCATE PREPARE SQLString;
        END LOOP;

	CLOSE Role_Cursor;
END //
DELIMITER ;