package bdd;
import java.io.*;
import java.util.*;
import java.sql.*;
import java.lang.reflect.Method;
import java.lang.reflect.Field;
public class BDTable
{
    /** Retourne le nom d'une méthode (get+fieldname)*/
    public String functGet (String attr)
    {
        StringBuilder ns=new StringBuilder(attr);
        ns.setCharAt(0,Character.toUpperCase(attr.charAt(0)));
        String namef="get"+ns.toString();
        return namef;
    }

    public Object valFie(Field f) throws Exception
    {
        Method[] fn=this.getClass().getDeclaredMethods();
        Object val=null;
        for(int i=0;i<fn.length;i++)
        {
            if(fn[i].getName().equals(functGet(f.getName()))==true) val=fn[i].invoke(this);
        }
        return val;
    }

    public int countNotNull() throws Exception
    {
        int isa=0;
        //Method[] fn=this.getClass().getDeclaredMethods();
        Field[] attr=this.getClass().getDeclaredFields();
        for(int i=0;i<attr.length;i++)
        {
            //if(fn[i].getName().startsWith("get")==true && fn[i].invoke(this)!=null) 
            if((attr[i].getType().getName().equals("double")==false && attr[i].getType().getName().equals("int")==false && valFie(attr[i])!=null) 
            || (attr[i].getType().getName().equals("double")==true && ((Double)valFie(attr[i]))!=0)
            || (attr[i].getType().getName().equals("int")==true && ((Integer)valFie(attr[i]))!=0))
            isa++;
        }
        return isa;
    }

    public int countGet() throws Exception
    {
        int isa=0;
        Method[] fn=this.getClass().getDeclaredMethods();
        for(int i=0;i<fn.length;i++)
        {
            if(fn[i].getName().startsWith("get")==true) isa++;
        }
        return isa;
    }

    public Method[] methNotNull() throws Exception
    {
        Method[] val=new Method[countNotNull()];
        Method[] fn=this.getClass().getDeclaredMethods();
        int ind=0;
        for(int i=0;i<fn.length;i++)
        {
            if(fn[i].getName().startsWith("get")==true && fn[i].invoke(this)!=null) 
            {
                val[ind]=fn[i];
                ind++;
            }
        }
        return val;
    }

    public Method[] methGet() throws Exception
    {
        Method[] val=new Method[countGet()];
        Method[] fn=this.getClass().getDeclaredMethods();
        int ind=0;
        for(int i=0;i<fn.length;i++)
        {
            if(fn[i].getName().startsWith("get")==true) 
            {
                val[ind]=fn[i];
                ind++;
            }
        }
        return val;
    }

    public Field[] fieldNotNull() throws Exception
    {
        Field[] attr=this.getClass().getDeclaredFields();
        Field[] val=new Field[countNotNull()];
        Method[] fn=methGet();
        int ind=0;
        for(int i=0;i<attr.length;i++)
        {
            if((attr[i].getType().getName().equals("double")==false && attr[i].getType().getName().equals("int")==false && valFie(attr[i])!=null) 
            || (attr[i].getType().getName().equals("double")==true && ((Double)valFie(attr[i]))!=0)
            || (attr[i].getType().getName().equals("int")==true && ((Integer)valFie(attr[i]))!=0))
            { 
                val[ind]=attr[i];
                ind++;
            }
        }
        return val;
    }

    public Method methId() throws Exception
    {
        Method[] lm=this.getClass().getDeclaredMethods();
        Method val=lm[0];
        for(int i=0;i<lm.length;i++)
        {
            if(lm[i].getName().equals("getId"+getClass().getSimpleName())==true) val=lm[i];
        }
        return val;
    }

    public Method methConstr() throws Exception
    {
        Method[] lm=this.getClass().getDeclaredMethods();
        Method val=lm[0];
        for(int i=0;i<lm.length;i++)
        {
            if(lm[i].getName().equals("construit")==true) {
                val=lm[i];
            }
        }
        return val;
    }

    public Field fieldId() throws Exception
    {
        Field[] lm=this.getClass().getDeclaredFields();
        Field val=lm[0];
        for(int i=0;i<lm.length;i++)
        {
            if(lm[i].getName().equals("id"+getClass().getSimpleName())==true) val=lm[i];
        }
        return val;
    }

    public String claId() throws Exception
    {
        String val=new String();
        Field[] lm=this.getClass().getDeclaredFields();
        val=((String)methId().invoke(this));
        return val;
    }
    public static String toUpperFirst(String a) {
        char[] toChar = a.toCharArray();
        char[] f = new char[1];
        f[0] = toChar[0];
        String first = new String(f);
        String other;
        char[] oth = new char[toChar.length - 1];
        for (int i = 0; i < oth.length; i++) {
            oth[i] = toChar[i + 1];
        }
        other = new String(oth);
        return first.toUpperCase() + other;
    }
    
}