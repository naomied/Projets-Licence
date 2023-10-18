package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Langue extends BDTable {
    private String id_Langue;
    private String nom_Langue;

    public Langue construit(ResultSet res) throws Exception
	{
		Langue retour = new Langue(res.getString(1),res.getString(2));   
        return retour;
	}

    public Langue() {}

    public Langue(String id_Langue, String nom_Langue) {
        this.id_Langue = id_Langue;
        this.nom_Langue = nom_Langue;
    }
    
    public String getId_Langue() {
        return this.id_Langue;
    }

    public void setId_Langue(String id_Langue) {
        this.id_Langue = id_Langue;
    }

    public String getNom_Langue() {
        return this.nom_Langue;
    }

    public void setNom_Langue(String nom_Langue) {
        this.nom_Langue = nom_Langue;
    }

    
}