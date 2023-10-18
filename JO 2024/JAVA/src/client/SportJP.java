package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class SportJP extends BDTable{
    private String id_Sport_Jp;
    private String nom_Sport_Jp;
    private String nom_Anglais_Jp;
    private Date date_Creation_Sport_Jp;
    private String categorie_sport_Jp;

    public SportJP construit(ResultSet res) throws Exception
	{
		SportJP retour = new SportJP(res.getString(1),res.getString(2),res.getString(3),res.getDate(4),res.getString(5));   
        return retour;
	}
    public SportJP() {}

    public SportJP(String id_Sport_Jp, String nom_Sport_Jp, String nom_Anglais_Jp, Date date_Creation_Sport_Jp, String categorie_sport_Jp) {
        this.id_Sport_Jp = id_Sport_Jp;
        this.nom_Sport_Jp = nom_Sport_Jp;
        this.nom_Anglais_Jp = nom_Anglais_Jp;
        this.date_Creation_Sport_Jp = date_Creation_Sport_Jp;
        this.categorie_sport_Jp = categorie_sport_Jp;
    }

    public String getId_Sport_Jp() {
        return this.id_Sport_Jp;
    }

    public void setId_Sport_Jp(String id_Sport_Jp) {
        this.id_Sport_Jp = id_Sport_Jp;
    }

    public String getNom_Sport_Jp() {
        return this.nom_Sport_Jp;
    }

    public void setNom_Sport_Jp(String nom_Sport_Jp) {
        this.nom_Sport_Jp = nom_Sport_Jp;
    }

    public String getNom_Anglais_Jp() {
        return this.nom_Anglais_Jp;
    }

    public void setNom_Anglais_Jp(String nom_Anglais_Jp) {
        this.nom_Anglais_Jp = nom_Anglais_Jp;
    }

    public Date getDate_Creation_Sport_Jp() {
        return this.date_Creation_Sport_Jp;
    }

    public void setDate_Creation_Sport_Jp(Date date_Creation_Sport_Jp) {
        this.date_Creation_Sport_Jp = date_Creation_Sport_Jp;
    }
    public String getCategorie_sport_Jp() {
        return this.categorie_sport_Jp;
    }

    public void setCategorie_sport_Jp(String categorie_sport_Jp) {
        this.categorie_sport_Jp = categorie_sport_Jp;
    }
    
}