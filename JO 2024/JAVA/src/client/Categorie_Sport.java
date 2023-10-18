package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Categorie_Sport extends BDTable {
    private String id_Categorie_Sport;
    private String nom_Categorie_Sport;

    public Categorie_Sport construit(ResultSet res) throws Exception
	{
		Categorie_Sport retour = new Categorie_Sport(res.getString(1),res.getString(2));   
        return retour;
	}

    public Categorie_Sport() {}
    public Categorie_Sport(String id_Categorie_Sport, String nom_Categorie_Sport) {
        this.id_Categorie_Sport = id_Categorie_Sport;
        this.nom_Categorie_Sport = nom_Categorie_Sport;
    }

    public String getId_Categorie_Sport() {
        return this.id_Categorie_Sport;
    }

    public void setId_Categorie_Sport(String id_Categorie_Sport) {
        this.id_Categorie_Sport = id_Categorie_Sport;
    }

    public String getNom_Categorie_Sport() {
        return this.nom_Categorie_Sport;
    }

    public void setNom_Categorie_Sport(String nom_Categorie_Sport) {
        this.nom_Categorie_Sport = nom_Categorie_Sport;
    }

    
}