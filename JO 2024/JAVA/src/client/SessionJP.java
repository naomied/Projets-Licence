package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.Time;
import java.util.Date;
import bdd.*;
import connexion.*;

public class SessionJP extends BDTable {
    private String id_Session;
    private int num_Jour_Session;
    private Date date_Session;
    private Time heure_Debut;
    private Time heure_Fin;
    private String id_Sport_JP;
    private String id_Site;

    public SessionJP construit(ResultSet res) throws Exception
	{
		SessionJP retour = new SessionJP(res.getString(1),res.getInt(2),res.getDate(3),
        res.getTime(4),res.getTime(5),res.getString(6),res.getString(7));   
        return retour;
	}

    public SessionJP() {}
    public SessionJP(String id_Session, int num_JPur_Session, Date date_Session, Time heure_Debut, Time heure_Fin, String id_Sport_JP, String id_Site) {
        this.id_Session = id_Session;
        this.num_Jour_Session = num_JPur_Session;
        this.date_Session = date_Session;
        this.heure_Debut = heure_Debut;
        this.heure_Fin = heure_Fin;
        this.id_Sport_JP = id_Sport_JP;
        this.id_Site = id_Site;
    }
    public String getId_Session() {
        return this.id_Session;
    }

    public void setId_Session(String id_Session) {
        this.id_Session = id_Session;
    }

    public int getNum_Jour_Session() {
        return this.num_Jour_Session;
    }

    public void setNum_Jour_Session(int num_JPur_Session) {
        this.num_Jour_Session = num_JPur_Session;
    }

    public Date getDate_Session() {
        return this.date_Session;
    }

    public void setDate_Session(Date date_Session) {
        this.date_Session = date_Session;
    }

    public Time getHeure_Debut() {
        return this.heure_Debut;
    }

    public void setHeure_Debut(Time heure_Debut) {
        this.heure_Debut = heure_Debut;
    }

    public Time getHeure_Fin() {
        return this.heure_Fin;
    }

    public void setHeure_Fin(Time heure_Fin) {
        this.heure_Fin = heure_Fin;
    }

    public String getId_Sport_JP() {
        return this.id_Sport_JP;
    }

    public void setId_Sport_JP(String id_Sport_JP) {
        this.id_Sport_JP = id_Sport_JP;
    }
    public String getId_Site() {
        return this.id_Site;
    }

    public void setId_Site(String id_Site) {
        this.id_Site = id_Site;
    }
    
}