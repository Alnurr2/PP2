CREATE OR REPLACE PROCEDURE upsert_contact(p_phone VARCHAR, p_name VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE phone_owner = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE phone_owner = p_name; 
    ELSE
        INSERT INTO phonebook(phone, phone_owner) VALUES(p_phone, p_name);
    END IF;
END;
$$;



CREATE OR REPLACE PROCEDURE delete_contact(phone_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
DELETE FROM phonebook WHERE phone_owner = phone_value OR phone = phone_value;
END;
$$;



CREATE OR REPLACE PROCEDURE insert_contacts(
    phones TEXT[],
    names TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(names,1) != array_length(phones,1) THEN
        RAISE EXCEPTION 'Array lengths mismatch';
    END IF;

    FOR i IN 1..array_length(names, 1) LOOP
        
        IF phones[i] !~ '^\+7\d{10}$' THEN
            RAISE NOTICE 'Invalid phone: %', phones[i];
        ELSE
            CALL upsert_contact(phones[i], names[i]);
        END IF;

    END LOOP;
END;
$$;