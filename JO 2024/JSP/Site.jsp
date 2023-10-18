<%@ page import="java.sql.*, connexion.*, bdd.*, client.*" %>
<%
        Fonction f = new Fonction();
        Connection con = null;
        Deconnexion decon = new Deconnexion();
        BDTable bd = new BDTable();
        Site site = new Site();
        Connexion c = null;
        try {
            System.out.println("tafiditra anaty try");
            c = new Connexion();
            c.connecter();
            con = c.getCon();
            java.sql.Statement stmt = con.createStatement();
            System.out.println("tonga");

            String requete = "select * from Site";
            System.out.println(requete);
            BDTable[] lSite = f.findWthReq(requete, site, con);

            Site[] listeSite = new Site[lSite.length];
            
            out.println("<div class='table-wrapper'>");
                out.println("<table class ='fl-table'>");
                    out.println("<tr><th>ID</th><th>Nom du site</th><th>Capacite</th><th>Date Construction</th><th>Adresse</th></tr>");
                 for (int i = 0; i < lSite.length; i++) {
                    listeSite[i] = (Site) lSite[i];
                    out.println("<tr><td>" + listeSite[i].getId_Site() + "</td><td>" + listeSite[i].getNom_Site() + "</td><td>" + listeSite[i].getCapacite() + "</td><td>" + listeSite[i].getDate_construction() + "</td><td>" + listeSite[i].getAdresse() + "</td></tr>");
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
<html>
    <head>
        <title>Sites</title>
        <link rel="stylesheet" type="text/css" href="css/Style.css">
      </head>
  <body>
    <nav> 
        <div class="navbar" id="navbar">
            <div class="menu"> 
                <a class="nav-link" href="Pays.jsp">Pays Participants</a>
                <a class="nav-link-active" href="Site.jsp">Sites</a>
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
    
  </body>
</html>