package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.Time;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Detenteur_Record extends BDTable {
    private String id_Detenteur_Record;
    private String nom_Detenteur_Record;
    private String prenom_Detenteur_Record;
    private Date date_naissance;
    private String id_Epreuve;

    public Detenteur_Record construit(ResultSet res) throws Exception
	{
		Detenteur_Record retour = new Detenteur_Record(res.getString(1),res.getString(2),
        res.getString(3),res.getDate(4),res.getString(5));   
        return retour;
	}

    public Detenteur_Record() {}

    public Detenteur_Record(String id_Detenteur_Record, String nom_Detenteur_Record, String prenom_Detenteur_Record, Date date_naissance, String id_Epreuve) {
        this.id_Detenteur_Record = id_Detenteur_Record;
        this.nom_Detenteur_Record = nom_Detenteur_Record;
        this.prenom_Detenteur_Record = prenom_Detenteur_Record;
        this.date_naissance = date_naissance;
        this.id_Epreuve = id_Epreuve;
    }

    public String getId_Detenteur_Record() {
        return this.id_Detenteur_Record;
    }

    public void setId_Detenteur_Record(String id_Detenteur_Record) {
        this.id_Detenteur_Record = id_Detenteur_Record;
    }

    public String getNom_Detenteur_Record() {
        return this.nom_Detenteur_Record;
    }

    public void setNom_Detenteur_Record(String nom_Detenteur_Record) {
        this.nom_Detenteur_Record = nom_Detenteur_Record;
    }

    public String getPrenom_Detenteur_Record() {
        return this.prenom_Detenteur_Record;
    }

    public void setPrenom_Detenteur_Record(String prenom_Detenteur_Record) {
        this.prenom_Detenteur_Record = prenom_Detenteur_Record;
    }

    public Date getDate_naissance() {
        return this.date_naissance;
    }

    public void setDate_naissance(Date date_naissance) {
        this.date_naissance = date_naissance;
    }

    public String getId_Epreuve() {
        return this.id_Epreuve;
    }

    public void setId_Epreuve(String id_Epreuve) {
        this.id_Epreuve = id_Epreuve;
    }
}