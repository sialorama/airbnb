# vue qui affiche les valeurs des identifiants dans la table location

create view v_location2 AS
    select quartier.nom_quartier, secteur.nom_secteur, room_type.r_type, location.prix, location.nuit_mini, location.dispo from location
    join quartier on quartier.id_quartier = location.id_quartier
    join secteur on secteur.id_secteur= location.id_secteur
    join room_type on room_type.id_room_type = location.id_room_type

créer une procedure qui affiche les prix par quartier


#dispo_prix : procédure permettant d afficher la correlation entre le nombre de nuitées et le prix,
# lorsqu on appelle la fonction saisir le prix seuil CALL dispo_prix(prix)
DELIMITER //
CREATE PROCEDURE dispo_prix
(IN correlation INT)
BEGIN
SELECT location.prix, location.nuit_mini
FROM location
WHERE location.prix>correlation;
END
DELIMITER ; 


# dispo_prix_quartier : procédure permettant d afficher la correlation entre le quartier, le nombre de nuitées et le prix,
# lorsqu on appelle la fonction saisir le prix seuil
DELIMITER //
CREATE PROCEDURE dispo_prix_quartier
(IN correlation INT)
BEGIN
SELECT location.prix, location.nuit_mini, location.quartier
FROM location
JOIN quartier on quartier.id_quartier = location.id_quartier
WHERE location.prix>correlation;
END
DELIMITER ; 

# prix_maxi : procédure permettant d afficher les quartiers et les secteurs ayant les prix les plus eleves 
# lorsqu on appelle la fonction saisir le prix seuil
DELIMITER //
CREATE PROCEDURE prix_maxi
(IN correlation INT)
BEGIN
SELECT location.id_quartier, location.id_secteur, location.prix, location.nuit_mini, quartier.nom_quartier, secteur.nom_secteur
FROM location
JOIN quartier on quartier.id_quartier = location.id_quartier
join secteur on secteur.id_secteur = location.id_secteur
WHERE location.prix>correlation;
END
DELIMITER ; 

#secteur_quartier : procédure qui affiche les secteurs pour un quartier
# saisir le nom du quartier lorsquon appelle la fonction
DELIMITER //
CREATE PROCEDURE secteur_quartier
(IN `secqua` VARCHAR(20))
BEGIN
SELECT *
FROM location
join quartier on quartier.id_quartier = location.id_quartier
WHERE nom_quartier = secqua;
END
DELIMITER ;


#prix_quartier : procédure qui appelle les prix inférieurs à x pour un quartier
# saisir le prix  lorsquon appelle la fonction
DELIMITER //
CREATE PROCEDURE prix_quartiers
(IN `secqua` INT(20))
BEGIN
SELECT location.id_quartier, location.prix, quartier.nom_quartier
FROM location
JOIN quartier on quartier.id_quartier = location.id_quartier
join secteur on secteur.id_secteur= location.id_secteur
WHERE prix < secqua;
END//
DELIMITER ;


#finalite : procedure qui affiche le room_type en fonction du quartier, du secteur et du prix
#finalite : procedure qui affiche la relation entre disponibilite et prix

DELIMITER //
CREATE PROCEDURE prix_moyen_quartier
(IN `quartier` VARCHAR(20))
BEGIN
SELECT quartier.nom_quartier AVG(location.prix)
FROM location
GROUP BY quartier
join quartier on quartier.id_quartier = location.id_quartier
WHERE nom_quartier = quartier;
END
DELIMITER ;

DELIMITER //
CREATE PROCEDURE prix_moyen_quartier
(IN `quartier` VARCHAR(20))
BEGIN
SELECT quartier.nom_quartier, AVG(location.prix)
FROM location
join quartier on quartier.id_quartier = location.id_quartier
GROUP BY location.id_quartier
WHERE 
END
DELIMITER ;

#prix_moyen_quartier : procédure qui affiche les prix moyen par quartier
# saisir le prix  lorsquon appelle la fonction
DELIMITER //
CREATE PROCEDURE prix_moyen_quartier()
BEGIN
SELECT quartier.nom_quartier, AVG(location.prix)
FROM location
join quartier on quartier.id_quartier = location.id_quartier
GROUP BY location.id_quartier;
END
DELIMITER //

#prix_moyen_quartier_secteur : procédure qui affiche les prix moyen par quartier et par secteur
# saisir le prix  lorsquon appelle la fonction
DELIMITER //
CREATE PROCEDURE prix_moyen_quartier_secteur()
BEGIN
SELECT quartier.nom_quartier, secteur.nom_secteur, AVG(location.prix)
FROM location
join quartier on quartier.id_quartier = location.id_quartier
join secteur on secteur.id_secteur = location.id_secteur
GROUP BY location.id_quartier, location.id_secteur;
END
DELIMITER //