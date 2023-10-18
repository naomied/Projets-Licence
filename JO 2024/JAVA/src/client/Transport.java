package client;

import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Date;
import bdd.*;
import connexion.*;

public class Transport extends BDTable{
    private String id_Transport;
    private String id_Type_Transport;
    private String id_Site;

    public Transport construit(ResultSet res) throws Exception
	{
		Transport retour = new Transport(res.getString(1),res.getString(2),res.getString(3));   
        return retour;
	}

    public Transport(String id_Transport, String id_Type_Transport, String id_Site) {
        this.id_Transport = id_Transport;
        this.id_Type_Transport = id_Type_Transport;
        this.id_Site = id_Site;
    }
    public Transport() {}

    public String getId_Transport() {
        return this.id_Transport;
    }

    public void setId_Transport(String id_Transport) {
        this.id_Transport = id_Transport;
    }

    public String getId_Type_Transport() {
        return this.id_Type_Transport;
    }

    public void setId_Type_Transport(String id_Type_Transport) {
        this.id_Type_Transport = id_Type_Transport;
    }

    public String getId_Site() {
        return this.id_Site;
    }

    public void setId_Site(String id_Site) {
        this.id_Site = id_Site;
    }
}