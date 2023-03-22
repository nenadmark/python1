-- SQLite
#users
INSERT INTO users ("name", "email", "password", "is_admin") VALUES ("Pero", "Pero@email.com", "1234", false);
INSERT INTO users ("name", "email", "password", "is_admin") VALUES ("admin", "ad", "12", true);


#plants
INSERT INTO plants ("id", "name", "photo_path") VALUES ("001", "ruza", "photo/path/photo.png");

#pots
INSERT INTO pots ("id", "name", "plant_inside") VALUES ("001", "big_pot", "ruza");
