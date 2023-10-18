package client;
import java.util.*;
import java.sql.*;
import bdd.*;
import connexion.*;

public class Site extends BDTable{
    private String id_Site;
    private String nom_Site;
    private Integer capacite;
    private Integer date_construction;
    private String adresse;

    public Site construit(ResultSet res) throws Exception
	{
		Site retour = new Site(res.getString(1),res.getString(2),
			res.getInt(3),res.getInt(4),res.getString(5));
        return retour;
	}
    public Site() {}
    public Site(String id_Site, String nom_Site, Integer capacite, Integer date_construction, String adresse) {
        this.id_Site = id_Site;
        this.nom_Site = nom_Site;
        this.capacite = capacite;
        this.date_construction = date_construction;
        this.adresse = adresse;
    }

    public String getId_Site() {
        return this.id_Site;
    }

    public void setId_Site(String id_Site) {
        this.id_Site = id_Site;
    }

    public String getNom_Site() {
        return this.nom_Site;
    }

    public void setNom_Site(String nom_Site) {
        this.nom_Site = nom_Site;
    }

    public Integer getCapacite() {
        return this.capacite;
    }

    public void setCapacite(Integer capacite) {
        this.capacite = capacite;
    }

    public Integer getDate_construction() {
        return this.date_construction;
    }

    public void setDate_construction(Integer date_construction) {
        this.date_construction = date_construction;
    }

    public String getAdresse() {
        return this.adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
}