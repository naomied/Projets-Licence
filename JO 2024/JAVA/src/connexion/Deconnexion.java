package connexion;
import java.sql.*;
public class Deconnexion
{
	public void deconnect(Connexion con) throws Exception
	{
		con.getCon().close();
	}
}