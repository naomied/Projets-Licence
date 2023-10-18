package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Epreuve extends BDTable {
    private String id_Epreuve;
    private String nom_Epreuve;
    private String id_Session;

    public Epreuve construit(ResultSet res) throws Exception
	{
		Epreuve retour = new Epreuve(res.getString(1),res.getString(2),res.getString(3));   
        return retour;
	}

    public Epreuve() {}

    public Epreuve(String id_Epreuve, String nom_Epreuve, String id_Session) {
        this.id_Epreuve = id_Epreuve;
        this.nom_Epreuve = nom_Epreuve;
        this.id_Session = id_Session;
    }

    public String getId_Epreuve() {
        return this.id_Epreuve;
    }

    public void setId_Epreuve(String id_Epreuve) {
        this.id_Epreuve = id_Epreuve;
    }

    public String getNom_Epreuve() {
        return this.nom_Epreuve;
    }

    public void setNom_Epreuve(String nom_Epreuve) {
        this.nom_Epreuve = nom_Epreuve;
    }

    public String getId_Session() {
        return this.id_Session;
    }

    public void setId_Session(String id_Session) {
        this.id_Session = id_Session;
    }

    
}