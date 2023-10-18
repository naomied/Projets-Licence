package bdd;
import java.io.*;
import java.util.*;
import java.sql.*;
import java.lang.reflect.Method;
import java.lang.reflect.Field;

public class Fonction{
    public BDTable[] findWthReq(String req,BDTable filtre,Connection con) throws Exception
    {
        java.sql.Statement stmt = con.createStatement();
        ResultSet res=stmt.executeQuery(req);
        Vector val=new Vector();
        Method[] limeth=filtre.getClass().getDeclaredMethods();
        while (res.next()) 
        {
            Object[] args=new Object[1];
            args[0]=res;
            val.addElement(filtre.methConstr().invoke(filtre,args));
        }
        BDTable[] rep=new BDTable[val.size()];
        for(int i=0;i<val.size();i++)
        {
            rep[i]=((BDTable)val.get(i));
        }
        stmt.close();
        return rep;
    }
    
    public BDTable[] find(BDTable filtre,Connection con) throws Exception
    {
        //Method[] methMisy=filtre.methNotNull();
        Field[] fieldMisy=filtre.fieldNotNull();
        String req="select * from "+filtre.getClass().getSimpleName();
        //System.out.println(filtre.countNotNull());
        if(filtre.countNotNull()==0) req=req;
        if(filtre.countNotNull()==1)
        {
            if(fieldMisy[0].getType().getName().equals("double")==true || fieldMisy[0].getType().getName().equals("int")==true) req=req+" where "+fieldMisy[0].getName()+"="+filtre.valFie(fieldMisy[0]);
            else req=req+" where "+fieldMisy[0].getName()+"='"+filtre.valFie(fieldMisy[0])+"'";
        } //req=req+" where "+fieldMisy[0].getName()+"='"+filtre.valFie(fieldMisy[0])+"'";
        if(filtre.countNotNull()>1){
            req="select * from "+filtre.getClass().getSimpleName()+" where ";
            for(int i=0;i<fieldMisy.length-1;i++)
            {
                if(fieldMisy[i].getType().getName().equals("double")==true || fieldMisy[i].getType().getName().equals("int")==true) req=req+fieldMisy[i].getName()+"="+filtre.valFie(fieldMisy[i])+" and ";
                else req=req+fieldMisy[i].getName()+"='"+filtre.valFie(fieldMisy[i])+"' and ";
            }
            if(fieldMisy[fieldMisy.length-1].getType().getName().equals("double")==true || fieldMisy[fieldMisy.length-1].getType().getName().equals("int")==true) req=req+fieldMisy[fieldMisy.length-1].getName()+"="+filtre.valFie(fieldMisy[fieldMisy.length-1]);
            else req=req+fieldMisy[fieldMisy.length-1].getName()+"='"+filtre.valFie(fieldMisy[fieldMisy.length-1])+"'";
        }
        //System.out.println(req);
        return findWthReq(req,filtre,con);
    }
}