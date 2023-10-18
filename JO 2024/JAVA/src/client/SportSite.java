package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class SportSite extends BDTable {
    private String nom_sport;
    private String nom_site;

    public SportSite construit(ResultSet res) throws Exception
	{
		SportSite retour = new SportSite(res.getString(1),res.getString(2));   
        return retour;
	}

    public SportSite(String nom_sport,String nom_site){}
    public SportSite(){
        this.nom_sport = nom_sport;
        this.nom_site = nom_site;
    }
    
    public String getNom_sport(){
        return nom_sport;
    }
    public String getNom_site(){
        return nom_site;
    }
}