package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Type_Transport extends BDTable {
    private String id_Type_Transport;
    private String nom_Type_Transport;
    private String caracteristique;

    public Type_Transport construit(ResultSet res) throws Exception
	{
		Type_Transport retour = new Type_Transport(res.getString(1),res.getString(2),res.getString(3));   
        return retour;
	}
    public Type_Transport() {}

    public Type_Transport(String id_Type_Transport, String nom_Type_Transport, String caracteristique) {
        this.id_Type_Transport = id_Type_Transport;
        this.nom_Type_Transport = nom_Type_Transport;
        this.caracteristique = caracteristique;
    }

    public String getId_Type_Transport() {
        return this.id_Type_Transport;
    }

    public void setId_Type_Transport(String id_Type_Transport) {
        this.id_Type_Transport = id_Type_Transport;
    }

    public String getNom_Type_Transport() {
        return this.nom_Type_Transport;
    }

    public void setNom_Type_Transport(String nom_Type_Transport) {
        this.nom_Type_Transport = nom_Type_Transport;
    }

    public String getCaracteristique() {
        return this.caracteristique;
    }

    public void setCaracteristique(String caracteristique) {
        this.caracteristique = caracteristique;
    }


}