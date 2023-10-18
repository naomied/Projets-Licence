package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class SportJO extends BDTable {
    private String id_Sport_Jo;
    private String nom_Sport_Jo;
    private String nom_Anglais_Jo;
    private Date date_Creation_Sport_Jo;
    private String categorie_sport_Jo;

    
    public SportJO construit(ResultSet res) throws Exception
	{
		SportJO retour = new SportJO(res.getString(1),res.getString(2),res.getString(3),
        res.getDate(4),res.getString(5));   
        return retour;
	}
    
    public SportJO() {
    }

    public SportJO(String id_Sport_Jo, String nom_Sport_Jo, String nom_Anglais_Jo, Date date_Creation_Sport_Jo, String categorie_sport_Jo) {
        this.id_Sport_Jo = id_Sport_Jo;
        this.nom_Sport_Jo = nom_Sport_Jo;
        this.nom_Anglais_Jo = nom_Anglais_Jo;
        this.date_Creation_Sport_Jo = date_Creation_Sport_Jo;
        this.categorie_sport_Jo = categorie_sport_Jo;
    }

    public String getId_Sport_Jo() {
        return this.id_Sport_Jo;
    }

    public void setId_Sport_Jo(String id_Sport_Jo) {
        this.id_Sport_Jo = id_Sport_Jo;
    }

    public String getNom_Sport_Jo() {
        return this.nom_Sport_Jo;
    }

    public void setNom_Sport_Jo(String nom_Sport_Jo) {
        this.nom_Sport_Jo = nom_Sport_Jo;
    }

    public String getNom_Anglais_Jo() {
        return this.nom_Anglais_Jo;
    }

    public void setNom_Anglais_Jo(String nom_Anglais_Jo) {
        this.nom_Anglais_Jo = nom_Anglais_Jo;
    }

    public Date getDate_Creation_Sport_Jo() {
        return this.date_Creation_Sport_Jo;
    }

    public void setDate_Creation_Sport_Jo(Date date_Creation_Sport_Jo) {
        this.date_Creation_Sport_Jo = date_Creation_Sport_Jo;
    }

    public String getCategorie_sport_Jo() {
        return this.categorie_sport_Jo;
    }

    public void setCategorie_sport_Jo(String categorie_sport_Jo) {
        this.categorie_sport_Jo = categorie_sport_Jo;
    }

}