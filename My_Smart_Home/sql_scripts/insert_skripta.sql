-- SQLite
-- INSERT naredbe za dodavanje soba
INSERT INTO rooms (name, floor) VALUES ("Living room", 0);
INSERT INTO rooms (name, floor) VALUES ("Kitchen", 0);
INSERT INTO rooms (name, floor) VALUES ("Guest room small", 0);
INSERT INTO rooms (name, floor) VALUES ("Bedroom", 1);
INSERT INTO rooms (name, floor) VALUES ("Guest room large", 1);

-- INSERT naredbe za dodavanje TV uređaja
INSERT INTO televisions (name, manufacturer, active, volume, channel, room_id)
    VALUES ("Main TV", "Samsung", 0, 5, 1, 1);

INSERT INTO televisions (name, manufacturer, active, volume, channel, room_id)
    VALUES ("Guest room TV 1", "LG", 0, 5, 1, 3);

INSERT INTO televisions (name, manufacturer, active, volume, channel, room_id)
    VALUES ("Guest room TV 2", "LG", 0, 5, 1, 5);

INSERT INTO televisions (name, manufacturer, active, volume, channel, room_id)
    VALUES ("Bedroom TV", "Sony", 0, 5, 1, 4);


-- INSERT naredba za dodavanje hladnjaka
INSERT INTO refrigerators (name, manufacturer, active, temperature, room_id) 
    VALUES ("Double Door Fridge", "Bosch", 1, 6, 2);


-- INSERT naredba za dodavanje svijetla
INSERT INTO lights (name, manufacturer, active, intensity, room_id) 
    VALUES ("Living Room Lights", "Phillips HUE", 1, 5, 1);

INSERT INTO lights (name, manufacturer, active, intensity, room_id) 
    VALUES ("kitchen Lights", "Phillips HUE", 1, 7, 2);

INSERT INTO lights (name, manufacturer, active, intensity, room_id) 
    VALUES ("Guest room small Lights", "Phillips HUE", 1, 2, 3);

INSERT INTO lights (name, manufacturer, active, intensity, room_id) 
    VALUES ("Bedroom Lights", "Phillips HUE", 1, 1, 4);

INSERT INTO lights (name, manufacturer, active, intensity, room_id) 
    VALUES ("Guest room large Lights", "Phillips HUE", 1, 2, 5);


    -- INSERT naredba za dodavanje zvucnika
INSERT INTO speakers (name, manufacturer, active, volume, playlist_playing, eq_settings, room_id) 
    VALUES ("Living Room Sounds", "AdamAudio", 1, 3, 1, "flat", 1);

INSERT INTO speakers (name, manufacturer, active, volume, playlist_playing, eq_settings, room_id) 
    VALUES ("kitchen Sounds", "AdamAudio", 1, 4, 1, "flat", 2);

INSERT INTO speakers (name, manufacturer, active, volume, playlist_playing, eq_settings, room_id) 
    VALUES ("Guest room small Sounds", "AdamAudio", 1, 1, 1, "flat", 3);

INSERT INTO speakers (name, manufacturer, active, volume, playlist_playing, eq_settings, room_id) 
    VALUES ("Bedroom Sounds", "AdamAudio", 1, 2, 1, "flat", 4);

INSERT INTO speakers (name, manufacturer, active, volume, playlist_playing, eq_settings, room_id) 
    VALUES ("Guest room large Sounds", "AdamAudio", 1, 1, 1, "flat", 5);