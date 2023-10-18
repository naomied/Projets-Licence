package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Athlete extends BDTable {
    private String id_Athlete;
    private String nom_Athlete;
    private String prenom_Athlete;
    private Date date_Naissance_Athlete;
    private char genre;
    private String id_Pays;
    private String jeux;
    private int Nb_Participation_Athlete;

    
    public Athlete construit(ResultSet res) throws Exception
	{
		Athlete retour = new Athlete(res.getString(1),res.getString(2),res.getString(3),
        res.getDate(4),(char)res.getString(5).charAt(0),res.getString(6),res.getString(7),res.getInt(8));   
        return retour;
	}
    public Athlete() {}

    public Athlete(String id_Athlete, String nom_Athlete, String prenom_Athlete, Date date_Naissance_Athlete, char genre, String id_Pays, String jeux, int Nb_Participation_Athlete) {
        this.id_Athlete = id_Athlete;
        this.nom_Athlete = nom_Athlete;
        this.prenom_Athlete = prenom_Athlete;
        this.date_Naissance_Athlete = date_Naissance_Athlete;
        this.genre = genre;
        this.id_Pays = id_Pays;
        this.jeux = jeux;
        this.Nb_Participation_Athlete = Nb_Participation_Athlete;
    }

    public String getId_Athlete() {
        return this.id_Athlete;
    }

    public void setId_Athlete(String id_Athlete) {
        this.id_Athlete = id_Athlete;
    }

    public String getNom_Athlete() {
        return this.nom_Athlete;
    }

    public void setNom_Athlete(String nom_Athlete) {
        this.nom_Athlete = nom_Athlete;
    }

    public String getPrenom_Athlete() {
        return this.prenom_Athlete;
    }

    public void setPrenom_Athlete(String prenom_Athlete) {
        this.prenom_Athlete = prenom_Athlete;
    }

    public Date getDate_Naissance_Athlete() {
        return this.date_Naissance_Athlete;
    }

    public void setDate_Naissance_Athlete(Date date_Naissance_Athlete) {
        this.date_Naissance_Athlete = date_Naissance_Athlete;
    }

    public char getGenre() {
        return this.genre;
    }

    public void setGenre(char genre) {
        this.genre = genre;
    }

    public String getId_Pays() {
        return this.id_Pays;
    }

    public void setId_Pays(String id_Pays) {
        this.id_Pays = id_Pays;
    }

    public String getJeux() {
        return this.jeux;
    }

    public void setJeux(String jeux) {
        this.jeux = jeux;
    }

    public int getNb_Participation_Athlete() {
        return this.Nb_Participation_Athlete;
    }

    public void setNb_Participation_Athlete(int Nb_Participation_Athlete) {
        this.Nb_Participation_Athlete = Nb_Participation_Athlete;
    }

}