package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Pays extends BDTable {
    private String id_Pays;
    private String nom_Pays;
    private String drapeau;

    public Pays construit(ResultSet res) throws Exception
	{
		Pays retour = new Pays(res.getString(1),res.getString(2),res.getString(3));
        return retour;
	}
    public Pays() {}

    public Pays(String id_Pays, String nom_Pays, String drapeau) {
        this.id_Pays = id_Pays;
        this.nom_Pays = nom_Pays;
        this.drapeau = drapeau;
    }

    public String getId_Pays() {
        return this.id_Pays;
    }

    public void setId_Pays(String id_Pays) {
        this.id_Pays = id_Pays;
    }

    public String getNom_Pays() {
        return this.nom_Pays;
    }

    public void setNom_Pays(String nom_Pays) {
        this.nom_Pays = nom_Pays;
    }

    public String getDrapeau() {
        return this.drapeau;
    }

    public void setDrapeau(String drapeau) {
        this.drapeau = drapeau;
    }

    
}