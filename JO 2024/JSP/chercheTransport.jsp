<%@ page import="java.sql.*,java.util.List,java.util.ArrayList, connexion.*, bdd.*, client.*" %>

<html>
    <head>
        <title>transports</title>
        <link rel="stylesheet" type="text/css" href="css/Style.css">
      </head>
  <body>
    <nav> 
        <div class="navbar" id="navbar">
            <div class="menu"> 
                <a class="nav-link" href="Pays.jsp">Pays Participants</a>
                <a class="nav-link-active" href="transport.jsp">transports</a>
                <div class="dropdown-simple">
                    <a class="nav-link" href="#">Sports</a>
                    <div class="dropdown-content">
                        <div class="dropdown-row">
                            <div class="dropdown-column">
                                <ul>
                                    <li><a href="Sport_Jo.jsp">Sports Olympiques</a></li>
                                </ul>
                            </div>
                            <div class="dropdown-column">
                                <ul>
                                    <li><a href="Sport_Jp.jsp">Sports Paralympiques</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="dropdown-simple">
                    <a class="nav-link" href="#">Sessions</a>
                    <div class="dropdown-content">
                        <div class="dropdown-row">
                            <div class="dropdown-column">
                                <ul>
                                    <li><a href="Session_JO.jsp">Sessions Olympiques</a></li>
                                </ul>
                            </div>
                            <div class="dropdown-column">
                                <ul>
                                    <li><a href="Session_JP.jsp">Sessions Paralympiques</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <a class="nav-link" href="Epreuve.jsp">Epreuves</a>
                <a class="nav-link" href="DetenteurRecord.jsp">Detenteurs de records</a>
                <a class="nav-link" href="Recherche.jsp">RECHERCHE AVANCEE</a>
    
            </div>
            <div class="search-bar"> 
                <form class="search-bar-form">
    
                    <input class="search-bar-input"  type="search" onfocusout="this.value=''" placeholder="Rechercher..."  autocomplete="off" required><i class="fa fa-search" ></i>
    
                    <div id="suggestions"></div>
    
                </form>
    
            </div>
    
        </div>
    
        </nav>
        <div class = "fond">
            <img src="/css/fond.png" alt="">
        </div>
        <%
    //On recupere les valeurs des input
    String siteName = request.getParameter("nom-site").trim();
    
    Fonction f = new Fonction();
    Connection con = null;
    Deconnexion decon = new Deconnexion();
    BDTable bd = new BDTable();
    Transport transport = new Transport();
    Connexion c = null;
    List<Transport> listetransport = new ArrayList<Transport>();
    try {
        c = new Connexion();
        c.connecter();
        con = c.getCon();
        java.sql.Statement stmt = con.createStatement();
        String requete = "select id_transport,nom_type_transport,caracteristique from type_transport INNER JOIN transport USING(id_type_transport) INNER JOIN site USING(id_site) where nom_site like '%" + siteName + "%'";
        BDTable[] ltransport = f.findWthReq(requete, transport, con);
        out.println("<div class='table-wrapper'>");
            out.println("<table class ='fl-table'>");
                out.println("<tr><th>ID</th><th>Type de transport</th><th>caracteristique</th></tr>");
                for (int i = 0; i < ltransport.length; i++) {
                listetransport.add((Transport) ltransport[i]);
                out.println("<tr><td>" + listetransport.get(i).getId_Transport()+ "</td><td>" + listetransport.get(i).getId_Type_Transport() + "</td><td>" + listetransport.get(i).getId_Site()+ "</td></tr>");
          }
          out.println("</table>");
          out.println("</div>");
    } catch (SQLException e1) {
        out.println(e1.getMessage());
        if (c.getCon() != null) {
            con.rollback();
        }
    } catch (Exception e2) {
        out.println(e2.getMessage());
    } finally {
        if (c.getCon() != null) {
            decon.deconnect(c);
        }
    }
%>
    
  </body>
</html>