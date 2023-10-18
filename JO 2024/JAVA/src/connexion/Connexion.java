package connexion;

import java.sql.*;
import java.util.*;

public class Connexion
{
	Connection con;

	public void setCon(Connection c)
	{
		con=c;
	}
	public Connection getCon()
	{
		return con;
	}
	
	public Connection connecter()
	{
		Connection connexion=null;
		try
		{
			Class.forName("org.postgresql.Driver");
            connexion = DriverManager
            .getConnection("jdbc:postgresql://localhost:5432/groupe2BDD","postgres", "hasina");
            setCon(connexion);
            return connexion;
		}

		catch (Exception e) {
			e.printStackTrace();
         	System.err.println(e.getClass().getName()+": "+e.getMessage());
         	System.exit(0);
		}
		return connexion;
	}
}
