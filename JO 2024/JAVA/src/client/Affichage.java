package client;
import java.awt.*;
import java.io.*;
import java.util.*;
import java.sql.*;
import java.lang.reflect.Method;
import java.lang.reflect.Field;
import bdd.*;
import connexion.*; 

public class Affichage
{
    public static void main(String[] strs) throws Exception
    {
        Fonction f = new Fonction();
        Connection con = null;
        Deconnexion decon = new Deconnexion();
        BDTable bd = new BDTable();
        Site site = new Site();
            
        try
        {
            System.out.println("tafiditra anaty try");
            Connexion c=new Connexion();
            c.connecter();
            con = c.getCon();
            java.sql.Statement stmt = con.createStatement();
            System.out.println("tonga");

            String requete="select * from Site";
            System.out.println(requete);
            BDTable [] lSite = f.findWthReq(requete,site,con);
            System.out.println("length "+ lSite.length);
            Site [] listeSite = new Site[lSite.length];

            for(int i=0;i<lSite.length;i++)
            {
                listeSite[i]=(Site)lSite[i];
                System.out.println(listeSite[i].getNom_Site());
            }
            decon.deconnect(c);

        } catch (Exception e1) {
                System.out.println(e1.getMessage());
            }
    }
}
