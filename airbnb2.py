import mysql.connector

class BDD:

    def __init__(self):#qd on appelle la classe ttes les valeurs dans le init vont être executees
        self.mydb=mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="airb")
        self.curs = self.mydb.cursor()


    def close(self):
        self.curs.close()
        self.bdd.close()

        # create view v_location2 AS
        #     select quartier.nom_quartier, secteur.nom_secteur, room_type.r_type, location.prix, location.nuit_mini, location.dispo from location
        #     join quartier on quartier.id_quartier = location.id_quartier
        #     join secteur on secteur.id_secteur= location.id_secteur
        #     join room_type on room_type.id_room_type = location.id_room_type

    
    def get_v_location2(self):
        # self.connect()
        self.curs.execute("select * from v_location2")
        airbnbres = self.curs.fetchall()
        #self.close()
        return airbnbres



        #----------------------------------------------------------------------------------
        # DELIMITER //
        # CREATE PROCEDURE prix_quartiers
        # (IN secqua INT(20))
        # BEGIN
        # SELECT location.id_quartier, location.prix, quartier.nom_quartier
        # FROM location
        # JOIN quartier on quartier.id_quartier = location.id_quartier
        # join secteur on secteur.id_secteur= location.id_secteur
        # WHERE prix < secqua;
        # END //
        # DELIMITER ;


    def appeler_procedure_prix_quartiers(self, prix):
        self.curs.callproc("prix_quartiers",(prix,))
        for result in self.curs.stored_results():
            return result.fetchall()
           # self.close()



        #------------------------------------------------------------------------------
        # DELIMITER //
        # CREATE PROCEDURE dispo_prix
        # (IN `correlation` INT)
        # BEGIN
        # SELECT location.prix, location.nuit_mini
        # FROM location
        # WHERE location.prix>correlation;
        # END//
        # DELIMITER ;


    def appeler_procedure_dispo_prix(self, prix):
        self.curs.callproc("dispo_prix",(prix,))
        for result in self.curs.stored_results():
            return result.fetchall()
           # self.close()

    


        #_____________________________________________________________________________

        # DELIMITER //
        # CREATE PROCEDURE dispo_prix_quartier
        # (IN correlation INT(50))
        # BEGIN
        # SELECT location.prix, location.nuit_mini, quartier.nom_quartier
        # FROM location
        # JOIN quartier on quartier.id_quartier = location.id_quartier
        # WHERE location.prix>correlation;
        # END //
        # DELIMITER ;

    def appeler_procedure_dispo_prix_quartier(self, prix):
        self.curs.callproc("dispo_prix_quartier",(prix,))
        for result in self.curs.stored_results():
            return result.fetchall()
           # self.close()


        #______________________________________________________


        # DELIMITER //
        # CREATE PROCEDURE prix_moyen_quartier()
        # BEGIN
        # SELECT quartier.nom_quartier, AVG(location.prix)
        # FROM location
        # join quartier on quartier.id_quartier = location.id_quartier
        # GROUP BY location.id_quartier;
        # END //
        # DELIMITER ;

    def appeler_procedure_prix_moyen_quartier(self):
        self.curs.callproc("prix_moyen")
        return result.fetchall()
           # self.close()

        # print(BDD.appeler_procedure())
        #__________________________________________________________________


        # DELIMITER //
        # CREATE PROCEDURE secteur_quartier
        # (IN `secqua` VARCHAR(20))
        # BEGIN
        # SELECT *
        # FROM location
        # join quartier on quartier.id_quartier = location.id_quartier
        # WHERE nom_quartier = secqua;
        # END//
        # DELIMITER ;

    def appeler_procedure_secteur_quartier(self, quartier):
        self.curs.callproc("secteur_quartier",(quartier,))
        for result in self.curs.stored_results():
            return result.fetchall()
           # self.close()

        #________________________________________________________________________

        # DELIMITER //
        # CREATE PROCEDURE prix_maxi
        # (IN correlation INT)
        # BEGIN
        # SELECT location.id_quartier, location.id_secteur, location.prix, location.nuit_mini, quartier.nom_quartier, secteur.nom_secteur
        # FROM location
        # JOIN quartier on quartier.id_quartier = location.id_quartier
        # join secteur on secteur.id_secteur = location.id_secteur
        # WHERE location.prix>correlation;
        # END//
        # DELIMITER ;

    def appeler_procedure_prix_maxi(self, prix):
        self.curs.callproc("prix_quartiers",(prix,))
        for result in self.curs.stored_results():
            return result.fetchall()
           # self.close()
    
    def appeler_procedure_prix_quartiersup(self, prix):
        self.curs.callproc("prix_quartiersup",(prix,))
        for result in self.curs.stored_results():
            return result.fetchall()
           # self.close()






    def dbRequestlocation(self):
        request = "SELECT * FROM location"
        self.curs.execute(request)
        response = self.curs.fetchall()
        return response
        




# bdd = BDD()
# # #print(bdd.get_v_location2())  
# print(bdd.appeler_procedure_prix_quartiersup(500))
# print(bdd.appeler_procedure_dispo_prix(50)) 


# print(bdd.appeler_procedure_dispo_prix_quartier(50))
#print(bdd.appeler_procedure_secteur_quartier("Manhattan"))
#print(bdd.appeler_procedure_prix_moyen_quartier())
#print(bdd.appeler_procedure_prix_maxi(400))
#print(bdd.dbRequestlocation())

